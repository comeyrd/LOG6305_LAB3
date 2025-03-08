from poly_sbst.common.abstract_grammar import AbstractGrammar
from poly_sbst.generators.abstract_generator import AbstractGenerator
import numpy as np
import string
import random
import typing
from poly_sbst.generators.random_generator import RandomGenerator

grammar = {
"<start>": ["<protocol><domain>/<path>?<query>"],
"<protocol>":["","http://","https://"],
"<domain>": ["<before><hostname>.<ext>"],
"<path>":["<string>","<path>/<string>"],
"<query>":["<string>=<string>","<query>&<string>=<string>"],
"<hostname>":["<string>","google","facebook","uber"],
"<ext>":["com","qc.ca","org","fr","ca","io","tv","be","ch"],
"<before>":["www.",""],
"<string>":["<char>" * i for i in range(3, 11)],
"<char>": list(string.ascii_letters)+list(string.digits)
}


class UrlTestSuiteGenerator(AbstractGenerator):
    """
    A class that generates test suites using a random generator.

    Attributes:
        _name (str): The name of the generator.
        test_gen (RandomGenerator): The random generator used to generate individual tests.
        max_length (int): The maximum length of the test suite.
        min_length (int): The minimum length of the test suite.
    """

    def __init__(self) -> None:
        super().__init__()
        self._name = "UrlGenerator"
        self.gram = AbstractGrammar(grammar)
        self.min_length = 20
        self.max_length = 40

    @property
    def name(self) -> int:
        return self._name

    def cmp_func(self, x: np.ndarray, y: np.ndarray) -> float:
        """
        Compare two test cases and return a similarity score.

        Args:
            x (np.ndarray): The first test case.
            y (np.ndarray): The second test case.

        Returns:
            float: The similarity score between the two test cases.
        """
        return 0.0

    def generate_random_test(self) -> str:
        """
        Generate a random test suite.

        Returns:
            str: The generated test suite.
        """
        n = random.randint(self.min_length, self.max_length)
        test_suite = []
        for i in range(n):
            test_suite.append(self.gram.generate_input())

        return np.array(test_suite)
