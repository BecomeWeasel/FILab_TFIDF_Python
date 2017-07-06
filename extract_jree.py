# -*- coding: utf-8 -*-
"""
Functions to extract various elements of interest from documents already parsed
by `spaCy <http://spacy.io/>`_, such as n-grams, named entities, subject-verb-object
triples, and acronyms.
"""
from __future__ import absolute_import, division, print_function, unicode_literals

from collections import defaultdict
from itertools import takewhile
from operator import itemgetter
import re

from cytoolz import itertoolz
from numpy import nanmin, nanmax, zeros, NaN
from spacy.parts_of_speech import CONJ, DET, NOUN, VERB
from spacy.tokens.span import Span as SpacySpan

import spacy_utils_jree
from spacy_utils_jree import (normalized_str, get_main_verbs_of_sent,
                                 get_subjects_of_verb, get_objects_of_verb,
                                 get_span_for_compound_noun,
                                 get_span_for_verb_auxiliaries,
    get_hyphen_words_of_sent)


import textacy
#from textacy import spacy_utils, text_utils
from textacy import text_utils
from textacy.compat import unicode_
#from textacy.spacy_utils import (normalized_str, get_main_verbs_of_sent,
#                                 get_subjects_of_verb, get_objects_of_verb,
#                                 get_span_for_compound_noun,
#                                 get_span_for_verb_auxiliaries)
from textacy.constants import NUMERIC_NE_TYPES, REPORTING_VERBS


def words(doc,
          filter_stops=True, filter_punct=True, filter_nums=False,
          include_pos=None, exclude_pos=None, min_freq=1):
    """
    Extract an ordered sequence of words from a document processed by spaCy,
    optionally filtering words by part-of-speech tag and frequency.

    Args:
        doc (``textacy.Doc``, ``spacy.Doc``, or ``spacy.Span``)
        filter_stops (bool): if True, remove stop words from word list
        filter_punct (bool): if True, remove punctuation from word list
        filter_nums (bool): if True, remove number-like words (e.g. 10, 'ten')
            from word list
        include_pos (str or Set[str]): remove words whose part-of-speech tag
            IS NOT included in this param
        exclude_pos (str or Set[str]): remove words whose part-of-speech tag
            IS in the specified tags
        min_freq (int): remove words that occur in `doc` fewer than
            `min_freq` times

    Yields:
        ``spacy.Token``: the next token from ``doc`` passing specified filters
            in order of appearance in the document

    Raises:
        TypeError: if `include_pos` or `exclude_pos` is not a str, a set of str,
            or a falsy value

    .. note:: Filtering by part-of-speech tag uses the universal POS tag set,
        http://universaldependencies.org/u/pos/
    """
    words_ = (w for w in doc if not w.is_space)
    if filter_stops is True:
        words_ = (w for w in words_ if not w.is_stop)
    if filter_punct is True:
        words_ = (w for w in words_ if not w.is_punct)
    if filter_nums is True:
        words_ = (w for w in words_ if not w.like_num)
    if include_pos:
        if isinstance(include_pos, unicode_):
            include_pos = include_pos.upper()
            words_ = (w for w in words_ if w.pos_ == include_pos)
        elif isinstance(include_pos, (set, frozenset, list, tuple)):
            include_pos = {pos.upper() for pos in include_pos}
            words_ = (w for w in words_ if w.pos_ in include_pos)
        else:
            msg = 'invalid `include_pos` type: "{}"'.format(type(include_pos))
            raise TypeError(msg)
    if exclude_pos:
        if isinstance(exclude_pos, unicode_):
            exclude_pos = exclude_pos.upper()
            words_ = (w for w in words_ if w.pos_ != exclude_pos)
        elif isinstance(exclude_pos, (set, frozenset, list, tuple)):
            exclude_pos = {pos.upper() for pos in exclude_pos}
            words_ = (w for w in words_ if w.pos_ not in exclude_pos)
        else:
            msg = 'invalid `exclude_pos` type: "{}"'.format(type(exclude_pos))
            raise TypeError(msg)
    if min_freq > 1:
        words_ = list(words_)
        freqs = itertoolz.frequencies(normalized_str(w) for w in words_)
        words_ = (w for w in words_
                  if freqs[normalized_str(w)] >= min_freq)

    for word in words_:
        yield word


