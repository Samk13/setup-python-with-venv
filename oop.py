class Item:
    rate = 19.0
    all = []

    def __init__(self, name: str, price=0, quantity=1):
        # validate price and quantity
        assert price >= 0, "Price must be >= 0"
        assert quantity >= 0, "Quantity must be >= 0"
        assert isinstance(name, str), "Name must be a string"
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f"Item({self.name}, {self.price}, {self.quantity})"

    def calculate_total_price(self):
        return float(self.price) * float(self.quantity)


item1 = Item("apple", 12)
item2 = Item("samsung", 13)
item3 = Item("Huawei", 15)

print(Item.all)
