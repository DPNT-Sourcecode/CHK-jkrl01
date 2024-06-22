from lib.solutions.HLO import hello_solution


class TestHello():
    def test_hello__no_capitalise(self):
        """Function shall not capitalise name

        Dependent on client specification.
        """
        assert hello_solution.hello('danny') == 'Hello, danny!'

    def test_hello__zero_length(self):
        """Function shall except zero-length names

        This is needs to be confirmed/detailed in Client Specification.
        """
        assert hello_solution.hello('') == 'Hello, !'

    def test_hello__type_coercion(self):
        """This is a type error, but demenstrates type coercion should
        untype-checked code is run.
        """
        # deliberate type error
        assert hello_solution.hello(5) == 'Hello, 5!' # type: ignore

    def test_hello__fullname(self):
        assert hello_solution.hello('Danny Stewart') == 'Hello, Danny Stewart!'

    def test_hello__clientspec_1(self):
        assert hello_solution.hello("Craftsman") == 'Hello, Craftsman!'

    def test_hello__clientspec_2(self):
        assert hello_solution.hello("Mr. X") == 'Hello, Mr. X!'