def ngrams(doc, n,
           filter_stops=True, filter_punct=True, filter_nums=False,
           include_pos=None, exclude_pos=None, min_freq=1):
    """
    Extract an ordered sequence of n-grams (``n`` consecutive words) from a
    spacy-parsed doc, optionally filtering n-grams by the types and
    parts-of-speech of the constituent words.

    Args:
        doc (``textacy.Doc``, ``spacy.Doc``, or ``spacy.Span``)
        n (int): number of tokens per n-gram; 2 => bigrams, 3 => trigrams, etc.
        filter_stops (bool): if True, remove ngrams that start or end
            with a stop word
        filter_punct (bool): if True, remove ngrams that contain
            any punctuation-only tokens
        filter_nums (bool): if True, remove ngrams that contain
            any numbers or number-like tokens (e.g. 10, 'ten')
        include_pos (str or Set[str]): remove ngrams if any of their constituent
            tokens' part-of-speech tags ARE NOT included in this param
        exclude_pos (str or Set[str]): remove ngrams if any of their constituent
            tokens' part-of-speech tags ARE included in this param
        min_freq (int, optional): remove ngrams that occur in `doc` fewer than
            `min_freq` times

    Yields:
        ``spacy.Span``: the next ngram from ``doc`` passing all specified
            filters, in order of appearance in the document

    Raises:
        ValueError: if ``n`` < 1
        TypeError: if `include_pos` or `exclude_pos` is not a str, a set of str,
            or a falsy value

    .. note:: Filtering by part-of-speech tag uses the universal POS tag set,
        http://universaldependencies.org/u/pos/
    """
    if n < 1:
        raise ValueError('n must be greater than or equal to 1')

    ngrams_ = (doc[i: i + n]
               for i in range(len(doc) - n + 1))
    ngrams_ = (ngram for ngram in ngrams_
               if not any(w.is_space for w in ngram))
    if filter_stops is True:
        ngrams_ = (ngram for ngram in ngrams_
                   if not ngram[0].is_stop and not ngram[-1].is_stop)
    if filter_punct is True:
        ngrams_ = (ngram for ngram in ngrams_
                   if not any(w.is_punct for w in ngram))
    if filter_nums is True:
        ngrams_ = (ngram for ngram in ngrams_
                   if not any(w.like_num for w in ngram))
    if include_pos:
        if isinstance(include_pos, unicode_):
            include_pos = include_pos.upper()
            ngrams_ = (ngram for ngram in ngrams_
                       if all(w.pos_ == include_pos for w in ngram))
        elif isinstance(include_pos, (set, frozenset, list, tuple)):
            include_pos = {pos.upper() for pos in include_pos}
            ngrams_ = (ngram for ngram in ngrams_
                       if all(w.pos_ in include_pos for w in ngram))
        else:
            msg = 'invalid `include_pos` type: "{}"'.format(type(include_pos))
            raise TypeError(msg)
    if exclude_pos:
        if isinstance(exclude_pos, unicode_):
            exclude_pos = exclude_pos.upper()
            ngrams_ = (ngram for ngram in ngrams_
                       if all(w.pos_ != exclude_pos for w in ngram))
        elif isinstance(exclude_pos, (set, frozenset, list, tuple)):
            exclude_pos = {pos.upper() for pos in exclude_pos}
            ngrams_ = (ngram for ngram in ngrams_
                       if all(w.pos_ not in exclude_pos for w in ngram))
        else:
            msg = 'invalid `exclude_pos` type: "{}"'.format(type(exclude_pos))
            raise TypeError(msg)
    if min_freq > 1:
        ngrams_ = list(ngrams_)
        freqs = itertoolz.frequencies(normalized_str(ngram) for ngram in ngrams_)
        ngrams_ = (ngram for ngram in ngrams_
                   if freqs[normalized_str(ngram)] >= min_freq)

    for ngram in ngrams_:
        yield ngram


