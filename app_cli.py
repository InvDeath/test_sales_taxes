import sys
import settings
from sales import Item, Cart


class ParseError(Exception): pass


def suggest_type(title):
    for item_type, keywords in settings.ASSUMPTION_TYPES.items():
        for kword in keywords:
            if kword in title:
                return item_type
    return 'general'


def render_output(cart):
    result = []
    for item in cart.items:
        result.append('1 {}: {:.2f}'.format(item.title, item.get_price_with_taxes()))
    result.append('Sales Taxes: {:.2f}'.format(cart.get_total_taxes()))
    result.append('Total: {:.2f}'.format(cart.get_total_price()))
    return '\n'.join(result)


def create_item_from_string(raw_input):
    try:
        count = int(raw_input.split(' ')[0])
        title = raw_input[raw_input.find(' ') + 1: raw_input.find(' at ')]
        price = float(raw_input[raw_input.find(' at ') + 4:])
        imported = True if 'imported' in title else False
        item_type = suggest_type(title)
    except:
        raise ParseError

    items = []
    for i in range(count):
        items.append(Item(title=title, price=price, item_type=item_type, imported=imported))
    return items


def main():
    cart = Cart()
    print('Add some items:')
    for line in sys.stdin:
        if line.isspace(): break
        try:
            for item in create_item_from_string(line):
                cart.add_item(item)
        except ParseError:
            print('Wrong line format')
    if cart.count():
        print(render_output(cart))
    else:
        print('Cart is empty')


if __name__ == '__main__':
    main()
