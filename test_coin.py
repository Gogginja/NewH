import unittest
import coin

class TestCoin(unittest.TestCase):
    #test if we can collect 1 coin
    def test_collectOne(self):
        self.assertEquals(coin.collect, 1)
    #test if we can collect both coins
    def test_collectBoth(self):
        self.assertEquals(coin.collect, 0)


if __name__ == '__main__':
    unittest.main()