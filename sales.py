class Item(object):
    def __init__(self, title, price, item_type, imported):
        self.title = title
        self.imported = imported
        self.item_type = item_type
        self.price = price

    def get_tax_amount(self):
        pass

    def _is_taxable(self):
        pass


class Cart(object):
    def __init__(self, items=None):
        self.items = items if items else []

    def get_total_taxes(self):
        pass

    def get_total_price(self):
        pass

    def __str__(self):
        pass
