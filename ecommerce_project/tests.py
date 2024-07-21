import unittest
from main import Item, Cart

class TestEcommerce(unittest.TestCase):

    def test_add_item(self):
        """
        Test that an item can be added to the cart.
        """
        cart = Cart()
        item = Item("Laptop", 1000)
        cart.add_item(item)
        
        # Check that the cart has exactly one item
        self.assertEqual(len(cart.items), 1)
        
        # Check that the item in the cart is the one we added
        self.assertEqual(cart.items[0].name, "Laptop")

    def test_total_price(self):
        """
        Test that the total price of items in the cart is calculated correctly.
        """
        cart = Cart()
        item1 = Item("Laptop", 1000)
        item2 = Item("Smartphone", 500)
        
        # Add items to the cart
        cart.add_item(item1)
        cart.add_item(item2)
        
        # Check that the total price is the sum of the item prices
        self.assertEqual(cart.total_price(), 1500)

    def test_apply_discount(self):
        """
        Test that a discount is applied correctly to the total price.
        """
        cart = Cart()
        item1 = Item("Laptop", 1000)
        item2 = Item("Smartphone", 500)
        
        # Add items to the cart
        cart.add_item(item1)
        cart.add_item(item2)
        
        # Check that the total price after applying a 10% discount is correct
        self.assertEqual(cart.apply_discount(0.10), 1350)

if __name__ == '__main__':
    unittest.main()
