

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
            total_price += int(sku[0]) * sku_price_map[sku[1]]
            continue
        return -1 # sku not present in any maps

    return total_price


