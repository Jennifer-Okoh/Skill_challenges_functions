import math

def calculate_reading_time(text):
    words = text.split()
    word_count = len(words)
    minutes = math.ceil(word_count / 200)
    return minutes