def named_entities(doc,
                   include_types=None, exclude_types=None,
                   drop_determiners=True, min_freq=1):
    """
    Extract an ordered sequence of named entities (PERSON, ORG, LOC, etc.) from
    a spacy-parsed doc, optionally filtering by entity types and frequencies.

    Args:
        doc (``textacy.Doc`` or ``spacy.Doc``)
        include_types (str or Set[str]): remove named entities whose type IS NOT
            in this param; if "NUMERIC", all numeric entity types ("DATE",
            "MONEY", "ORDINAL", etc.) are included
        exclude_types (str or Set[str]): remove named entities whose type IS
            in this param; if "NUMERIC", all numeric entity types ("DATE",
            "MONEY", "ORDINAL", etc.) are excluded
        drop_determiners (bool): remove leading determiners (e.g. "the")
            from named entities (e.g. "the United States" => "United States")
        min_freq (int): remove named entities that occur in `doc` fewer
            than `min_freq` times

    Yields:
        ``spacy.Span``: the next named entity from ``doc`` passing all specified
            filters in order of appearance in the document

    Raise:
        TypeError: if `include_types` or `exclude_types` is not a str, a set of
            str, or a falsy value
    """
    if isinstance(doc, textacy.Doc):
        nes = doc.spacy_doc.ents
    else:
        nes = doc.ents
    if include_types:
        if isinstance(include_types, unicode_):
            include_types = include_types.upper()
            if include_types == 'NUMERIC':
                include_types = NUMERIC_NE_TYPES  # we now go to next if block
            else:
                nes = (ne for ne in nes if ne.label_ == include_types)
        if isinstance(include_types, (set, frozenset, list, tuple)):
            include_types = {type_.upper() for type_ in include_types}
            nes = (ne for ne in nes if ne.label_ in include_types)
        else:
            msg = 'invalid `include_types` type: "{}"'.format(type(include_types))
            raise TypeError(msg)
    if exclude_types:
        if isinstance(exclude_types, unicode_):
            exclude_types = exclude_types.upper()
            if exclude_types == 'NUMERIC':
                exclude_types = NUMERIC_NE_TYPES  # we now go to next if block
            else:
                nes = (ne for ne in nes if ne.label_ != exclude_types)
        if isinstance(exclude_types, (set, frozenset, list, tuple)):
            exclude_types = {type_.upper() for type_ in exclude_types}
            nes = (ne for ne in nes if ne.label_ not in exclude_types)
        else:
            msg = 'invalid `exclude_types` type: "{}"'.format(type(exclude_types))
            raise TypeError(msg)
    if drop_determiners is True:
        nes = (ne if ne[0].pos != DET else ne[1:] for ne in nes)
    if min_freq > 1:
        nes = list(nes)
        freqs = itertoolz.frequencies(ne.text for ne in nes)
        nes = (ne for ne in nes
               if freqs[ne.text] >= min_freq)

    for ne in nes:
        yield ne


def noun_chunks(doc, drop_determiners=True, min_freq=1):
    """
    Extract an ordered sequence of noun chunks from a spacy-parsed doc, optionally
    filtering by frequency and dropping leading determiners.

    Args:
        doc (``textacy.Doc`` or ``spacy.Doc``)
        drop_determiners (bool): remove leading determiners (e.g. "the")
            from phrases (e.g. "the quick brown fox" => "quick brown fox")
        min_freq (int): remove chunks that occur in `doc` fewer than
            `min_freq` times

    Yields:
        ``spacy.Span``: the next noun chunk from ``doc`` in order of appearance
             in the document
    """
    if isinstance(doc, textacy.Doc):
        ncs = doc.spacy_doc.noun_chunks
    else:
        ncs = doc.noun_chunks
    if drop_determiners is True:
        ncs = (nc if nc[0].pos != DET else nc[1:]
               for nc in ncs)
    if min_freq > 1:
        ncs = list(ncs)
        freqs = itertoolz.frequencies(normalized_str(nc) for nc in ncs)
        ncs = (nc for nc in ncs
               if freqs[normalized_str(nc)] >= min_freq)

    for nc in ncs:
        yield nc


