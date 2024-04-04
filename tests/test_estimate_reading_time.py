from lib.estimate_reading_time import *
def test_calculate_reading_time():
    # test case 1: short text
    short_text = "This is a short text"
    assert calculate_reading_time(short_text) == 1

    #test case 2: long text
    long_text = "I am going to the beach during this summer and I'll make sure to swim"
    assert calculate_reading_time(long_text) == 1

    # test case 3: exactly 200 words
    exactly_200_words = "word " * 200
    assert calculate_reading_time(exactly_200_words) == 1

    # test case 4: morethan 200 words
    more_than_200_words = "word " * 202
    assert calculate_reading_time(more_than_200_words) == 2

    # test case 5: Empty text
    empty_text = ""
    assert calculate_reading_time(empty_text) == 0
