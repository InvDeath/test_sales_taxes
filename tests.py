import unittest


class TestItem(unittest.TestCase):
    def test_calc_tax_imported(self):
        '''
        Imported items have additional tax
        '''
        self.assertTrue(False)

    def test_calc_tax_excepted(self):
        '''
        Not all item types have tax
        '''
        self.assertTrue(False)

    def test_is_taxable(self):
        '''
        Check if item is imported
        '''
        self.assertTrue(False)


class TestCart(unittest.TestCase):
    def test_total_taxes(self):
        '''
        Calculate sum of all taxes in cart
        '''
        self.assertTrue(False)

    def test_total_price(self):
        '''
        Summ of all prices ant taxes
        '''
        self.assertTrue(False)

    def test_item_string(self):
        '''
        Format result string for item
        '''
        self.assertTrue(False)

    def test_output(self):
        '''
        Test result output
        '''
        self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