def pos_regex_matches(doc, pattern):
    """
    Extract sequences of consecutive tokens from a spacy-parsed doc whose
    part-of-speech tags match the specified regex pattern.

    Args:
        doc (``textacy.Doc`` or ``spacy.Doc`` or ``spacy.Span``)
        pattern (str): Pattern of consecutive POS tags whose corresponding words
            are to be extracted, inspired by the regex patterns used in NLTK's
            `nltk.chunk.regexp`. Tags are uppercase, from the universal tag set;
            delimited by < and >, which are basically converted to parentheses
            with spaces as needed to correctly extract matching word sequences;
            white space in the input doesn't matter.

            Examples (see ``constants_jree.POS_REGEX_PATTERNS``):

            * noun phrase: r'<DET>? (<NOUN>+ <ADP|CONJ>)* <NOUN>+'
            * compound nouns: r'<NOUN>+'
            * verb phrase: r'<VERB>?<ADV>*<VERB>+'
            * prepositional phrase: r'<PREP> <DET>? (<NOUN>+<ADP>)* <NOUN>+'

    Yields:
        ``spacy.Span``: the next span of consecutive tokens from ``doc`` whose
            parts-of-speech match ``pattern``, in order of apperance
    """
    # standardize and transform the regular expression pattern...
    pattern = re.sub(r'\s', '', pattern)
    pattern = re.sub(r'<([A-Z]+)\|([A-Z]+)>', r'( (\1|\2))', pattern)
    pattern = re.sub(r'<([A-Z]+)>', r'( \1)', pattern)

    tags = ' ' + ' '.join(tok.pos_ for tok in doc)

    for m in re.finditer(pattern, tags):
        yield doc[tags[0:m.start()].count(' '):tags[0:m.end()].count(' ')]


def subject_verb_object_triples(doc):
    """
    Extract an ordered sequence of subject-verb-object (SVO) triples from a
    spacy-parsed doc. Note that this only works for SVO languages.

    Args:
        doc (``textacy.Doc`` or ``spacy.Doc`` or ``spacy.Span``)

    Yields:
        Tuple[``spacy.Span``, ``spacy.Span``, ``spacy.Span``]: the next 3-tuple
            of spans from ``doc`` representing a (subject, verb, object) triple,
            in order of appearance
    """
    # TODO: What to do about questions, where it may be VSO instead of SVO?
    # TODO: What about non-adjacent verb negations?
    # TODO: What about object (noun) negations?
    hyphenWordsList = []
    
    if isinstance(doc, SpacySpan):
        sents = [doc]
    else:  # textacy.Doc or spacy.Doc
        sents = doc.sents

    for sent in sents:
        start_i = sent[0].i
        
        hyphenWords, hyphenWordFound = get_hyphen_words_of_sent(sent)
        hyphenWordsList.append(hyphenWords)
        
        if hyphenWordFound is True:
            hyphenWords, hyphenWordFound = get_hyphen_words_of_sent(sent)
            hyphenWordsList.append(hyphenWords)
        if hyphenWordFound is True:
            hyphenWords, hyphenWordFound = get_hyphen_words_of_sent(sent)
            hyphenWordsList.append(hyphenWords)
        if hyphenWordFound is True:
            hyphenWords, hyphenWordFound = get_hyphen_words_of_sent(sent)
            hyphenWordsList.append(hyphenWords)
        if hyphenWordFound is True:
            hyphenWords, hyphenWordFound = get_hyphen_words_of_sent(sent)
            hyphenWordsList.append(hyphenWords)
        if hyphenWordFound is True:
            hyphenWords, hyphenWordFound = get_hyphen_words_of_sent(sent)
            hyphenWordsList.append(hyphenWords)
        
        print("=================================================================================================== HYPHEN WORDS LIST =====================================================================")
        print(hyphenWordsList)
        
        verbs = get_main_verbs_of_sent(sent)
        '''
        for verb in verbs:
            prevPrevTok = verb.nbor(-2)
            prevTok = verb.nbor(-1)
            if prevTok.text == "-" and verb.pos_ == "VERB" and verb.dep_ != "amod":
                
                print("HYPHEN VERB FOUND-------------------23452348905702398452389-44590235234950923485908234058930498502394850392485093485")
                print(verb)
        '''        
                
        for verb in verbs:
            print("Finding SUBJ/OBJ for verb:::::::::::::")
            print(verb)
            subjs = get_subjects_of_verb(verb)
            print(subjs)
            if not subjs:
                print("SUBJECTS NOT FOUNDDDDDDDDDDDDDDDDDDDDD")
                #continue
            objs = get_objects_of_verb(verb)
            print(objs)
            if not objs:
                print("OBJECTS NOT FOUNDDDDDDDDDDDDDDDDDDDDD")
                #continue

            # add adjacent auxiliaries to verbs, for context
            # and add compounds to compound nouns
            verb_span = get_span_for_verb_auxiliaries(verb)
            verb = sent[verb_span[0] - start_i: verb_span[1] - start_i + 1]
            for subj in subjs:
                subj = sent[get_span_for_compound_noun(subj)[0] - start_i: subj.i - start_i + 1]
                for obj in objs:
                    if obj.pos == NOUN:
                        span = get_span_for_compound_noun(obj)
                    elif obj.pos == VERB:
                        span = get_span_for_verb_auxiliaries(obj)
                    else:
                        span = (obj.i, obj.i)
                    obj = sent[span[0] - start_i: span[1] - start_i + 1]

                    yield [subj, verb, obj]


