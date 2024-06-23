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
    # multibuy offers list must be in descending order of the first element of
    # the tuple
    # tuple[multibuy_size, discounted_price]
    sku_multibuy_map = {
            'A': [(5, 200), (3, 130)],
            'B': [(2, 45)],
            }

    total_price = 0

    sku_list = list(skus)
    sku_counts = collections.Counter(sku_list)

    for sku, quantity in sku_counts.items():
        if not sku in sku_price_map:
            return -1 # return early if invalid sku found
        total_price += checkout_compute_sku_cost(
                sku, quantity, sku_price_map, sku_multibuy_map)

    return total_price

def checkout_compute_sku_cost(
    sku: str, 
    quantity: int, 
    sku_price_map: dict, 
    sku_multibuy_map: dict[str, list]
    ) -> int:
    """Computes multibuy price when sku begins a number

    Provides the best price for the quantity.

    Example:
    --------
    given A costs 50, and 3A multibuy is 130.
    AAAA -> AAA + A -> 130 + 50 = 180
    """
    price = sku_price_map[sku]
    if sku in sku_multibuy_map:
        multibuy_offers = sku_multibuy_map[sku]
        total_multi_buy_price, remainder = checkout_compute_multibuy_price(
                quantity, 
                multibuy_offers)
    else:
        remainder = quantity
        total_multi_buy_price = 0

    total_singleton_price = price * remainder

    return total_singleton_price + total_multi_buy_price 

def checkout_compute_multibuy_price(
    quantity: int, 
    multibuy_offers: list[tuple[int, int]]
    ) -> tuple[int, int]:
    """Given a quantity and the multibuy offers list, returns maximum multibuy
    price and the remainder that will be charged at full price.

    Note:
        multibuy_offers list must be sorted in descending order with the first
        key of the tuple.
    """
    remainder = quantity
    total_multi_buy_price = 0
    for multibuy_size, discounted_price in multibuy_offers:
        number_of_multibuys = remainder // multibuy_size
        total_multi_buy_price += (number_of_multibuys * discounted_price)
        remainder = remainder - (multibuy_size * number_of_multibuys)

    return total_multi_buy_price, remainder

