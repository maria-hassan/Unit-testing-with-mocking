import unittest


def sum(a, b):
    return a + b


class sumTest(unittest.TestCase):

    def setUp(self):
        print("Setup Called")
        self.a = 10
        self.b = 20

    def test_sum1(self):
        print("Test-1 called")
        result = sum(self.a, self.b)
        self.assertEqual(result, self.a + self.b)

    def test_sum2(self):
        print("Test-2 called")
        result = sum(self.b, self.a)
        self.assertEqual(result, self.b + self.a)


if __name__ == "__main__":
    unittest.main()
