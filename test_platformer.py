import unittest
import platformer


class TestPlatformer(unittest.TestCase):
    #testing right and left movement
    def test_movement(self):
        self.assertGreater(platformer.getX(), 0)
    #test that player can jump up
    def test_jump(self):
        self.assertLess(platformer.getY(),420) 
    #test player can collect all set coins
    def test_coin(self):
        self.assertEquals(platformer.getScore(), 2)
    #test if player can lose
    def test_lose(self):
        self.assertEquals(platformer.getState(), 'lose')
    #test if player can win
    def test_win(self):
        self.assertEquals(platformer.getState(), 'win')
    #test if player is playing
    def test_playing(self):
        self.assertEquals(platformer.getState(), 'playing')
           

if __name__ == '__main__':
    unittest.main()