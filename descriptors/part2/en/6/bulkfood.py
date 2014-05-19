from entity import BusinessEntity, Quantity

class LineItem(BusinessEntity):

    weight = Quantity()
    price = Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price
