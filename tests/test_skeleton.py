#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from alan_pytridge.skeleton import fib

__author__ = "Olly Shaw"
__copyright__ = "Olly Shaw"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
