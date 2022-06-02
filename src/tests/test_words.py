import pytest
from src.words import get_word_count

@pytest.fixture
def multiline_text_1():
    return """For although a man is judged by his actions, by what he has said and done, 
            a man judges himself by what he is willing to do, by what he might have said, or might have done 
            – a judgment that is necessarily hampered, bot only by the scope and limits of his imagination, but 
            by the ever-changing measure of his doubt and self-esteem."""


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
            'a': 3, 'actions': 1, 'although': 1, 'and': 3, 'bot': 1, 'but': 1, 'by': 6, 'do': 1, 'done': 2, 'doubt': 1, 'ever': 1, 'changing': 1, 'for': 1, 'hampered': 1, 'has': 1, 'have': 2, 'he': 3, 'himself': 1, 'his': 3, 'imagination': 1, 'is': 3, 'judged': 1, 'judges': 1, 'judgment': 1, 'limits': 1, 'man': 2, 'measure': 1, 'might': 2, 'necessarily': 1, 'of': 2, 'only': 1, 'or': 1, 'said': 2, 'scope': 1, 'self': 1, 'esteem': 1, 'that': 1, 'the': 2, 'to': 1, 'what': 3, 'willing': 1,
        }
        assert get_word_count(multiline_text_1) == expected