def acronyms_and_definitions(doc, known_acro_defs=None):
    """
    Extract a collection of acronyms and their most likely definitions, if available,
    from a spacy-parsed doc. If multiple definitions are found for a given acronym,
    only the most frequently occurring definition is returned.

    Args:
        doc (``textacy.Doc`` or ``spacy.Doc`` or ``spacy.Span``)
        known_acro_defs (dict, optional): if certain acronym/definition pairs
            are known, pass them in as {acronym (str): definition (str)};
            algorithm will not attempt to find new definitions

    Returns:
        dict: unique acronyms (keys) with matched definitions (values)

    References:
        Taghva, Kazem, and Jeff Gilbreth. "Recognizing acronyms and their definitions."
            International Journal on Document Analysis and Recognition 1.4 (1999): 191-198.
    """
    # process function arguments
    acro_defs = defaultdict(list)
    if not known_acro_defs:
        known_acronyms = set()
    else:
        for acro, defs in known_acro_defs.items():
            if not isinstance(defs, list):
                acro_defs[acro] = [defs]
        known_acronyms = set(acro_defs.keys())

    if isinstance(doc, SpacySpan):
        sents = [doc]
    else:  # textacy.Doc or spacy.Doc
        sents = doc.sents

    # iterate over sentences and their tokens
    for sent in sents:
        max_ind = len(sent) - 1

        for i, token in enumerate(sent):

            token_ = token.text
            if token_ in known_acronyms or text_utils.is_acronym(token_) is False:
                continue

            # define definition search window(s)
            window_size = min(2 * len(token_), len(token_) + 5)
            windows = [sent[max(i - window_size, 0): i],
                       sent[min(i + 1, max_ind): min(i + window_size + 1, max_ind)]]
            # if candidate inside (X) or -X-, only look in pre-window
            if 0 < i < max_ind:
                adjacent_tokens = sent[i - 1].text + sent[i + 1].text
                if adjacent_tokens in {'()', '--', '––'}:
                    windows.pop()

            # iterate over possible windows
            # filtering for valid definition strings
            for window in windows:
                window_ = window.text
                # window text can't be all uppercase
                if window_.isupper():
                    continue
                # window can't contain separating punctuation
                if '!' in window_ or '?' in window_ or ':' in window_ or ';' in window_:
                    continue
                # acronym definition can't contain itself: no ouroboros!
                if token_ in window_:
                    continue
                # window must contain at least one character used in acronym
                if not any(char in window_ for char in token_):
                    continue
                definition, confidence = _get_acronym_definition(
                    token_, window, threshold=0.8)
                if definition:
                    acro_defs[token_].append((definition, confidence))

            if not acro_defs.get(token_):
                acro_defs[token_].append(('', 0.0))

    # vote by confidence score in the case of multiple definitions
    for acro, defs in acro_defs.items():
        if len(defs) == 1:
            acro_defs[acro] = defs[0][0]
        else:
            acro_defs[acro] = sorted(defs, key=itemgetter(1), reverse=True)[0][0]

    return dict(acro_defs)


