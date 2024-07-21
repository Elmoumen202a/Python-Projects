class Item:
    def __init__(self, name, price):
        """
        Initialize an item with a name and a price.
        
        :param name: The name of the item
        :param price: The price of the item
        """
        self.name = name
        self.price = price

class Cart:
    def __init__(self):
        """
        Initialize an empty shopping cart.
        """
        self.items = []

    def add_item(self, item):
        """
        Add an item to the shopping cart.
        
        :param item: The item to add
        """
        self.items.append(item)

    def total_price(self):
        """
        Calculate the total price of all items in the cart.
        
        :return: The total price of the items
        """
        return sum(item.price for item in self.items)

    def apply_discount(self, discount):
        """
        Apply a discount to the total price of the items in the cart.
        
        :param discount: The discount rate as a decimal (e.g., 0.10 for 10%)
        :return: The total price after the discount is applied
        """
        return self.total_price() * (1 - discount)

def main():
    """
    Main function to demonstrate the functionality of the Cart and Item classes.
    """
    cart = Cart()
    
    # Create some items
    item1 = Item("Laptop", 1000)
    item2 = Item("Smartphone", 500)

    # Add items to the cart
    cart.add_item(item1)
    cart.add_item(item2)

    # Calculate and print the total price without discount
    print(f"Total price without discount: ${cart.total_price():.2f}")

    # Apply a 10% discount and print the total price with discount
    print(f"Total price with 10% discount: ${cart.apply_discount(0.10):.2f}")

if __name__ == "__main__":
    main()
