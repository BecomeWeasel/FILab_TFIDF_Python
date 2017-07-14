from spacy.en import English



nlp=English()

doc=nlp('The cat and good dog sleep in the basket near the door.')

showingmatrix=[]

for np in doc.noun_chunks:
    showingmatrix.append(np)

print(showingmatrix)