import dictionary as d
import richWord as rw

class MultiDictionary:

    def __init__(self):
        self.parole = []
        self.diz = {"italian": d.Dictionary(), "english": d.Dictionary(), "spanish": d.Dictionary()}
        self.diz["italian"].loadDictionary("./resources/Italian.txt")
        self.diz["english"].loadDictionary("./resources/English.txt")
        self.diz["spanish"].loadDictionary("./resources/Spanish.txt")

    def printDic(self, language):
        for i in self.diz.keys():
            if i == language:
                self.diz[i].printAll()

    def searchWord(self, words, language):
        for word in words.split(" "):
            if self.diz[language].dict.__contains__(word):
                word = rw.RichWord(word)
                if word.corretta is None:
                    word.corretta = True
                    self.parole.append(word)
            else:
                word = rw.RichWord(word)
                if word.corretta is None:
                    word.corretta = False
                    self.parole.append(word)
                    print(word)

    def searchWordLinear(self, words, language):
        for word in words.split(" "):
            if word in self.diz[language].dict:
                word = rw.RichWord(word)
                if word.corretta is None:
                    word.corretta = True
                    self.parole.append(word)
            else:
                word = rw.RichWord(word)
                if word.corretta is None:
                    word.corretta = False
                    self.parole.append(word)
                    print(word)

    def searchWordDichotomic(self, words, language):
        parts = words.split(" ")
        meta = self.diz[language][int(len(self.diz[language])/2)]
        pass