def _get_acronym_definition(acronym, window, threshold=0.8):
    """
    Identify most likely definition for an acronym given a list of tokens.

    Args:
        acronym (str): acronym for which definition is sought
        window (``spacy.Span``): a span of tokens from which definition
            extraction will be attempted
        threshold (float, optional): minimum "confidence" in definition required
            for acceptance; valid values in [0.0, 1.0]; higher value => stricter threshold

    Returns:
        Tuple[str, float]: most likely definition for given acronym ('' if none found),
            along with the confidence assigned to it

    References:
        Taghva, Kazem, and Jeff Gilbreth. "Recognizing acronyms and their definitions."
            International Journal on Document Analysis and Recognition 1.4 (1999): 191-198.
    """
    def build_lcs_matrix(X, Y):
        m = len(X)
        n = len(Y)
        b = zeros((m, n), dtype=int)
        c = zeros((m, n), dtype=int)
        for i in range(0, m):
            for j in range(0, n):
                if X[i] == Y[j]:
                    c[i, j] = c[i - 1, j - 1] + 1
                    b[i, j] = 1
                elif c[i - 1, j] >= c[i, j - 1]:
                    c[i, j] = c[i - 1, j]
                else:
                    c[i, j] = c[i, j - 1]
        return c, b

    def parse_lcs_matrix(b, start_i, start_j, lcs_length, stack, vectors):
        m = b.shape[0]
        n = b.shape[1]
        for i in range(start_i, m):
            for j in range(start_j, n):
                if b[i, j] == 1:
                    s = (i, j)
                    stack.append(s)
                    if lcs_length == 1:
                        vec = [NaN] * n
                        for k, l in stack:
                            vec[l] = k
                        vectors.append(vec)
                    else:
                        parse_lcs_matrix(b, i + 1, j + 1, lcs_length - 1, stack, vectors)
                    stack = []
        return vectors

    def vector_values(v, types):
        vv = {}
        first = v.index(int(nanmin(v)))
        last = v.index(int(nanmax(v)))
        vv['size'] = (last - first) + 1
        vv['distance'] = len(v) - last
        vv['stop_count'] = 0
        vv['misses'] = 0
        for i in range(first, last + 1):
            if v[i] >= 0 and types[i] == 's':
                vv['stop_count'] += 1
            elif v[i] is None and types[i] not in ['s', 'h']:
                vv['misses'] += 1
        return vv

    def compare_vectors(A, B, types):
        vv_A = vector_values(A, types)
        vv_B = vector_values(B, types)
        # no one-letter matches, sorryboutit
        if vv_A['size'] == 1:
            return B
        elif vv_B['size'] == 1:
            return A
        if vv_A['misses'] > vv_B['misses']:
            return B
        elif vv_A['misses'] < vv_B['misses']:
            return A
        if vv_A['stop_count'] > vv_B['stop_count']:
            return B
        if vv_A['stop_count'] < vv_B['stop_count']:
            return A
        if vv_A['distance'] > vv_B['distance']:
            return B
        elif vv_A['distance'] < vv_B['distance']:
            return A
        if vv_A['size'] > vv_B['size']:
            return B
        elif vv_A['size'] < vv_B['size']:
            return A
        return A

    # get definition window's leading characters and word types
    def_leads = []
    def_types = []
    for tok in window:
        tok_text = tok.text
        if tok.is_stop:
            def_leads.append(tok_text[0])
            def_types.append('s')
        elif text_utils.is_acronym(tok_text):
            def_leads.append(tok_text[0])
            def_types.append('a')
        elif '-' in tok_text and not tok_text.startswith('-'):
            tok_split = [t[0] for t in tok_text.split('-') if t]
            def_leads.extend(tok_split)
            def_types.extend('H' if i == 0 else 'h' for i in range(len(tok_split)))
        else:
            def_leads.append(tok_text[0])
            def_types.append('w')
    def_leads = ''.join(def_leads).lower()
    def_types = ''.join(def_types)

    # extract alphanumeric characters from acronym
    acr_leads = ''.join(c for c in acronym if c.isalnum())
    # handle special cases of '&' and trailing 's'
    acr_leads = acr_leads.replace('&', 'a')
    if acr_leads.endswith('s'):
        # bail out if it's only a 2-letter acronym to start with, e.g. 'Is'
        if len(acr_leads) == 2:
            return ('', 0)
        acr_leads = acr_leads[:-1]
    acr_leads = acr_leads.lower()

    c, b = build_lcs_matrix(acr_leads, def_leads)

    # 4.4.1
    lcs_length = c[c.shape[0] - 1, c.shape[1] - 1]
    confidence = lcs_length / len(acronym)
    if confidence < threshold:
        return ('', confidence)

    vecs = parse_lcs_matrix(b, 0, 0, lcs_length, [], [])
    # first letter of acronym must be present
    vecs = [vec for vec in vecs if 0 in vec]
    if not vecs:
        return ('', confidence)

    best_vec = vecs[0]
    for vec in vecs[1:]:
        best_vec = compare_vectors(best_vec, vec, def_types)

    first = best_vec.index(int(nanmin(best_vec)))
    last = best_vec.index(int(nanmax(best_vec)))

    definition = window[first: last + 1].text
    if len(definition.split()) == 1:
        return ('', confidence)

    return (definition, confidence)


