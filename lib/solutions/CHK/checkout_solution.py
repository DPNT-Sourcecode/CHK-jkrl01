

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    sku_price_map = {
            'A': 50,
            'B': 30,
            'C': 20,
            'D': 15,

            }

    sku_list = skus.split(',') # assume comma delimiter

    return sku_price_map[skus]


