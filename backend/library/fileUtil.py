from .foodItem import FoodItem
import os

def databaseToFoodList():
    file = open('./library/foodDatabase.txt', 'r')

    foods = []
    line = file.readline()
    while (line != ""):
        name, grams, cal, protein, carbs, sugar, fat, sodium = line.split(",")
        newItem = FoodItem(name, int(grams), int(cal), int(protein), int(carbs), int(sugar), int(fat), int(sodium))
        foods.append(newItem)
        line = file.readline()
    file.close()

    return foods


def foodListToDatabase(foods):
    file = open("foodDatabase.txt", "w")

    for f in foods:
        file.write('%d,%d\n' % (f.name, f.cal))

    file.close()
