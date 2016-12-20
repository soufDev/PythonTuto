from _operator import attrgetter


class InventoryLine:
    """Class that represent an Inventory Line of sales"""

    def __init__(self, product, price, quantity):
        """Constructor of the Inventory"""
        self.product = product
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        """print our attribute nicely"""
        return "<Inventory Line {} ({}/{})>".format(self.product, self.price, self.quantity)

inventory = [
    InventoryLine("pomme rouge", 1.2, 19),
    InventoryLine("orange", 1.4, 24),
    InventoryLine("banane", 0.9, 21),
    InventoryLine("poire", 1.2, 24),
]

inventory.sort(key=attrgetter("quantity"), reverse=True)
print(sorted(inventory, key=attrgetter("price")))