""" SIMPLE INVOICE EXERCISE """

class Product():
    """ Class PRODUCT """
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

class Invoice():
    """ Class INVOICE """
    def __init__(self):
        self.items = []
        self.lines = 0

    def add_product(self, product: Product):
        """ Function for Adding Products to the invoice 

        Args:
            product (Product): Object from class Product
        """
        self.items.append([self.lines, product])
        self.lines += 1

    def calculate_tax(self):
        """ Function returning the calculated value of the invoice (adding taxes)

        Returns:
            Float: The total amount of the invoice once applied taxes
        """
        total = 0
        for product in self.items:
            total += product[1].price
        return total * 1.21

new_invoice = Invoice()
new_invoice.add_product(Product("Keyboard", 19.90))
new_invoice.add_product(Product("Mouse", 12.45))
new_invoice.add_product(Product("Intel CPU", 105.25))

for item in new_invoice.items:
    print(f"{item[0]}) {item[1].name}, {item[1].price}€")

print(f"Total Invoice: {new_invoice.calculate_tax():.2f}€")
