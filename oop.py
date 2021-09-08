class item:
    rate = 19.0

    def __init__(self, name: str, price=0, quantity=1):
        # validate price and quantity
        assert price >= 0, "Price must be >= 0"
        assert quantity >= 0, "Quantity must be >= 0"
        assert isinstance(name, str), "Name must be a string"
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return float(self.price) * float(self.quantity)


item1 = item("apple", 10)
item1.quantity = 3
print(item.__dict__)
