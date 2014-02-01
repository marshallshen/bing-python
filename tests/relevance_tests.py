import unittest
from nose.tools import *
from bing.relevance import Relevance

def test_invalid_query():
    try:
        Relevance.validate_input("", 0.1)
        assert False
    except Exception:
        assert True

def test_invalid_precision():
    try:
        Relevance.validate_input("", 1.1)
        assert False
    except Exception:
        assert True

def test_valid_input():
    try:
        Relevance.validate_input("Groupon", 0.3)
        assert True
    except Exception:
        assert False

def test_exclude_stopwords():
    assert_equal(Relevance("test-query", 0.1).exclude_repeat_and_stop_words("it has some stopwords in the list, it also has some duplicate words"),
                "has some stopwords list, also duplicate words")