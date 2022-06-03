import re

def get_word_count(content: str):
    """
    Takes a text string as input and returns a dictionary where keys are unique words in lowercase and values are 
    the number of occurences in the text
    
    e.g 
    >> get_word_count("Hello World")
    {'hello': 1, 'world': 1}
    """
    raise NotImplementedError

def get_top_word(content: str):
    """
    Takes a text string as input and returns the words that occurs the most in a list.
    
    e.g 
    >> get_top_word("Hello hello the World world")
    ["hello", "world"]
    """
    raise NotImplementedError

def generate_text_report(content: str):
    """
    Takes a text string as input and returns a report in the following format.
    "There are <X> unique words and the top occuring words is/are <word1>, <word2>"
    
    e.g 
    >> generate_text_report("Hello and hello to the world")
    "There are 5 unique words and the top occuring words is/are 'hello'"
    """
    raise NotImplementedError
