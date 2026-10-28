# Baylee Coons
# Fall 2026 CIS256
# Programming Assignment 4

import pytest
from guess_the_word import words, choose_word

def test_choose_word():
    # ensures picked word is actually in the list
    selected = choose_word()
    assert selected in words

def test_words_list_not_empty():
    
    assert len(words) > 0