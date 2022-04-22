import unittest
import player


class TestPlayer(unittest.TestCase):
    #test if player can lose
    def test_lose(self):
        self.assertEquals(player.getState(), 'lose')
    #test if player can win
    def test_win(self):
        self.assertEquals(player.getState(), 'win')
        
    