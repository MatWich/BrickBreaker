import pprint
import pymongo
from pymongo import MongoClient


class Database:
    
    def __init__(self):
        self.cluster = MongoClient('localhost', 27017)
        self.db = self.cluster["BrickBreakerGame"]
        self.scores = self.db["scores"]

    def addScore(self, pName, score, id=0):
        toSend = {
            "pName": pName,
            "score": score
        }
    
        
        self.scores.insert_one(toSend)
        id += 1

    # checks if there is more then 10 scores in db
    def update(self):
        result = self.checkDocAmount()
        while result > 10:
            self.findAllScores()
            self.findTheLowest()
            result = self.checkDocAmount()

    def findAllScores(self):
        self.results = []
        for result in self.scores.find({}, {"score": 1, "_id": 1}):
            self.results.append(result)
    
    # this func find & delete the lowest elemtnt
    def findTheLowest(self):
        lowest = self.results[0]
        for result in self.results:
            if lowest["score"] > result["score"]:
                lowest = result

        print("the lowest element is: ", lowest["_id"], lowest["score"])
        self.scores.delete_one({"_id": lowest["_id"]})

    
    def checkDocAmount(self):
        return self.scores.count_documents({})

    def loopfor10(self):
        # counter the number that cannot be exceed
        counter = 0
        # the list that will be returned
        highScores = [] 

        # loop through sorted results
        for result in self.scores.find({}).sort([("score", 1)]).limit(10):
            counter += 1
            # if exceed break
            if counter >= 11:
                break
            
            # maybe appending to the list and return it?
            print(str(counter) + ". " ,result)
            highScores.append(result)


        # how many
        print("the amount of docs: ",self.scores.count_documents({}))
        return highScores
    
    # delete all colections
    def clear(self):
        self.scores.delete_many({})

db = Database()
#db.clear()
#db.addScore("Gary", 100)
#db.addScore("Gerul", 700)
#db.addScore("Jozek", 100)
#db.addScore("Jan", 250)
#db.addScore("Bace", 400)
#db.addScore("Jozek", 110)
#db.addScore("Gary", 140)
#db.addScore("Jozek", 300)
#db.addScore("Jozek", 900)
#db.addScore("Jozek", 320)


#db.update()
temp =  db.loopfor10()
pprint.pprint(temp)