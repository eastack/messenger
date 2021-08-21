import unittest

import requests

from core.apis import HttpMethods


class HttpMethodTestCase(unittest.TestCase):
    def test_delete(self):
        """
        测试删除
        """
        requests.delete(HttpMethods.delete)


if __name__ == '__main__':
    unittest.main()
