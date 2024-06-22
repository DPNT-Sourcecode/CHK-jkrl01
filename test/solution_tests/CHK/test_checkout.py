from lib.solutions.CHK import checkout_solution


class TestCheckout():
    def test_checkout__single_sku(self):
        assert checkout_solution.checkout('A') == 50

    def test_checkout__single_sku_multibuy_offer(self):
        assert checkout_solution.checkout('3A') == 130

    def test_checkout__single_sku_multibuy_nooffer(self):
        assert checkout_solution.checkout('2A') == 130

    def test_checkout__single_sku_multibuy_mixed(self):
        """Multi-buy offer can apply to a subset of quanitities
        4A -> 3A + A -> 130 + 50 = 180
        """
        assert checkout_solution.checkout('4A') == 180

    def test_checkout__many_sku(self):
        """Assume Delimiter is comma.

        Not defined in client specification"""
        assert checkout_solution.checkout('A,B') == 80

    def test_checkout__many_sku_multibuy(self):
        """Multibuy syntax is ambiguous. Assume <number><sku>"""
        assert checkout_solution.checkout('3A,B') == 160

    def test_checkout__illegal_1(self):
        assert checkout_solution.checkout('this_is_illegal') == -1

