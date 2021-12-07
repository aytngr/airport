class Menu:
    def __init__(self, meals):
        self.meals = meals
    def get_meal_names(self):
        names=[]
        for meal in self.meals:
            names.append(meal.name)
        return names