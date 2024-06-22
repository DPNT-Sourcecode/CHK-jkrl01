from lib.solutions.HLO import hello_solution


class TestHello():
    def test_hello(self):
        assert hello_solution.hello('danny') == 'Hello, danny!'

    def test_hello__zero_length(self):
        assert hello_solution.hello('') == 'Hello, !'

    def test_hello__type_coercion(self):
        assert hello_solution.hello(5) == 'Hello, 5!'

    def test_hello__fullname(self):
        assert hello_solution.hello('Danny Stewart') == 'Hello, Danny Stewart!'

    def test_hello__clientspec_1(self):
        assert hello_solution.hello("Craftsman") == 'Hello, Craftsman!'

    def test_hello__clientspec_2(self):
        assert hello_solution.hello("Mr. X") == 'Hello, Mr. X!'





