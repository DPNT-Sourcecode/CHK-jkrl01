import re

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    """Takes a string of SKUs delimited by comma (,). Multibuys are prefixed
    with a number.
    """
    sku_price_map = {
            'A': 50,
            'B': 30,
            'C': 20,
            'D': 15,
            }

    sku_multibuy_map = {
            '3A': 130,
            '2B': 45,
            }

    total_price = 0

    sku_list = skus.split(',') # assume comma delimiter

    for sku in sku_list:
        if sku in sku_price_map:
            total_price += sku_price_map[sku]
            continue
        if sku in sku_multibuy_map:
            total_price += sku_multibuy_map[sku]
            continue
        if sku[0].isnumeric() and sku[1] in sku_price_map:
            total_price += checkout_compute_multibuy(
                    sku, sku_price_map, sku_multibuy_map)
            continue
        return -1 # sku not present in any maps

    return total_price

def sku_split(sku: str) -> tuple[str, int]:
    """Takes a SKU string, returns a tuple of the SKU and quantity.

    examples
    --------
    A   -> (A, 1)
    3A  -> (A, 3)
    30A -> (A, 30)
    """

    quantity_re = re.compile(r'^\d+')
    quantity_matched = quantity_re.match(sku)
    if quantity_matched is None:
        return (sku, 1)
    

    quantity = int(quantity_matched.group())
    sku_name = sku[quantity_matched.start() + 1:]
    return (sku_name, quantity)


def checkout_compute_multibuy(sku: str, sku_price_map: dict, sku_multibuy_map: dict) -> int:
    """Computes multibuy price when sku begins a number

    Provides the best price for the quantity.

    Example:
    --------
    given A costs 50, and 3A multibuy is 130.
    4A -> 3A + A -> 130 + 50 = 180
    """
    return int(sku[0]) * sku_price_map[sku[1]]

