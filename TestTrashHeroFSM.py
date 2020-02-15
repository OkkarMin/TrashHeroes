import unittest
from TrashHeroFSM import TrashHero


class TestTrashHeroFSM(unittest.TestCase):
    def setUp(self):
        self.trash_hero = TrashHero()

    def test_left_flap_open_sequence(self):
        self.assertTrue(self.trash_hero.change_to_setup())
        self.assertTrue(self.trash_hero.change_to_ready())
        self.assertTrue(self.trash_hero.change_to_detecting_object())
        self.assertTrue(self.trash_hero.change_to_left_flap_open())

    def test_right_flap_open_sequence(self):
        self.assertTrue(self.trash_hero.change_to_setup())
        self.assertTrue(self.trash_hero.change_to_ready())
        self.assertTrue(self.trash_hero.change_to_detecting_object())
        self.assertTrue(self.trash_hero.change_to_right_flap_open())


if __name__ == "__main__":
    unittest.main()
