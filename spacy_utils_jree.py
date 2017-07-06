"""
Set of small utility functions that take Spacy objects as input.
"""
from __future__ import absolute_import, division, print_function, unicode_literals

from itertools import takewhile
import logging
import spacy
from spacy.en import English
from spacy.en import language_data
from spacy.en import tokenizer_exceptions
from spacy.en.language_data import update_exc, strings_to_exc
from spacy.en.language_data import TOKENIZER_EXCEPTIONS, ORTH
from spacy import symbols
from spacy.symbols import *

from spacy.parts_of_speech import NOUN, PROPN, VERB
from spacy.tokens.token import Token as SpacyToken
from spacy.tokens.span import Span as SpacySpan

import textacy
from textacy.text_utils import is_acronym
from textacy.constants import AUX_DEPS, SUBJ_DEPS, OBJ_DEPS



logger = logging.getLogger(__name__)


def is_plural_noun(token):
    """
    Returns True if token is a plural noun, False otherwise.

    Args:
        token (``spacy.Token``): parent document must have POS information

    Returns:
        bool
    """
    if token.doc.is_tagged is False:
        raise ValueError('token is not POS-tagged')
    return True if token.pos == NOUN and token.lemma != token.lower else False


def is_negated_verb(token):
    """
    Returns True if verb is negated by one of its (dependency parse) children,
    False otherwise.

    Args:
        token (``spacy.Token``): parent document must have parse information

    Returns:
        bool

    TODO: generalize to other parts of speech; rule-based is pretty lacking,
    so will probably require training a model; this is an unsolved research problem
    """
    if token.doc.is_parsed is False:
        raise ValueError('token is not parsed')
    if token.pos == VERB and any(c.dep_ == 'neg' for c in token.children):
        return True
    # if (token.pos == NOUN
    #         and any(c.dep_ == 'det' and c.lower_ == 'no' for c in token.children)):
    #     return True
    return False


def preserve_case(token):
    """
    Returns True if `token` is a proper noun or acronym, False otherwise.

    Args:
        token (``spacy.Token``): parent document must have POS information

    Returns:
        bool
    """
    if token.doc.is_tagged is False:
        raise ValueError('token is not POS-tagged')
    return token.pos == PROPN or is_acronym(token.text)


def normalized_str(token):
    """
    Return as-is text for tokens that are proper nouns or acronyms, lemmatized
    text for everything else.

    Args:
        token (``spacy.Token`` or ``spacy.Span``)

    Returns:
        str
    """
    if isinstance(token, SpacyToken):
        return token.text if preserve_case(token) else token.lemma_
    elif isinstance(token, SpacySpan):
        return ' '.join(subtok.text if preserve_case(subtok) else subtok.lemma_
                        for subtok in token)
    else:
        msg = 'Input must be a spacy Token or Span, not {}.'.format(type(token))
        raise TypeError(msg)


def merge_spans(spans):
    """
    Merge spans *in-place* within parent doc so that each takes up a single token.

    Args:
        spans (Iterable[``spacy.Span``])
    """
    for span in spans:
        try:
            span.merge(span.root.tag_, span.text, span.root.ent_type_)
        except IndexError as e:
            logger.error(e)

def get_merge_hyphen_word(sent, spanStart, spanEnd, tok, tokPOS, tokDep):
    
    newWord = sent[spanStart:spanEnd]
    
    print("NEW WORD: " + newWord.text)
    print("TOK: " + tok.text)
    print("TOKPOS: " + tokPOS)
    print("TOKDEP: " + tokDep)
    print("NEWWORD ROOT: " + newWord.root.text)
    print("NEWWORD POS: " + newWord.root.pos_)
    print("NEWWORD DEP: " + newWord.root.dep_)
    
    mergedNewWord = newWord.merge()
    
    print("MERGED WORD: " + mergedNewWord.text  + " POS: " + mergedNewWord.pos_ + " DEP: " + mergedNewWord.dep_)
    
    return mergedNewWord

