import unittest
import main

class TestMain(unittest.TestCase):
    #Tests to see if the game can be paused
    def test_pause(self):
        self.assertEquals(main.getPaused(), True)
    #Tests to see if the game can be paused
    def test_mainMenu(self):
        self.assertEquals(main.getScreen(), 'mainMenu')

    def test_select(self):
        self.assertEquals(main.getScreen(), 'levelSelect')

    def test_settings(self):
        self.assertEquals(main.getScreen(), 'settings')

    def test_audio(self):
        self.assertEquals(main.getScreen(), 'settings_audio')

    def test_gameplay(self):
        self.assertEquals(main.getScreen(), 'settings_gameplay')

    def test_video(self):
        self.assertEquals(main.getScreen(), 'settings_video')

    def test_level1Active(self):
        self.assertEquals(main.getScreen(), 'level_1')
    
    def test_level2Active(self):
        self.assertEquals(main.getScreen(), 'level_2')

    def test_level3Active(self):
        self.assertEquals(main.getScreen(), 'level_3')