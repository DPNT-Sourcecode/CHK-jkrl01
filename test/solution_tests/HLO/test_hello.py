from lib.solutions.HLO import hello_solution


class TestHello():
    def test_hello(self):
        assert hello_solution.hello('danny') == 'Hello, World!'

    def test_hello__zero_length(self):
        assert hello_solution.hello('') == 'Hello, World!'

    def test_hello__fullname(self):
        assert hello_solution.hello('Danny Stewart') == 'Hello, World!'

    def test_hello__clientspec_1(self):
        assert hello_solution.hello("Craftsman") == 'Hello, World!'

    def test_hello__clientspec_2(self):
        assert hello_solution.hello("Mr. X") == 'Hello, World!'




