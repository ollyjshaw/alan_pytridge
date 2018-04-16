#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from alan_pytridge.skeleton import fib
from alan_pytridge.skeleton import Alan


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)

def test_nothing_found_in_empty_list():
    words = []
    phrase = Alan().getPhrase(words)
    assert phrase == "Lynn, I've pierced my foot on a spike!!"

def test_nothing_found_in_list_with_no_partridge_words():
    words = ["foo", "bar", "baz"]
    phrase = Alan().getPhrase(words)
    assert phrase == "Lynn, I've pierced my foot on a spike!!"

def test_finds_a_single_partridge_words():
    words = ["foo", "Dan", "baz"]
    phrase = Alan().getPhrase(words)
    assert phrase == "Mine's a Pint!"


def test_finds_multiple_partridge_words():
    words = ["foo", "Dan", "Lynn", "baz"]
    phrase = Alan().getPhrase(words)
    assert phrase == "Mine's a Pint!!"

def test_finds_multiple_partridge_words2():
    words = ["Dan", "foo", "Dan", "Lynn", "baz"]
    phrase = Alan().getPhrase(words)
    assert phrase == "Mine's a Pint!!!"