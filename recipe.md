# Reading Time Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# Example

def estimate_reading_time(text):
    Parameters
    text: a string representing readable text
    Return
        a float representing a reading time


## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE
'''
Given a text of 200 words
It will return a reading time of 1
'''
estimate_reading_time("...200...")
# => 1.0

'''
Given a text of 400 words
it will return a reading time of 2
'''
estimate reading time of ("...400...")
# => 2.0

'''
Given a reading time of 300 words
it will return a reading time of 1.5
'''
estimate_reading_time("...300...")
=# > 1.5


'''
Given an empty text
It will raise an error
'''

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour


```

Ensure all test function names are unique, otherwise pytest will ignore them!
