from typing import List
from .fileUtil import *

class FoodDatabase:
    foods: List[FoodItem]
    
    def __init__(self):
        self.foods = databaseToFoodList()
    

    #NOTE: add in functionality to replace item in the name is a duplicate
    def addFood(self, item):
        index = 0
        for f in self.foods:
            if (item.name < f.name):
                break
            +(+index)

        if (index == len(self.foods)):
            self.foods.append(item)
        else:
            self.foods.insert(item, index)

    
    def removeFood(self, item):
        index = 0
        for f in self.foods:
            if (item.name == f.name):
                break
            +(+index)
        
        if (index != len(self.foods)):
            self.foods.pop(index)


    def findFood(self, name):
        for f in self.foods:
            if (f.name == name):
                return f
    

    def getNamesList(self):
        names = []
        for f in self.foods:
            names.append(f.name)
        return names      