def semistructured_statements(doc, entity, cue='be', ignore_entity_case=True,
                              min_n_words=1, max_n_words=20):
    """
    Extract "semi-structured statements" from a spacy-parsed doc, each as a
    (entity, cue, fragment) triple. This is similar to subject-verb-object triples.

    Args:
        doc (``textacy.Doc`` or ``spacy.Doc``)
        entity (str): a noun or noun phrase of some sort (e.g. "President Obama",
            "global warming", "Python")
        cue (str, optional): verb lemma with which `entity` is associated
            (e.g. "talk about", "have", "write")
        ignore_entity_case (bool, optional): if True, entity matching is case-independent
        min_n_words (int, optional): min number of tokens allowed in a matching fragment
        max_n_words (int, optional): max number of tokens allowed in a matching fragment

    Yields:
        (``spacy.Span`` or ``spacy.Token``, ``spacy.Span`` or ``spacy.Token``, ``spacy.Span``):
              where each element is a matching (entity, cue, fragment) triple

    Notes:
        Inspired by N. Diakopoulos, A. Zhang, A. Salway. Visual Analytics of
        Media Frames in Online News and Blogs. IEEE InfoVis Workshop on Text
        Visualization. October, 2013.

        Which itself was inspired by by Salway, A.; Kelly, L.; Skadiņa, I.; and
        Jones, G. 2010. Portable Extraction of Partially Structured Facts from
        the Web. In Proc. ICETAL 2010, LNAI 6233, 345-356. Heidelberg, Springer.
    """
    if ignore_entity_case is True:
        entity_toks = entity.lower().split(' ')
        get_tok_text = lambda x: x.lower_
    else:
        entity_toks = entity.split(' ')
        get_tok_text = lambda x: x.text
    first_entity_tok = entity_toks[0]
    n_entity_toks = len(entity_toks)
    cue = cue.lower()
    cue_toks = cue.split(' ')
    n_cue_toks = len(cue_toks)

    def is_good_last_tok(tok):
        if tok.is_punct:
            return False
        if tok.pos in {CONJ, DET}:
            return False
        return True

    for sent in doc.sents:
        for tok in sent:

            # filter by entity
            if get_tok_text(tok) != first_entity_tok:
                continue
            if n_entity_toks == 1:
                the_entity = tok
                the_entity_root = the_entity
            if tok.i + n_cue_toks >= len(doc):
                continue
            elif all(get_tok_text(tok.nbor(i=i + 1)) == et for i, et in enumerate(entity_toks[1:])):
                the_entity = doc[tok.i: tok.i + n_entity_toks]
                the_entity_root = the_entity.root
            else:
                continue

            # filter by cue
            terh = the_entity_root.head
            if terh.lemma_ != cue_toks[0]:
                continue
            if n_cue_toks == 1:
                min_cue_i = terh.i
                max_cue_i = terh.i + n_cue_toks
                the_cue = terh
            elif all(terh.nbor(i=i + 1).lemma_ == ct for i, ct in enumerate(cue_toks[1:])):
                min_cue_i = terh.i
                max_cue_i = terh.i + n_cue_toks
                the_cue = doc[terh.i: max_cue_i]
            else:
                continue
            if the_entity_root in the_cue.rights:
                continue

            # now add adjacent auxiliary and negating tokens to the cue, for context
            try:
                min_cue_i = min(left.i for left in takewhile(
                    lambda x: x.dep_ in {'aux', 'neg'}, reversed(list(the_cue.lefts))))
            except ValueError:
                pass
            try:
                max_cue_i = max(right.i for right in takewhile(
                    lambda x: x.dep_ in {'aux', 'neg'}, the_cue.rights))
            except ValueError:
                pass
            if max_cue_i - min_cue_i > 1:
                the_cue = doc[min_cue_i: max_cue_i]
            else:
                the_cue = doc[min_cue_i]

            # filter by fragment
            try:
                min_frag_i = min(right.left_edge.i for right in the_cue.rights)
                max_frag_i = max(right.right_edge.i for right in the_cue.rights)
            except ValueError:
                continue
            while is_good_last_tok(doc[max_frag_i]) is False:
                max_frag_i -= 1
            n_fragment_toks = max_frag_i - min_frag_i
            if n_fragment_toks <= 0 or n_fragment_toks < min_n_words or n_fragment_toks > max_n_words:
                continue
            # HACK...
            if min_frag_i == max_cue_i - 1:
                min_frag_i += 1
            the_fragment = doc[min_frag_i: max_frag_i + 1]

            yield (the_entity, the_cue, the_fragment)


