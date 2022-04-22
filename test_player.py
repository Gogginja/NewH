import unittest
import player

class TestPlayer(unittest.TestCase):
    #test if player can stay idle
    def test_idle(self):
        self.assertEquals(player.getState(), 'idle')
    #test if player can run
    def test_run(self):
        self.assertEquals(player.getState(), 'run')

if __name__ == '__main__':
    unittest.main()

    