import unittest
from sales import Item, Cart
from app_cli import create_item_from_string, suggest_type


class TestItem(unittest.TestCase):
    def test_get_tax(self):
        '''
        Tests taxes for all types of goods
        '''
        # general
        item1 = Item(title='music CD', price=14.99, item_type='general', imported=False)
        self.assertEqual(item1.get_price_with_taxes(), 16.49)

        # imported, general
        item2 = Item(title='imported bottle of perfume', price=47.50, item_type='general', imported=True)
        self.assertEqual(item2.get_price_with_taxes(), 54.65)

        # books
        item3 = Item(title='book', price=12.49, item_type='books', imported=False)
        self.assertEqual(item3.get_price_with_taxes(), 12.49)

        # imported, books
        item4 = Item(title='book', price=12.49, item_type='books', imported=True)
        self.assertEqual(item4.get_price_with_taxes(), 13.14)

        # food
        item5 = Item(title='chocolate bar', price=0.85, item_type='food', imported=False)
        self.assertEqual(item5.get_price_with_taxes(), 0.85)

        # imported, food
        item6 = Item(title='box of imported chocolates', price=11.25, item_type='food', imported=True)
        self.assertEqual(item6.get_price_with_taxes(), 11.85)

        # medical
        item7 = Item(title='packet of headache pills', price=10.00, item_type='medical', imported=False)
        self.assertEqual(item7.get_price_with_taxes(), 10.00)

        # imported, medical
        item8 = Item(title='packet of imported headache pills', price=15.00, item_type='medical', imported=True)
        self.assertEqual(item8.get_price_with_taxes(), 15.75)

    def test_is_taxable(self):
        '''
        Check if item not in exemptions
        '''
        # general
        item1 = Item(title='music CD', price=14.99, item_type='general', imported=False)
        self.assertTrue(item1._is_taxable())

        # books
        item2 = Item(title='book', price=12.49, item_type='books', imported=False)
        self.assertFalse(item2._is_taxable())

        # food
        item3 = Item(title='chocolate bar', price=0.85, item_type='food', imported=False)
        self.assertFalse(item3._is_taxable())

        # medical
        item4 = Item(title='packet of headache pills', price=10.00, item_type='medical', imported=False)
        self.assertFalse(item4._is_taxable())

    def test_item_string(self):
        '''
        Format result string for item
        '''
        item1 = Item(title='music CD', price=14.99, item_type='general', imported=False)
        self.assertTrue(str(item1), 'music CD: 16.49')


class TestCart(unittest.TestCase):
    def test_total_taxes(self):
        '''
        Calculate sum of all taxes in cart
        '''
        item1 = Item(title='music CD', price=14.99, item_type='general', imported=False)
        self.assertTrue(str(item1), 'music CD: 16.49')

    def test_total_price(self):
        '''
        Sum of all prices ant taxes
        '''
        item1 = Item(title='book', price=12.49, item_type='books', imported=False)
        item2 = Item(title='music CD', price=14.99, item_type='general', imported=False)
        item3 = Item(title='chocolate bar', price=0.85, item_type='food', imported=False)

        cart = Cart(items=[item1, item2, item3])
        self.assertEqual(cart.get_total_price(), 29.83)

    def test_output(self):
        '''
        Test result output
        '''
        item1 = Item(title='book', price=12.49, item_type='books', imported=False)
        item2 = Item(title='music CD', price=14.99, item_type='general', imported=False)
        item3 = Item(title='chocolate bar', price=0.85, item_type='food', imported=False)

        cart = Cart(items=[item1, item2, item3])
        self.assertEqual(cart.get_total_taxes(), 1.50)


class TestCli(unittest.TestCase):
    def test_create_item_from_string(self):
        '''
        From stdin input create Item
        '''
        input1 = '1 book at 12.49'
        item1 = create_item_from_string(input1)[0]
        self.assertEqual(item1.title, 'book')
        self.assertEqual(item1.price, 12.49)
        self.assertEqual(item1.item_type, 'books')
        self.assertFalse(item1.imported)

        input2 = '1 imported box of chocolates at 10.50'
        item2 = create_item_from_string(input2)[0]
        self.assertTrue(item2.imported)

    def test_suggest_type(self):
        '''
        Test type suggestions
        '''
        type1 = suggest_type('book')
        self.assertEqual(type1, 'books')

        type2 = suggest_type('undef thing')
        self.assertEqual(type2, 'general')


if __name__ == '__main__':
    unittest.main()
