from lib.solutions.CHK import checkout_solution


class TestCheckout():
    def test_checkout__single_sku(self):
        assert checkout_solution.checkout('A') == 50

    def test_checkout__single_sku_multibuy(self):
        assert checkout_solution.checkout('3A') == 130

    def test_checkout__many_sku(self):
        """Assume Delimiter is comma.

        Not defined in client specification"""
        assert checkout_solution.checkout('A,B') == 80

    def test_checkout__many_sku_multibuy(self):
        """Assume Delimiter is comma"""
        assert checkout_solution.checkout('3A,B') == 160

    def test_checkout__illegal_1(self):
        assert checkout_solution.checkout('this_is_illegal') == -1



