

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
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

    sku_list = skus.split(',') # assume comma delimiter

    return sku_price_map[skus]
