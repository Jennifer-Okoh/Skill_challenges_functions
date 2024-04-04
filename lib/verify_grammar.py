
def verify_grammar(text):
    if text and text[0].isupper() and text[-1] in ['.', '!', '?']:
        return True
    else:
        return False