def get_hyphen_words_of_sent(sent):
    
    hyphenWords = []
    tokNumber = 0
    tokPOS = ''
    tokDep = ''
    hyphenWordFound = False
    
    for tok in sent:
                                    #### SINGLE HYPHEN WORD #################   DOUBLE HYPHEN WORD  ###################
        try:
            prevX3Tok = tok.nbor(-3)    #                               #
        except:
            None
        try:
            prevX2Tok = tok.nbor(-2)    # WORD PRIOR TO HYPHEN          #    WORD PRIOR TO HYPHEN
        except:
            None
        prevTok = tok.nbor(-1)      # POSSIBLE HYPHEN               #    #1 POSSIBLE HYPHEN
        ##TOKTOKTOKTOKTOKTOKTOKTOK  #                      [[[[[ MAIN TOKEN ]]]]]  
        try:
            afterTok = tok.nbor(1)      # 1ST WORD AFTER HYPHEN WORD    #    #2 POSSIBLE HYPHEN IF DOUBLE HYPHENATED WORD
        except:
            None
        try:
            afterX2Tok = tok.nbor(2)    # 2ND WORD AFTER HYPHEN WORD    #    LAST WORD IN HYPHEN WORD
        except:
            None
        #if tok.nbor(3) is not None:
        try:
            afterX3Tok = tok.nbor(3)    # 3RD WORD AFTER HYPHEN WORD    #    1ST WORD AFTER HYPHEN WORD
        except:
            None
        #if tok.nbor(4) is not None:
        #   afterX4Tok = tok.nbor(4)    # 4TH WORD AFTER HYPHEN WORD    #    2ND WORD AFTER HYPHEN WORD
        #afterX5Tok = tok.nbor(5)    # 5TH WORD AFTER HYPHEN WORD    #    3RD WORD AFTER HYPHEN WORD
        #afterX6Tok = tok.nbor(6)    # 6TH WORD AFTER HYPHEN WORD    #    4TH WORD AFTER HYPHEN WORD
        
        isCompoundNoun = False
        
        '''
        print("ATTEMPTING TO FIND HYPHEN WORD: " + str(tokNumber))
        print(tok)
        print(afterTok)
        '''
        if afterTok.pos_ == 'SPACE':
            continue
        
        #######################
        # Double hyphenated word
        #######################
        if prevTok.text == '-' and afterTok.text == '-':
            #COMPOUND NOUN/PRONOUN = NOUN
            if (prevX2Tok.pos_ == 'NOUN' or 'PROPN' and tok.pos_ == 'NOUN' or 'PROPN' 
                and afterX2Tok.pos_ == 'NOUN' or 'PROPN' and afterX3Tok.pos_ == 'VERB'):
                tokPOS == 'NOUN'    
            #COMPOUND ADJ = ADJ
            if (prevX2Tok.pos_ == 'NOUN' or 'PROPN' and tok.pos_ == 'ADJ'):
                tokPOS = 'ADJ'
            if (prevX2Tok.pos_ == 'NOUN' or 'PROPN' and tok.pos_ == 'PART'):
                tokPOS = 'ADJ'
            if (prevX2Tok.pos_ == u'ADJ' and tok.pos_ == 'PART'):
                tokPOS = 'ADJ'
            #COMPOUND VERB
            if (prevX2Tok.pos_ == 'NOUN' and tok.pos_ == 'NOUN' and afterX2Tok.pos_ == 'NOUN' and afterX3Tok.pos_ != 'VERB' and afterX3Tok.pos_ != 'VERB'):
                tokPOS = 'VERB'
            if all ([prevX2Tok.pos_ == 'NOUN', tok.pos_ == 'VERB']):
                tokPOS = 'VERB'
            #NUMBER-NUMBER = NUMBER    
            #if all ([hyphen_tag[1] == u'NUM', nextX2_tag[1] == u'NUM']):
            #    hyphen_tag[1] = u'NUM'
            #Exception such as when tagger makes mistake
            if (afterX3Tok.pos_ == 'NOUN' or 'PROPN'):
                tokPOS = 'ADJ'
            if (afterX2Tok.pos_ == u'ADJ' and afterX3Tok.pos_ == 'NOUN'):
                tokPOS = 'ADJ'
            tokDep = afterX2Tok.dep_
            
            
            newHyphenWord = get_merge_hyphen_word(sent, tokNumber-2, tokNumber+3, tok, tokPOS, tokDep)
            hyphenWords.append(newHyphenWord)
            hyphenWordFound = True
            break
            
        #######################
        # Single hyphenated word
        #######################
        if prevTok.text == '-' and afterTok.text != '-':
            #COMPOUND NOUN/PRONOUN = NOUN
            if (((prevX2Tok.pos_ == 'NOUN') or (prevX2Tok.pos_ == 'PROPN')) 
                and ((tok.pos_ == 'NOUN') or (tok.pos_ == 'PROPN')) 
                and ((afterTok.pos_ == 'VERB') or (afterTok.pos_ == 'PUNCT') or (afterTok.pos_ == 'CONJ') or (afterTok.pos_ == 'ADP') ) ):
                tokPOS = 'NOUN'
                isCompoundNoun = True
            
            #COMPOUND ADJ
            if((prevX2Tok.pos_ == ('NOUN' or 'PROPN')) and (tok.pos_ == 'ADJ') and (afterTok.pos_ == 'ADJ' or afterTok.pos_ == 'NOUN')):
                tokPOS = 'ADJ'
            if((prevX2Tok.pos_ == ('NOUN' or 'PROPN')) and (tok.pos_ == 'PART') and (tok.pos_ != 'VERB')):
                tokPOS = 'ADJ'
            if((prevX2Tok.pos_ == 'ADJ') and (tok.pos_ == 'PART')):
                tokPOS = 'ADJ'
            
            #COMPOUND VERB
            if((prevX2Tok.pos_ == 'NOUN') and (tok.pos_ == 'NOUN') and (afterTok.pos_ != 'VERB') and (afterX2Tok.pos_ != 'VERB')):
                if isCompoundNoun == True:
                    tokPOS = 'NOUN'
                if isCompoundNoun == False:
                    tokPOS = 'VERB'
            if((prevX2Tok.pos_ == 'NOUN') and (tok.pos_ == 'VERB') and (prevX2Tok.text != "un") and (prevX2Tok.text != "re") and (prevX2Tok.text != "ir")):
                tokPOS = 'VERB'
                
            # EXCEPTION SUCH AS WHEN TAGGER MAKES MISTAKE
            if ((afterTok.pos_ == 'NOUN' or 'PROPN') and (afterTok.pos_ != 'PART') and (afterTok.pos_ != 'ADP') and (afterTok.pos_ != 'PUNCT')):
                tokPOS = 'ADJ'
            if((afterTok.pos_ == 'ADJ') and (afterX2Tok.pos_ == 'NOUN')):
                tokPOS = 'ADJ'
            if ((prevX2Tok.pos_ == 'NUM') and (tok.pos_ == 'NUM')):
                tokPOS = 'NUM'
            if ((prevX2Tok.pos_ == 'NOUN') and (tok.pos_ == 'ADV')):
                tokPOS = 'ADV'
            if ((prevX2Tok.pos_ == 'ADV') and (tok.pos_ == 'VERB')):
                tokPOS = 'ADJ'
            tokDep = tok.dep_
            
            newHyphenWord = get_merge_hyphen_word(sent, tokNumber-2, tokNumber+1, tok, tokPOS, tokDep)
            hyphenWords.append(newHyphenWord)
            hyphenWordFound = True
            break
        tokNumber += 1
        
        
    return hyphenWords,hyphenWordFound

