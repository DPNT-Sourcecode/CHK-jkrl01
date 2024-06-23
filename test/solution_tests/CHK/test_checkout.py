from lib.solutions.CHK import checkout_solution


 # - {"method":"checkout","params":[""],"id":"CHK_R1_002"}, expected: 0, got: -1
 # - {"method":"checkout","params":["ABCD"],"id":"CHK_R1_011"}, expected: 115, got: -1
 # - {"method":"checkout","params":["AA"],"id":"CHK_R1_013"}, expected: 100, got: -1

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

    def test_checkout__single_sku_multibuy_double_digit_mixed(self):
        """Multi-buy offer can apply to a subset of quanitities
        10A -> 3*AAA + A -> 390 + 50 = 440
        """
        assert checkout_solution.checkout('AAAAAAAAAA') == 440

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

    # def test_sku_split__no_quantity(self):
    #     assert checkout_solution.sku_split('A') == ('A', 1)

    # def test_sku_split__single_digit_quantity(self):
    #     assert checkout_solution.sku_split('2A') == ('A', 2)

    # def test_sku_split__double_digit_quantity(self):
    #     assert checkout_solution.sku_split('10A') == ('A', 10)

    # def test_sku_split__triple_digit_quantity(self):
    #     assert checkout_solution.sku_split('100A') == ('A', 100)

    # def test_sku_split__multichar_sku(self):
    #     assert checkout_solution.sku_split('100ABDF') == ('ABDF', 100)
