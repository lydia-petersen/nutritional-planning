class FoodItem:
    name: str
    cals: float
    protein: float
    carbs: float
    sugar: float
    fat: float
    sodium: float

    def __init__(self, name, grams, cals, protein, carbs, sugar, fat, sodium):
        self.name = name.lower()
        self.cals = 0 if cals == 0 else (grams * 100) / cals  #calculate calories per 100g
        self.protein = 0 if protein == 0 else (grams * 100) / protein
        self.carbs = 0 if carbs == 0 else (grams * 100) / carbs
        self.sugar = 0 if sugar == 0 else (grams * 100) / sugar
        self.fat = 0 if fat == 0 else (grams * 100) / fat
        self.sodium = 0 if sodium == 0 else (grams * 100) / sodium

    def getCals(self, amount):
        return round((self.cals * amount) / 100, 2)
    
    def getProtein(self, amount):
        return round((self.protein * amount) / 100, 2)
    
    def getCarbs(self, amount):
        return round((self.carbs * amount) / 100, 2)
    
    def getSugar(self, amount):
        return round((self.sugar * amount) / 100, 2)
    
    def getFat(self, amount):
        return round((self.fat * amount) / 100, 2)
    
    def getSodium(self, amount):
        return round((self.sodium * amount) / 100, 2)

    def __str__(self):
        return f"{self.name} has {self.cals} calories per 100g"