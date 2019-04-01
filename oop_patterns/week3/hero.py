from abc import ABC


class Hero:
    def __init__(self):
        self.positive_effects = []
        self.negative_effects = []

        self.stats = {
            "HP": 128,
            "MP": 42,
            "SP": 100,

            "Strength": 15,
            "Perception": 4,
            "Endurance": 8,
            "Charisma": 2,
            "Intelligence": 3,
            "Agility": 8,
            "Luck": 1
        }

    def get_positive_effects(self):
        return self.positive_effects.copy()

    def get_negative_effects(self):
        return self.negative_effects.copy()

    def get_stats(self):
        return self.stats.copy()


class AbstractEffect(Hero, ABC):
    def __init__(self, base):
        self.base = base

    def get_stats(self):  # Возвращает итоговые хараетеристики
        # после применения эффекта
        pass

    def get_positive_effects(self):
        pass

    def get_negative_effects(self):
        pass


class AbstractPositive(AbstractEffect):
    def __init__(self, base):
        self.base = base


class Berserk(AbstractPositive):

    def __init__(self, base):
        super(base)
        self.stats.update("Strength", self.stats.get("Strength") + 7)
        self.stats.update("Endurance", self.stats.get("Endurance") + 7)
        self.stats.update("Agility", self.stats.get("Agility") + 7)
        self.stats.update("Luck", self.stats.get("Luck") + 7)
        self.stats.update("Perception", self.stats.get("Perception") - 7)
        self.stats.update("Charisma", self.stats.get("Charisma") - 7)
        self.stats.update("Intelligence", self.stats.get("Intelligence") - 7)
        self.stats.update("HP", self.stats.get("HP") + 50)

    def get_positive_effects(self):
        pass


class Blessing(AbstractPositive):


class AbstractNegative(AbstractEffect):
    def __init__(self, base):
        pass


class Weakness(AbstractNegative):
    pass

class EvilEye(AbstractNegative):
    pass

class Curse(AbstractNegative):
    pass