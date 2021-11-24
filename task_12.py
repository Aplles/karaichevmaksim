class Dessert:
    def __init__(self, name='', calories=0):
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


class JellyBean(Dessert):
    def __init__(self, name='', calories=0, flavor=''):
        Dessert.__init__(self, name, calories)
        self.flavor = flavor

    def setFlavor(self, flavor):
        self.flavor = flavor

    def getFlavor(self):
        return self.flavor

    def is_delicious(self):
        if self.flavor == 'black licorice':
            return False
        else:
            return True


des = JellyBean('Cake', 100, 'SomeBody')
print(des.is_delicious())
des.flavor = 'black licorice'
print(des.is_delicious())

