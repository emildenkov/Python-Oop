from unittest import TestCase, main
from project.mammal import Mammal


class TestMammal(TestCase):

    def setUp(self):
        self.mammal = Mammal("Test", "Type", "Sound")

    def test_correct_init(self):
        self.assertEqual("Test", self.mammal.name)
        self.assertEqual("Type", self.mammal.type)
        self.assertEqual("Sound", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_make_sound_returns_right_string(self):
        result = f"{self.mammal.name} makes {self.mammal.sound}"

        self.assertEqual(result, self.mammal.make_sound())

    def test_get_kingdom_returns_private_attribute(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_info_returns_the_right_string(self):
        result = f"{self.mammal.name} is of type {self.mammal.type}"

        self.assertEqual(result, self.mammal.info())


if __name__ == "__main__":
    main()