def direct_quotations(doc):
    """
    Baseline, not-great attempt at direction quotation extraction (no indirect
    or mixed quotations) using rules and patterns. English only.

    Args:
        doc (``textacy.Doc`` or ``spacy.Doc``)

    Yields:
        (``spacy.Span``, ``spacy.Token``, ``spacy.Span``): next quotation in ``doc``
            represented as a (speaker, reporting verb, quotation) 3-tuple

    Notes:
        Loosely inspired by Krestel, Bergler, Witte. "Minding the Source: Automatic
        Tagging of Reported Speech in Newspaper Articles".

    TODO: Better approach would use ML, but needs a training dataset.
    """
    if isinstance(doc, textacy.Doc):
        if doc.lang != 'en':
            raise NotImplementedError('sorry, English-language texts only :(')
        doc = doc.spacy_doc
    quote_end_punct = {',', '.', '?', '!'}
    quote_indexes = set(itertoolz.concat(
        (m.start(), m.end() - 1) for m in re.finditer(r"(\".*?\")|(''.*?'')|(``.*?'')", doc.string)))
    quote_positions = list(itertoolz.partition(
        2, sorted(tok.i for tok in doc if tok.idx in quote_indexes)))
    sents = list(doc.sents)
    sent_positions = [(sent.start, sent.end) for sent in sents]

    for q0, q1 in quote_positions:
        quote = doc[q0: q1 + 1]

        # we're only looking for direct quotes, not indirect or mixed
        if not any(char in quote_end_punct for char in quote.text[-4:]):
            continue

        # get adjacent sentences
        candidate_sent_indexes = []
        for i, (s0, s1) in enumerate(sent_positions):

            if s0 <= q1 + 1 and s1 > q1:
                candidate_sent_indexes.append(i)
            elif s0 < q0 and s1 >= q0 - 1:
                candidate_sent_indexes.append(i)

        for si in candidate_sent_indexes:
            sent = sents[si]

            # get any reporting verbs
            rvs = [tok for tok in sent
                   if spacy_utils.preserve_case(tok) is False and
                   tok.lemma_ in REPORTING_VERBS and
                   tok.pos_ == 'VERB' and
                   not any(oq0 <= tok.i <= oq1 for oq0, oq1 in quote_positions)]

            # get target offset against which to measure distances of NEs
            if rvs:
                if len(rvs) == 1:
                    rv = rvs[0]
                else:
                    min_rv_dist = 1000
                    for rv_candidate in rvs:
                        rv_dist = min(abs(rv_candidate.i - qp) for qp in (q0, q1))
                        if rv_dist < min_rv_dist:
                            rv = rv_candidate
                            min_rv_dist = rv_dist
                        else:
                            break
            else:
                # TODO: do we have no other recourse?!
                continue

            try:
                # rv_subj = _find_subjects(rv)[0]
                rv_subj = get_subjects_of_verb(rv)[0]
            except IndexError:
                continue
    #         if rv_subj.text in {'he', 'she'}:
    #             for ne in named_entities(doc, good_ne_types={'PERSON'}):
    #                 if ne.start < rv_subj.i:
    #                     speaker = ne
    #                 else:
    #                     break
    #         else:
            span = get_span_for_compound_noun(rv_subj)
            speaker = doc[span[0]: span[1] + 1]

            yield (speaker, rv, quote)
            break
