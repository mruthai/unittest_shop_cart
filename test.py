from main import  Shop, Item
import unittest

class ShoppingCartTest(unittest.TestCase):
    def test_add_product(self):
        test_cart = Shop()
        test_cart.cart.add("milk", "2", "2.00")

        self.assertEqual(len(test_cart.cart.items), 1)

        # self.assertIsInstance(test_cart.cart.items.keys, Shop)
        

    def test_goods(self):
        t_product = Item("milk", "2", "2.00")
        self.assertEqual(t_product.name, "milk")
        self.assertEqual(t_product.quantity, "2")
        self.assertEqual(t_product.price, "2.00")

    def test_deletion(self):
        test_del = Shop()
        test_del.cart.add("milk", "2", "5.00")
        test_del.cart.add("eggs", "5", "9.00")
        test_del.cart.add("popcorn", "5", "15.00")
        
        test_del.cart.delete("milk")
        

        self.assertEqual(len(test_del.cart.items), 2)


unittest.main()