import unittest

from core.apis import HttpMethods
from core.requests import Requests


class HttpMethodTestCase(unittest.TestCase, Requests):
    def test_delete(self):
        """
        delete test
        """
        self.delete(HttpMethods.delete)

    def test_post(self):
        """
        post test
        """
        self.delete(HttpMethods.delete)

if __name__ == '__main__':
    unittest.main()
