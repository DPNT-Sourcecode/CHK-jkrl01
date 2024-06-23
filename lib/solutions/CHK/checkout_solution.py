"""Checkout

SKU Specification:
    - Single Capital Letter
    - Multiple quantities expressed as repetitions
    - 'Basket' of SKUs is a single string of SKU characters

Discount Precedence:
    - buy M get N free has precedence over multibuy deals.
    - grouped multibuy deals take precedence over multibuy deals.
    - items considered to be free will not count towards the multibuy deal.

Constraints:
    - groups in group multibuy deals shall not overall
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

    # NOTE
    # I could have organised the various discounts into classes, but this
    # approach leds to less code overall which is important when iterating on
    # the client's needs. A more class-based approach would eventually improve
    # the extensibility once the foundational commercial needs have been
    # understood.

    sku_price_map = {
            'A': 50,
            'B': 30,
            'C': 20,
            'D': 15,
            'E': 40,
            'F': 10,
            'G': 20,
            'H': 10,
            'I': 35,
            'J': 60,
            'K': 70,
            'L': 90,
            'M': 15,
            'N': 40,
            'O': 10,
            'P': 50,
            'Q': 30,
            'R': 50,
            'S': 20,
            'T': 20,
            'U': 40,
            'V': 50,
            'W': 20,
            'X': 17,
            'Y': 20,
            'Z': 21,
            }

    # exact data inputs are ambiguous
    # multibuy offers list must be in descending order of the first element of
    # the tuple
    # tuple[multibuy_size, discounted_price]
    sku_multibuy_map = {
            'A': [(5, 200), (3, 130)],
            'B': [(2, 45)],
            'H': [(10, 80), (5, 45)],
            'K': [(2, 150)],
            'P': [(5, 200)],
            'Q': [(3, 80)],
            'V': [(3, 130), (2, 90)],
            }

    sku_get_some_free_map: dict[str, tuple[int, str, int]] = {
            'E': (2, 'B', 1),
            'F': (3, 'F', 1), # buy 2Fs get another free, if you have 3Fs
            'N': (3, 'M', 1), 
            'R': (3, 'Q', 1), 
            'U': (4, 'U', 1), # ambiguous: is this deal like F? 
                              # certainly follows the same structure.
            }

    sku_group_multibuy_map: dict[str, tuple[int, int]] = {
            'STXYZ': (3, 45)
            }

    total_price = 0
    sku_list = list(skus)
    sku_counts = collections.Counter(sku_list)

    # get some free discounts takes precedence
    sku_counts = checkout_get_some_free(sku_counts, sku_get_some_free_map)

    grouped_sku_counts_price, sku_counts = checkout_compute_grouped_sku_cost(
            sku_counts, sku_group_multibuy_map, sku_price_map)
    total_price += grouped_sku_counts_price

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
    """Computes the total cost of an SKU, which includes any multibuy discounts

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
    discount possible and the remainder is returned which will be charged at
    full price.

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

def checkout_get_some_free(
    sku_counts: dict[str, int],
    sku_get_some_free_map: dict[str, tuple[int, str, int]]
    ) -> dict[str, int]:

    for sku in sku_get_some_free_map:
        quantity, free_sku, free_quantity = sku_get_some_free_map[sku]
        if not sku in sku_counts:
            continue
        if sku_counts[sku] >= quantity:
            total_free_quantity = free_quantity * (sku_counts[sku] // quantity)
            if free_sku in sku_counts:
                remaining = sku_counts[free_sku] - total_free_quantity
                sku_counts[free_sku] = remaining if remaining > 0 else 0

    return sku_counts

def checkout_compute_grouped_sku_cost(
    sku_counts: dict[str, int],
    sku_group_multibuy_map: dict[str, tuple[int, int]],
    sku_price_map: dict[str, int]
    ) -> tuple[int, dict[str,int]]:
    """Given the SKU counts and the group multi-buy discount list, return the
    remaining SKU count list and the maximum discounted price for grouped items

    Notes:
        - The order of multibuy group deal costing is arbitrary as it is
          assumed the multibuy group deals do not overlap
    """
    total_discounted_price = 0
    for group, deal in sku_group_multibuy_map.items():
        multibuy_size, discounted_price = deal
        # a sorted price list can be cached, here computed repeatedly
        group_price_list = [(s,p) for s,p in sku_price_map.items() if s in group]
        group_price_list.sort(key=lambda g: g[1], reverse=True)
        priciest_group_list = [s[0] for s in group_price_list]
        number_of_multibuys, sku_counts = count_priciest_group_multibuys(
                sku_counts, priciest_group_list, multibuy_size)
        total_discounted_price += number_of_multibuys * discounted_price


    return total_discounted_price, sku_counts

def count_priciest_group_multibuys(
    sku_counts: dict[str, int],
    priciest_group_list: list[str],
    multibuy_size: int,
    ) -> tuple[int, dict[str,int]]:
    """Picks the priciest combination from sku_count. Returns with a new
    sku_count and the number of multibuys of multibuy_size found.

    Args:
        priciest_group: SKUs of multibuy group in descending price 
        multibuy_size: number of items to qualify as 1 multibuy

    Return:
        Tuple: 
            - number of multibuys
            - revised sku_count, omits items consumed by discount
    """

    number_of_multibuys = 0
    while True:
        # temporary state track sku_count state after picking an sku item
        next_sku_counts = sku_counts.copy()
        multibuy_picked = 0
        # try picking the priciest group item multibuy_size times
        for _ in range(1, multibuy_size+1, 1):
            previous_multibuy_pick = multibuy_picked
            for sku in priciest_group_list:
                # next priciest sku item found
                if sku in next_sku_counts:
                    next_sku_counts[sku] -= 1
                    # incrementing over using n from range clarifies the
                    # intention better
                    multibuy_picked += 1
                    # ensure sku is removed from sku_count if exhausted
                    if next_sku_counts[sku] == 0:
                            del next_sku_counts[sku]
                    break # picking complete, consider next pick
            # check if anything was picked
            if previous_multibuy_pick == multibuy_picked:
                break # if not, means sku_count is exhausted from group items

        # check if enough picked to count as part of multibuy
        if multibuy_picked == multibuy_size:
            number_of_multibuys += 1
            # commit post picked sku_count state
            sku_counts = next_sku_counts
        else:
            break # multibuy_picked could not be filled to multibuy_size which
                  # means sku_count has been exhausted from this group of items
            
    return number_of_multibuys, sku_counts

