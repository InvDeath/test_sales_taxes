import settings


def round_up(n):
    if len(str(n)) == 4 and str(n).endswith('5'):
        return n
    if round(n, 2) - round(n, 1) <= 0:
        return round(n, 1)
    return round(n, 1) + 0.05


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
            tax += round_up(self.price * settings.TAX)
        if self.imported:
            tax += round_up(self.price * settings.IMPORT_TAX)
        return tax

    def _is_taxable(self):
        if self.item_type in settings.EXEMPTIONS:
            return False
        return True


class Cart(object):
    def __init__(self, items=None):
        self.items = items if items else []

    def add_item(self, item):
        self.items.append(item)

    def get_total_taxes(self):
        total_taxes = 0
        for item in self.items:
            total_taxes += item.get_tax()
        return total_taxes

    def get_total_price(self):
        total_price = 0
        for item in self.items:
            total_price += item.get_price_with_taxes()
        return total_price

    def __str__(self):
        pass
