from lib.solutions.HLO import hello_solution


class TestHello():
    def test_hello(self):
        assert hello_solution.hello('danny') == 'Hello, World!'

    def test_hello__zero_length(self):
        assert hello_solution.hello('') == 'Hello, World!'

    def test_hello__fullname(self):
        assert hello_solution.hello('Danny Stewart') == 'Hello, World!'



