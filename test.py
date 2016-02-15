import unittest
import sys
from StringIO import StringIO

from app import FizzBuzz

class TestSuite(unittest.TestCase):

    def test_one(self):
        app = FizzBuzz()
        
        self.failIf(app.calc(33) != "Fizz")
        self.failIf(app.calc(66) != "Fizz")
        self.failIf(app.calc(50) != "Buzz")
        self.failIf(app.calc(15) != "FizzBuzz")
        self.failIf(app.calc(14) == "FizzBuzz")
        self.failIf(app.calc(15) == "Buzz")
        self.failIf(app.calc(33) == "Buzz")
        self.failIf(app.calc(1) == 1)

    def test_run(self):
        output = StringIO()

        app = FizzBuzz()
        app.run(100, output)
        self.failIf(len(output.getvalue().splitlines()) != 100)

    def test_primes(self):
        app = FizzBuzz()
        for p in (2,3,5,7,11):
            self.failIf('is a prime' not in app.calc(p))
def main():
    unittest.main()

if __name__ == "__main__":
    main()
