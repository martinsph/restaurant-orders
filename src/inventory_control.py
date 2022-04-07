class InventoryControl:
    INGREDIENTS = {
        'hamburguer': ['pao', 'carne', 'queijo'],
        'pizza': ['massa', 'queijo', 'molho'],
        'misto-quente': ['pao', 'queijo', 'presunto'],
        'coxinha': ['massa', 'frango'],
    }
    MINIMUM_INVENTORY = {
        'pao': 50,
        'carne': 50,
        'queijo': 100,
        'molho': 50,
        'presunto': 50,
        'massa': 50,
        'frango': 50,
    }

    def __init__(self):
        self.menu = list(self.INGREDIENTS.keys())
        self.inventory = self.MINIMUM_INVENTORY.copy()
        self.used_ingredients = self.MINIMUM_INVENTORY.copy()
        for ingredients in self.used_ingredients:
            self.used_ingredients[ingredients] = 0

    def add_new_order(self, customer, order, day):
        for item in self.INGREDIENTS[order]:
            if self.inventory[item] == 0:
                return False
            else:
                self.inventory[item] -= 1
                self.used_ingredients[item] += 1

    def get_quantities_to_buy(self):
        return self.used_ingredients
