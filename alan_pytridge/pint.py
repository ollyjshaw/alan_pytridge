class Alan:
    @staticmethod
    def partridge_words():
        return ["Dan", "Lynn"]

    def getPhrase(self, words):
        wordsFound = [words.count(i) for i in Alan.partridge_words()]
        exx = [ "!"*words.count(i) for i in Alan.partridge_words()]
        print(wordsFound)
        if sum(wordsFound) != 0:
            exclaim = "!" * sum(wordsFound)
            return "Mine's a Pint" + exclaim
        else:
            return "Lynn, I've pierced my foot on a spike!!"
