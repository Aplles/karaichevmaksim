class Dessert:
    def __init__(self, name=0, calories=0):
        self.name = name
        self.calories = calories

    def setName(self, name):
        self.name = name

    def setCalories(self, calories):
        self.calories = calories

    def getName(self):
        return self.name

    def getCalories(self):
        return self.calories

    def is_healthy(self):
        if isinstance(self.calories, (int, float)):
            return self.calories < 200
        else:
            return False

    def is_delicious(self):
        if type(self) == Dessert:
            return True
        else:
            return False


des1 = Dessert('Cake', 100)
print(des1.is_healthy())

des1.calories = 1000
print(des1.is_healthy())

print(des1.is_delicious())
