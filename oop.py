import csv


class Item:
    rate = 19.0
    all = []

    def __init__(self, name: str, price=0, quantity=1):
        # validate price and quantity
        assert price >= 0, "Price must be >= 0"
        assert quantity >= 0, "Quantity must be >= 0"
        assert isinstance(name, str), "Name must be a string"

        # initialize instance variables
        self.name = name
        self.price = price
        self.quantity = quantity

        # append each item initiated to the list
        Item.all.append(self)

    # representation of the object
    def __repr__(self):
        return f"Item({self.name}, {self.price}, {self.quantity})"

    # normal function
    def calculate_total_price(self):
        return float(self.price) * float(self.quantity)

    # class method to read the csv file and return a list of items
    @classmethod
    def initiate_from_csv(cls, filename: str):
        with open(filename, "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(name=item["name"], price=float(item["price"]),
                 quantity=int(item["quantity"]))

    @staticmethod
    def is_integer(num):
        # count out  the floats that are point zero
        # for i.e: 5.0, 10.0
        if isinstance(num, float):
            # count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False


print(Item.is_integer(5.1))
