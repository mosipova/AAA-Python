class Pizza:
    """ Basic Pizza class with dough and tomato souse"""
    pizza_name = 'Основа для пиццы'
    dough = '300'
    tomato_souse = '50'

    def __init__(self, dough=dough, tomato_souse=tomato_souse):
        self.dough = dough
        self.tomato_souse = tomato_souse

    def dict(self):
        """ Returns dict with ingredients"""
        return self.__dict__

    def __str__(self):
        """ Returns recipe of pizza on class init"""
        ingridients = self.__dict__
        recipe = []
        for i in ingridients.items():
            recipe.append(' '.join(i) + 'г')
        return str(self.pizza_name + ': ' + ', '.join(recipe))


class Margarita(Pizza):
    """ Pizza Margarita with cheese and tomatoes"""
    pizza_name = 'Маргарита'
    cheese = '150'
    tomatoes = '100'

    def __init__(self, cheese=cheese, tomatoes=tomatoes, **kwargs):
        super().__init__()
        self.__dict__.update(**kwargs)
        self.cheese = cheese
        self.tomatoes = tomatoes

class Diablo(Pizza):
    """ Pizza Diablo with chili and pepperoni"""
    pizza_name = 'Дьябло'
    chili_pepper = '30'
    pepperoni = '100'

    def __init__(self, chili_pepper=chili_pepper, pepperoni=pepperoni, **kwargs):
        super().__init__()
        self.__dict__.update(**kwargs)
        self.chili_pepper = chili_pepper
        self.pepperoni = pepperoni


class Pepperoni(Pizza):
    """ Pizza Pepperoni with cheese and pepperoni"""
    pizza_name = 'Пепперони'
    cheese = '150'
    pepperoni = '100'

    def __init__(self, cheese=cheese, pepperoni=pepperoni, **kwargs):
        super().__init__()
        self.__dict__.update(**kwargs)
        self.cheese = cheese
        self.pepperoni = pepperoni