def get_main_verbs_of_sent(sent):
    """Return the main (non-auxiliary) verbs in a sentence."""
    tok_tags = []
    prevTok_tags = []
    prevPrevTok_tags = []
    mainVerb = []
    mainVerbWithTokNumber = []
    
    
    tokNumber = 0
    for tok in sent:

        foundHyphenVerb = False
        hyphenIfStatementEntered = False
        prevTok = tok.nbor(-1)
        prevPrevTok = tok.nbor(-2)
        
        '''
        print("****************************BEFORE IF STATEMENTS TO FIND HYPHEN VERB*********************************************")
        print("PrevPrevTok: " + prevPrevTok.text)
        print("PrevTok: " + prevTok.text)
        print("Tok: " + tok.text)
        '''
        
        '''
        tok_tags.append((tok, tok.text, tok.pos_, tok.dep_))
        prevTok_tags.append((prevTok, prevTok.text, prevTok.pos_, prevTok.dep_))
        prevPrevTok_tags.append((prevPrevTok, prevPrevTok.text, prevPrevTok.pos_, prevPrevTok.dep_))
        '''
        
        
        '''
        if prevTok.text == '-' and tok.pos == VERB and tok.dep_ not in {'aux', 'auxpass', 'amod'}:# and tok.nbor(2).pos == "VERB":
            foundHyphenVerb = True
            
            print("=== PREV PREV of Tok INFO: MOST LIKELY THE WORD BEFORE HYPHEN ===")
            print("PREV PREV Tok: " + prevPrevTok.text)
            print("PREV PREV Tok.pos: " + prevPrevTok.pos_)
            print("PREV PREV Tok.dep: " + prevPrevTok.dep_)
            
            print("=== PREV of Tok INFO: MOST LIKELY THE HYPHEN ===")
            print("PREV Tok: " + prevTok.text)
            print("PREV Tok.pos: " + prevTok.pos_)
            print("PREV Tok.dep: " + prevTok.dep_)
            
            print("=== TOK INFO: MOST LIKELY THE VERB ===")
            print("Tok: " + tok.text)
            print("Tok.pos: " + tok.pos_)
            print("Tok.dep: " + tok.dep_)
            
            
            
            #newVerb = sent[tokNumber-2:tokNumber+1] #SPAN OBJECT OF NEW VERB
            mergedNewVerb = get_merge_hyphen_verb(sent, tokNumber-2, tokNumber+1, tok)
            
            #mergedNewVerb = newVerb.merge(newVerb.text, tok.pos_, newVerb.root.dep_)
            print("=== MERGED NEW VERB INFO ===")
            print(mergedNewVerb.text)
            print(mergedNewVerb.pos_)
            print(mergedNewVerb.dep_)
            
            #print("NNNNEWWWWW TOK")
            #print (tok1)
            #hyphenVerb = " ".join((str(prevPrevTok), str(prevTok), str(tok)))
            #hyphenVerb = unicode(" ".join((prevPrevTok, prevTok, tok))#, tok.next_element.next_element)
            #print("HYPHEN VERBBBBBBBBBBB--===============================================================")
            #print(hyphenVerb)
            
            #mainVerb.append(prevPrevTok)
            #mainVerb.append(prevTok)
            #mainVerb.append(tok)
            #print(hyphenVerb)
            
            #mainVerb.append(tok1)
            print("MERGED NEW VERB AFTER FINDING HYPHEN VERB")
            print(mergedNewVerb)
            mainVerb.append(mergedNewVerb)
            print("MAIN VERB")
            print(mainVerb)
            hyphenIfStatementEntered = True
            
        '''
                
        if tok.pos == VERB and tok.dep_ not in {'aux', 'auxpass'}: #and foundHyphenVerb is False:
            mainVerb.append(tok)
            mainVerbWithTokNumber.append((tok,tokNumber))
               
        '''
        if hyphenIfStatementEntered is True:
            tokNumber = tokNumber-2
            print("++++++++++++++++++++++++++++++ HYPHEN IF STATEMENT ENTERED IS TRUE +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        else:
            tokNumber +=1
            print("------------------------------- tokNUMBER + 1 -----------------------------------------------------------------------------------")
        '''
        
        #print("TOKNUMBER: " + str(tokNumber))
        tokNumber += 1
    
    #mainVerb = list(mainVerb)
    
    print("/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/LIST OF MAIN VERBS BEFORE CHECKING HYPHENATED VERBS/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/")
    print(mainVerb)
    tempMainVerb = mainVerb
    
    
    '''
    for verb in mainVerbWithTokNumber:
        #newVerb = sent[tokNumber-2:tokNumber+1] #SPAN OBJECT OF NEW VERB
        prevTok = verb[0].nbor(-1)
        prevPrevTok = verb[0].nbor(-2)
        
        print("LOOKING FOR VERBS WITH HYPHEN!!!!!!!!!!!")
        
        print("*****PREV PREV TOK: " + prevPrevTok.text)
        print("*****PREV TOK: " + prevTok.text)
        print("*****TOK: " + verb[0].text)
        
        
        
        if prevTok.text == '-' and tok.pos == VERB and tok.dep_ not in {'aux', 'auxpass', 'amod'}:# and tok.nbor(2).pos == "VERB":
            mergedNewVerb = get_merge_hyphen_word(sent, verb[1]-2, verb[1]+1, verb[0])
        
            #mergedNewVerb = newVerb.merge(newVerb.text, tok.pos_, newVerb.root.dep_)
            print("=== MERGED NEW VERB INFO ===")
            print(mergedNewVerb.text)
            print(mergedNewVerb.pos_)
            print(mergedNewVerb.dep_)
            
            #print("NNNNEWWWWW TOK")
            #print (tok1)
            #hyphenVerb = " ".join((str(prevPrevTok), str(prevTok), str(tok)))
            #hyphenVerb = unicode(" ".join((prevPrevTok, prevTok, tok))#, tok.next_element.next_element)
            #print("HYPHEN VERBBBBBBBBBBB--===============================================================")
            #print(hyphenVerb)
            
            #mainVerb.append(prevPrevTok)
            #mainVerb.append(prevTok)
            #mainVerb.append(tok)
            #print(hyphenVerb)
            
            #mainVerb.append(tok1)
            print("MERGED NEW VERB AFTER FINDING HYPHEN VERB")
            print(mergedNewVerb)
            if mergedNewVerb.pos_ == "VERB":
                mainVerb.append(mergedNewVerb)
        print("MAIN VERB")
        print(mainVerb)
            #hyphenIfStatementEntered = True
            #mainVerbWithTokNumber.replace(verb[0], mergedNewVerb)
    '''
    #mainVerb = tuple(mainVerb)
    '''
    for matchVerb in mainVerbWithTokNumber[0]:
        
        matchVerbList = list(mainVerbWithTokNumber[0])
        mainVerb = list(mainVerb)
        i = 0
        if mainVerb[i] != matchVerbList[i]:
            mainVerb[i] = matchVerb
            print("-*/-*/-*/-*/-*/-*/-*/-*/-*/-*/-*/-*/-*/-*/-*/-*/-*/-*/ HYPHEN VERB REPLACEDDDDDDDDDDDDDDDDDDDDD -*/-*/-*/-*/-*/-*/-*/-*/-*/-*/-*/-*/-*/-*/-*/")
            
        i+=1
        '''
    '''
        for matchVerb1 in mainVerb:
            
            if matchVerb[i] != matchVerb1[i]:
                
                mainVerb[i] = 
                
                print("-*/-*/-*/-*/-*/-*/-*/-*/-*/-*/-*/-*/-*/-*/-*/-*/-*/-*/ HYPHEN VERB REPLACEDDDDDDDDDDDDDDDDDDDDD -*/-*/-*/-*/-*/-*/-*/-*/-*/-*/-*/-*/-*/-*/-*/")
            i+=1
        
        mainVerb = tuple(mainVerb)
        '''
    return mainVerb

