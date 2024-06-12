from unittest import TestCase, main
from project.hero import Hero


class TestHero(TestCase):

    def setUp(self):
        self.hero = Hero("Hero", 1, 100, 100)
        self.enemy = Hero("Enemy", 1, 50, 50)

    def test_correct_init(self):
        self.assertEqual("Hero", self.hero.username)
        self.assertEqual(1, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(100, self.hero.damage)

    def test_battle_when_battling_with_myself_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_when_health_is_lower_or_equal_to_0_raises_value_error(self):
        self.hero.health = 0
        expected_str = "Your health is lower than or equal to 0. You need to rest"

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual(expected_str, str(ve.exception))

    def test_battle_when_enemy_health_is_lower_or_equal_to_0_raises_value_error(self):
        self.enemy.health = 0
        expected_str = f"You cannot fight {self.enemy.username}. He needs to rest"

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual(expected_str, str(ve.exception))

    def test_battle_when_hero_and_enemy_have_0_health_returns_draw(self):
        self.hero.health = 50

        result = self.hero.battle(self.enemy)

        self.assertEqual("Draw", result)

        self.assertEqual(0, self.hero.health)
        self.assertEqual(-50, self.enemy.health)

    def test_battle_when_hero_wins_expected_raise_in_level_health_and_damage(self):
        expected_level = self.hero.level + 1
        expected_health = self.hero.health - self.enemy.damage + 5
        expected_damage = self.hero.damage + 5

        result = self.hero.battle(self.enemy)

        self.assertEqual("You win", result)
        self.assertEqual(expected_level, self.hero.level)
        self.assertEqual(expected_health, self.hero.health)
        self.assertEqual(expected_damage, self.hero.damage)

    def test_battle_when_hero_lose_expected_increase_in_enemy_health_level_damage(self):
        self.hero, self.enemy = self.enemy, self.hero
        expected_level = self.enemy.level + 1
        expected_health = self.enemy.health - self.hero.damage + 5
        expected_damage = self.enemy.damage + 5

        result = self.hero.battle(self.enemy)
        self.assertEqual("You lose", result)
        self.assertEqual(expected_level, self.enemy.level)
        self.assertEqual(expected_damage, self.enemy.damage)
        self.assertEqual(expected_health, self.enemy.health)

    def test_correct__str__returns_proper_str(self):
        result = f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
               f"Health: {self.hero.health}\n" \
               f"Damage: {self.hero.damage}\n"

        self.assertEqual(result, str(self.hero))


if __name__ == "__main__":
    main()
