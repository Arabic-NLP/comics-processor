'''
this module takes a list of frames (dicts) and return an 
equevelant dict of feallings and tags.
'''
from cleaner import cleanAll

class calculator:
    def __init__(self, statment):
        self.statment=cleanAll(statment)
        self.listOfFeallings= statement[0]["fealling"].keys()
        self.listOfTags= statement[0]["fealling"].keys()
        self.res=dict()

    def calcFeallings(self):
        for i in self.statment:
            for m in self.listOfFeallings:
                if self.res.has_key(m):
                    self.res[m]+= i["feallings"][m]
                else:
                    self.res[m]= i["feallings"][m]

    def calcTags(self):
        for i in self.statment:
            for m in self.listOfTags:
                if self.res.has_key(m):
                    self.res[m]+= i["tags"][m]
                else:
                    self.res[m]= i["tags"][m]

    def excute(self): # calcs all
        self.calcFeallings()
        self.calcTags()
        return self.res
   
    
     
    
    
 