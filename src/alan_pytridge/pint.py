def getPhrase(words):
    wordsFound = [words.count(i) for i in _partridge_words()]
    if sum(wordsFound) != 0:
        exclaim = "!" * sum(wordsFound)
        return "Mine's a Pint" + exclaim
    else:
        return "Lynn, I've pierced my foot on a spike!!"


def _partridge_words():
    return ["Dan", "Lynn"]
