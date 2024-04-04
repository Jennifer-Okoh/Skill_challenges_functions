
from lib.verify_grammar import *

# test case 1: valid text
def test_verify_grammar():
    valid_text = "This is a valid text."
    assert verify_grammar(valid_text) == True

# test case 2: text starting with lower case
    lowercase_start = "this is not a valid text."
    assert verify_grammar(lowercase_start) == False

# test case 3: text ending with a comma
    ending_comma = " this is not a valid text,"
    assert verify_grammar(ending_comma) == False

# test case 4: text with only one character
    one_character = "H"
    assert verify_grammar(one_character) == False

# test case 5: Empty text
    empty_text = ""
    assert verify_grammar(empty_text) == False
