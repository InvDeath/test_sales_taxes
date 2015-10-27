import settings


class Item(object):
    def __init__(self, title, price, item_type, imported):
        self.title = title
        self.imported = imported
        self.item_type = item_type
        self.price = price

    def get_price_with_taxes(self):
        return round(self.price + self.get_tax(), 2)

    def get_tax(self):
        tax = 0
        if self._is_taxable():
            tax += self.price * settings.TAX, 2
        if self.imported:
            tax += self.price * settings.IMPORT_TAX, 2
        return tax

    def _is_taxable(self):
        if self.item_type in settings.EXEMPTIONS:
            return False
        return True


class Cart(object):
    def __init__(self, items=None):
        self.items = items if items else []

    def get_total_taxes(self):
        pass

    def get_total_price(self):
        pass

    def __str__(self):
        pass
