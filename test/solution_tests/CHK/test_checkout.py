from lib.solutions.CHK import checkout_solution

class TestCheckout():
    def test_checkout__single_sku(self):
        assert checkout_solution.checkout('A') == 50

    def test_checkout__single_sku_multibuy_offer(self):
        assert checkout_solution.checkout('AAA') == 130

    def test_checkout__single_sku_multibuy_nooffer_1(self):
        assert checkout_solution.checkout('AA') == 100

    def test_checkout__single_sku_multibuy_nooffer_2(self):
        assert checkout_solution.checkout('CC') == 40

    def test_checkout__single_sku_multibuy_mixed(self):
        """Multi-buy offer can apply to a subset of quanitities
        AAAA -> AAA + A -> 130 + 50 = 180
        """
        assert checkout_solution.checkout('AAAA') == 180

    def test_checkout__single_sku_multibuy_1(self):
        """Multi-buy offer can apply to a subset of quanitities
        AAAAA -> 200 = 200
        """
        assert checkout_solution.checkout('AAAAA') == 200

    def test_checkout__single_sku_multibuy_2(self):
        """Multi-buy offer can apply to a subset of quanitities
        AAAAAAAAA -> AAAAA + AAA + A -> 200 + 130 + 50 = 380
        """
        assert checkout_solution.checkout('AAAAAAAAA') == 380

    def test_checkout__single_sku_multibuy_double_digit_mixed(self):
        """Multi-buy offer can apply to a subset of quanitities
        10A -> 2*AAAAA -> 400
        """
        assert checkout_solution.checkout('AAAAAAAAAA') == 400

    def test_checkout__many_sku(self):
        assert checkout_solution.checkout('AB') == 80

    def test_checkout__many_sku_multibuy_1(self):
        assert checkout_solution.checkout('AAAB') == 160

    def test_checkout__many_sku_multibuy_2(self):
        assert checkout_solution.checkout('AABA') == 160

    def test_checkout__many_sku_multibuy_3(self):
        assert checkout_solution.checkout('AAABCCD') == 215

    def test_checkout__illegal_1(self):
        assert checkout_solution.checkout('this_is_illegal') == -1

    def test_checkout__illegal_2(self):
        assert checkout_solution.checkout('AAA,5this_is_illegal') == -1

    def test_checkout__client_spec_1(self):
        assert checkout_solution.checkout('') == 0

    def test_checkout__client_spec_2(self):
        assert checkout_solution.checkout('ABCD') == 115

    def test_checkout__client_spec_3(self):
        assert checkout_solution.checkout('AA') == 100

    def test_checkout__client_spec_4(self):
        assert checkout_solution.checkout('ABCDABCD') == 215

