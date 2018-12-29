class Alan:
    @staticmethod
    def pwords():
        return ["Dan", "Lynn"]

    def getPhrase(self, words):
        wordsFound = [words.count(i) for i in Alan.pwords()]
        exx = [ "!"*words.count(i) for i in Alan.pwords()]
        print(wordsFound)
        if sum(wordsFound) != 0:
            exclaim = "!" * sum(wordsFound)
            return "Mine's a Pint" + exclaim
        else:
            return "Lynn, I've pierced my foot on a spike!!"

    def somethingd():
        print("yo")
