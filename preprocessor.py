


def preprocess(text):
    
    text = text.replace(" the ", " ")
    text = text.replace(" The ", " ")
    text = text.replace(" a ", " ")
    text = text.replace(" A ", " ")
    text = text.replace(" this ", " ")
    text = text.replace(" This ", " ")
    text = text.replace(" Thus ", " ")
    text = text.replace(" thus ", " ")
    
    return text