import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

from library.foodItem import FoodItem
from library.foodDatabase import FoodDatabase

class Fruit(BaseModel):
    name: str

class Fruits(BaseModel):
    fruits: List[Fruit]

app = FastAPI()

origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class NamesList(BaseModel):
    names: list[str]

class FoodItem(BaseModel):
    name: str
    amount: float
    cals: float = 0
    protein: float = 0
    carbs: float = 0
    sugar: float = 0
    fat: float = 0
    sodium: float = 0

database = FoodDatabase()
for f in database.foods:
    print(f)

@app.get("/foods/{foodName}/amount/{amount}")
def getFood(foodName: str, amount: float):
    food = database.findFood(foodName)
    if food is None:
        return FoodItem(name=foodName, amount=0)
    foodItem = FoodItem(
                name=foodName,
                amount=amount,
                cals=food.getCals(amount),
                protein=food.getProtein(amount),
                carbs=food.getCarbs(amount),
                sugar=food.getSugar(amount),
                fat=food.getFat(amount),
                sodium=food.getSodium(amount)
                )
    return foodItem


@app.get("/names-list")
def getNamesList():
    return NamesList(names=database.getNamesList())

"""
@app.post("/weight/{weight}/height/{height}")
def changeWeight(weight: int, height: int): #weight (kg), #height (cm)
    #set weight, height, gender
    return
"""


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)