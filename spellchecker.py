import time

import multiDictionary as md

class SpellChecker:

    def __init__(self):
        self.diz = md.MultiDictionary()

    def handleSentence(self, txtIn, language):
        txt = replaceChars(txtIn)
        print("Contains")
        a = time.time()
        self.diz.searchWord(txt, language)
        b = time.time()
        print(b-a)
        print("---------")
        print("Linear")
        a = time.time()
        self.diz.searchWordLinear(txt, language)
        b = time.time()
        print(b - a)
        print("---------")
        print("Dicotomico")
        a = time.time()
        self.diz.searchWordDichotomic(txt, language)
        b = time.time()
        print(b - a)
        pass

    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\*_{}[]()>#+-.!$%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text