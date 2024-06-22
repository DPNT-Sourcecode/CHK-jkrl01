from lib.solutions.CHK import checkout_solution


class TestCheckout():
    def test_checkout__base(self):
        assert checkout_solution.checkout('A') == 50

    def test_checkout__base_multibuy(self):
        assert checkout_solution.checkout('3A') == 130

    def test_checkout__illegal_1(self):
        assert checkout_solution.checkout('this_is_illegal') == -1


