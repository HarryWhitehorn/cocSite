#cocSite - data
import random, string, requests

class Clan:
    def __init__(self,name,score,rank,badge=None):
        self.rank = rank
        self.name = name
        self.score = score
        self.badge = badge

    def __str__(self):
        return str("Clan object: '{}'".format(self.name))

class ClanGen:
    @staticmethod
    def nameGen(length=5):
        return ''.join(random.choices(string.ascii_lowercase, k=length)).title()

    @staticmethod
    def generateRandom(n=10):
        return [Clan(ClanGen.nameGen(),n*50-i*50,i) for i in range(1,n+1)]

    @staticmethod
    def badgeGen(tag=None):
        return "https://api-assets.clashofclans.com/badges/70/kvDxsbdNFcy7qSGz2J_pLKC3qWURmjWr0HuN3INY1Lg.png"

if __name__ == "__main__":
    data = ClanGen.generateRandom()
    print(data)