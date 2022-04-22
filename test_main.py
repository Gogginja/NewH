import unittest
import main
import coin
import platform
import player

class TestMain(unittest.TestCase):
    #Tests pass depending on which screen you exit on
    
    #Tests to see if the game is paused
    def test_pause(self):
        self.assertEquals(main.paused, True)
    #Tests to see if the game is in the Main Menu
    def test_mainMenu(self):
        self.assertEquals(main.currentScreen, 'mainMenu')
    #Tests to see if the game is in the level select
    def test_select(self):
        self.assertEquals(main.currentScreen, 'level_select')
    #Tests to see if the game is in the settings menu
    def test_settings(self):
        self.assertEquals(main.currentScreen, 'settings')
    #Tests to see if the game is in the audio settings
    def test_audio(self):
        self.assertEquals(main.currentScreen, 'settings_audio')
    #Tests to see if the game is in the gameplay
    def test_gameplay(self):
        self.assertEquals(main.currentScreen, 'settings_gameplay')
    #Tests to see if the game is in the video settings
    def test_video(self):
        self.assertEquals(main.currentScreen, 'settings_video')
    #Tests to see if the game is in Level 1
    def test_level1Active(self):
        self.assertEquals(main.currentScreen, 'level_1')
    #Tests to see if the game is in Level 2
    def test_level2Active(self):
        self.assertEquals(main.currentScreen, 'level_2')
    #Tests to see if the game is in Level 3
    def test_level3Active(self):
        self.assertEquals(main.currentScreen, 'level_3')

if __name__ == '__main__':
    unittest.main()