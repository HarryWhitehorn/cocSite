#cocSite - data
import random, string

class Clan:
    def __init__(self,name,score,rank,icon=None):
        self.rank = rank
        self.name = name
        self.score = score
        self.icon = icon

    def __str__(self):
        return str("Clan object: '{}'".format(self.name))

class ClanGen:
    @staticmethod
    def nameGen(length=5):
        return ''.join(random.choices(string.ascii_lowercase, k=length)).title()

    @staticmethod
    def generateRandom(n=10):
        return [Clan(ClanGen.nameGen(),500-i*50,i) for i in range(1,n+1)]

if __name__ == "__main__":
    data = ClanGen.generateRandom()
    print(data)