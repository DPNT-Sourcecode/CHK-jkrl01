"""Checkout

SKU Specification:
    - Single Capital Letter
    - Multiple quantities expressed as repetitions
    - 'Basket' of SKUs is a single string of SKU characters
"""

import collections

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    """Takes a string of SKUs, which are single capital letter characters.

    examples
    --------
    checkout('AAAA') --> 180
    checkout('AAAB') --> 160
    """
    sku_price_map = {
            'A': 50,
            'B': 30,
            'C': 20,
            'D': 15,
            }

    # exact data inputs are ambiguous
    # assume only one multibuy available for each SKU
    sku_multibuy_map = {
            'A': (3, 130),
            'B': (2, 45),
            }

    total_price = 0

    sku_list = list(skus)
    sku_counts = collections.Counter(sku_list)

    for sku, quantity in sku_counts.items():
        # return early is invalid sku found
        if not sku in sku_price_map:
            return -1

        total_price += checkout_compute_multibuy(
                sku, quantity, sku_price_map, sku_multibuy_map)

    return total_price

def checkout_compute_multibuy(sku: str, quantity: int, sku_price_map: dict, sku_multibuy_map: dict) -> int:
    """Computes multibuy price when sku begins a number

    Provides the best price for the quantity.

    Example:
    --------
    given A costs 50, and 3A multibuy is 130.
    AAAA -> AAA + A -> 130 + 50 = 180
    """
    price = sku_price_map[sku]
    if sku in sku_multibuy_map:
        multibuy_size, discounted_price = sku_multibuy_map[sku]
        number_of_multibuys = quantity // multibuy_size
        total_multi_buy_price = (number_of_multibuys * discounted_price)
        remainder = quantity % multibuy_size
    else:
        remainder = quantity
        total_multi_buy_price = 0

    total_singleton_price = price * remainder

    return total_singleton_price + total_multi_buy_price 