def get_subjects_of_verb(verb):
    """Return all subjects of a verb according to the dependency parse."""
    subjs = [tok for tok in verb.lefts
             if tok.dep_ in SUBJ_DEPS]
    '''
    for tok in verb.lefts:
        if tok.dep_ in SUBJ_DEPS:
            subjs =  textacy.extract_jree.noun_chunks(tok)
    '''
    # get additional conjunct subjects
    subjs.extend(tok for subj in subjs for tok in _get_conjuncts(subj))
    return subjs


def get_objects_of_verb(verb):
    """
    Return all objects of a verb according to the dependency parse,
    including open clausal complements.
    """
    
    objs = [tok for tok in verb.rights
            if tok.dep_ in OBJ_DEPS]
    # get open clausal complements (xcomp)
    objs.extend(tok for tok in verb.rights
                if tok.dep_ == 'xcomp')
    # get additional conjunct objects
    objs.extend(tok for obj in objs for tok in _get_conjuncts(obj))
    return objs


def _get_conjuncts(tok):
    """
    Return conjunct dependents of the leftmost conjunct in a coordinated phrase,
    e.g. "Burton, [Dan], and [Josh] ...".
    """
    return [right for right in tok.rights
            if right.dep_ == 'conj']


def get_span_for_compound_noun(noun):
    """
    Return document indexes spanning all (adjacent) tokens
    in a compound noun.
    """
    min_i = noun.i - sum(1 for _ in takewhile(lambda x: x.dep_ == 'compound',
                                              reversed(list(noun.lefts))))
    return (min_i, noun.i)


def get_span_for_verb_auxiliaries(verb):
    """
    Return document indexes spanning all (adjacent) tokens
    around a verb that are auxiliary verbs or negations.
    """
    min_i = verb.i - sum(1 for _ in takewhile(lambda x: x.dep_ in AUX_DEPS,
                                              reversed(list(verb.lefts))))
    max_i = verb.i + sum(1 for _ in takewhile(lambda x: x.dep_ in AUX_DEPS,
                                              verb.rights))
    return (min_i, max_i)
