from lib.solutions.CHK import checkout_solution


class TestCheckout():
    def test_checkout__base(self):
        assert checkout_solution.checkout('A') == 50


