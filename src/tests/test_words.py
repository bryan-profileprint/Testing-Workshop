"""
# text 1 
For although a man is judged by his actions, by what he has said and done, 
a man judges himself by what he is willing to do, by what he might have said, or might have done 
– a judgment that is necessarily hampered, bot only by the scope and limits of his imagination, but 
by the ever-changing measure of his doubt and self esteem.

# text 2
Sam lay back, and stared with open mouth, and for a moment, between bewilderment and great joy,
he could not answer. At last he gasped: “Gandalf! I thought you were dead! But then I thought I was dead myself. 
Is everything sad going to come untrue? What’s happened to the world?
"""
import pytest
from src.words import get_word_count

@pytest.fixture
def multiline_text_1():
    return """For although a man is judged by his actions, by what he has said and done, 
            a man judges himself by what he is willing to do, by what he might have said, or might have done 
            – a judgment that is necessarily hampered, bot only by the scope and limits of his imagination, but 
            by the ever-changing measure of his doubt and self esteem."""

@pytest.fixture
def multiline_text_2():
    return """Sam lay back, and stared with open mouth, and for a moment, between bewilderment and great joy,
            he could not answer. At last he gasped: “Gandalf! I thought you were dead! But then I thought I was dead myself. 
            Is everything sad going to come untrue? What’s happened to the world?”"""


class TestGetWordCount:
    def test_empty(self):
        input_string = ""
        assert get_word_count(input_string) == {}

    def test_one_word(self):
        input_string = "hello"
        assert get_word_count(input_string) == {'hello': 1}

    def test_simple(self):
        input_string = " hello world hello"
        assert get_word_count(input_string) == {'hello': 2, 'world': 1}

    def test_multiline_big(self):
        input_string = """For although a man is judged by his actions, by what he has said and done, a man judges himself by what he is willing to do, by what he might have said, or might have done – a judgment that is necessarily hampered, bot only by the scope and limits of his imagination, but by the ever-changing measure of his doubt and self-esteem."""
        expected = {
            'a': 3, 'actions': 1, 'although': 1, 'and': 3, 'bot': 1, 'but': 1, 'by': 6, 'do': 1, 'done': 2, 'doubt': 1, 'ever': 1, 'changing': 1, 'for': 1, 'hampered': 1, 'has': 1, 'have': 2, 'he': 3, 'himself': 1, 'his': 3, 'imagination': 1, 'is': 3, 'judged': 1, 'judges': 1, 'judgment': 1, 'limits': 1, 'man': 2, 'measure': 1, 'might': 2, 'necessarily': 1, 'of': 2, 'only': 1, 'or': 1, 'said': 2, 'scope': 1, 'self': 1, 'esteem': 1, 'that': 1, 'the': 2, 'to': 1, 'what': 3, 'willing': 1,
        }
        assert get_word_count(input_string) == expected

    def test_text_1(self, multiline_text_1):
        expected = {
            'a': 3, 'actions': 1, 'although': 1, 'and': 3, 'bot': 1, 'but': 1, 'by': 6, 'do': 1, 'done': 2, 'doubt': 1,
            'ever': 1, 'changing': 1, 'for': 1, 'hampered': 1, 'has': 1, 'have': 2, 'he': 3, 'himself': 1, 'his': 3, 'imagination': 1,
            'is': 3, 'judged': 1, 'judges': 1, 'judgment': 1, 'limits': 1, 'man': 2, 'measure': 1, 'might': 2, 'necessarily': 1, 'of': 2,
            'only': 1, 'or': 1, 'said': 2, 'scope': 1, 'self': 1, 'esteem': 1, 'that': 1, 'the': 2, 'to': 1, 'what': 3, 'willing': 1,
        }
        assert get_word_count(multiline_text_1) == expected

    def test_text_2(self, multiline_text_2):
        expected = {'a': 1, 'and': 3, 'answer': 1, 'at': 1, 'back': 1, 'between': 1, 'bewilderment': 1, 'but': 1, 'come': 1, 'could': 1, 
            'dead': 2, 'everything': 1, 'for': 1, 'gandalf': 1, 'gasped': 1, 'going': 1, 'great': 1, 'happened': 1, 'he': 2, 'i': 3, 
            'is': 1, 'joy': 1, 'last': 1, 'lay': 1, 'moment': 1, 'mouth': 1, 'myself': 1, 'not': 1, 'open': 1, 's': 1, 'sad': 1, 
            'sam': 1, 'stared': 1, 'the': 1, 'then': 1, 'thought': 2, 'to': 2, 'untrue': 1, 'was': 1, 'were': 1, 'what': 1, 
            'with': 1, 'world': 1, 'you': 1,
        }
        assert get_word_count(multiline_text_2) == expected
