#!/usr/bin/env python
# -*- coding: utf-8 -*-

def fib(n):
    """Fibonacci example function

    Args:
      n (int): integer

    Returns:
      int: n-th Fibonacci number
    """
    assert n > 0
    a, b = 1, 1
    for i in range(n-1):
        a, b = b, a+b
    return a

class Alan:

    @staticmethod
    def pwords():
        return ["Dan", "Lynn"]

    
    def getPhrase(self, words):
        wordsFound = [ words.count(i) for i in Alan.pwords()]
        exx = [ "!"*words.count(i) for i in Alan.pwords()]
        print(wordsFound)
        if wordsFound:
            exclaim = "!" * sum(wordsFound)
            return "Mine's a Pint" + exclaim
        else:
            return "Lynn, I've pierced my foot on a spike!!"
            