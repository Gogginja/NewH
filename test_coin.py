import imp
import unittest
import coin
import player

class TestCoin(unittest.TestCase):
    #test if we can collect stars
    def test_collectOne(self):
        self.assertEquals(coin.collect(600,150,coin.coin1), 1)
    #Test to see if the player has entered a goal then they have won
    def test_goalWin(self):
        self.assertEquals(coin.end(350,0,coin.goal1), True)


if __name__ == '__main__':
    unittest.main()