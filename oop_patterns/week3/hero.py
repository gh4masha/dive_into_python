from abc import ABC, abstractmethod


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
        super().__init__()
        self.base = base
        self.positive_effects = self.base.positive_effects.copy()
        self.negative_effects = self.base.negative_effects.copy()

    # @abstractmethod
    def get_stats(self):  # Возвращает итоговые хараетеристики
        # после применения эффекта
        pass

    # def get_positive_effects(self):
    #     pass
    #
    # def get_negative_effects(self):
    #     pass


class AbstractPositive(AbstractEffect, ABC):
    def __init__(self, base):
        super().__init__(base)

    # def get_stats(self):  # Возвращает итоговые хараетеристики
    #     # после применения эффекта
    #     pass


class Berserk(AbstractPositive):

    def __init__(self, base):
        super().__init__(base)

    def get_positive_effects(self):
        self.positive_effects.append("Berserk")
        return self.positive_effects.copy()

    def get_stats(self):
        self.stats["Strength"] = self.base.stats.get("Strength") + 7
        self.stats["Endurance"] = self.base.stats.get("Endurance") + 7
        self.stats["Agility"] = self.base.stats.get("Agility") + 7
        self.stats["Luck"] = self.base.stats.get("Luck") + 7
        self.stats["Perception"] = self.base.stats.get("Perception") - 3
        self.stats["Charisma"] = self.base.stats.get("Charisma") - 3
        self.stats["Intelligence"] = self.base.stats.get("Intelligence") - 3
        self.stats["HP"] = self.base.stats.get("HP") + 50
        return self.stats.copy()


class Blessing(AbstractPositive):
    def __init__(self, base):
        super().__init__(base)

    def get_positive_effects(self):
        self.base.positive_effects.append("Blessing")
        return self.positive_effects.copy()

    def get_stats(self):
        self.stats["Strength"] = self.base.stats.get("Strength") + 2
        self.stats["Endurance"] = self.base.stats.get("Endurance") + 2
        self.stats["Agility"] = self.base.stats.get("Agility") + 2
        self.stats["Luck"] = self.base.stats.get("Luck") + 2
        self.stats["Perception"] = self.base.stats.get("Perception") + 2
        self.stats["Charisma"] = self.base.stats.get("Charisma") + 2
        self.stats["Intelligence"] = self.base.stats.get("Intelligence") + 2
        return self.stats.copy()


class AbstractNegative(AbstractEffect, ABC):
    def __init__(self, base):
        super().__init__(base)


class Weakness(AbstractNegative):
    def __init__(self, base):
        super().__init__(base)

    def get_negative_effects(self):
        self.negative_effects.append("Weakness")
        return self.positive_effects.copy()

    def get_stats(self):
        self.stats["Strength"] = self.base.stats.get("Strength") - 4
        self.stats["Endurance"] = self.base.stats.get("Endurance") - 4
        self.stats["Agility"] = self.base.stats.get("Agility") - 4
        return self.stats.copy()


class EvilEye(AbstractNegative):
    def __init__(self, base):
        super().__init__(base)

    def get_negative_effects(self):
        self.negative_effects.append("EvilEye")
        return self.positive_effects.copy()

    def get_stats(self):
        self.stats["Luck"] = self.base.stats.get("Luck") - 10
        return self.stats.copy()


class Curse(AbstractNegative):
    def __init__(self, base):
        super().__init__(base)

    def get_negative_effects(self):
        self.base.negative_effects.append("Curse")
        return self.positive_effects.copy()

    def get_stats(self):
        self.stats["Strength"] = self.base.stats.get("Strength") - 2
        self.stats["Endurance"] = self.base.stats.get("Endurance") - 2
        self.stats["Agility"] = self.base.stats.get("Agility") - 2
        self.stats["Luck"] = self.base.stats.get("Luck") - 2
        self.stats["Perception"] = self.base.stats.get("Perception") - 2
        self.stats["Charisma"] = self.base.stats.get("Charisma") - 2
        self.stats["Intelligence"] = self.base.stats.get("Intelligence") - 2
        return self.stats.copy()


if __name__ == '__main__':
    hero = Hero()
    hero = Hero()

    print(hero.get_stats())
    # {'HP': 128, 'MP': 42, 'SP': 100, 'Strength': 15, 'Perception': 4, 'Endurance': 8, 'Charisma': 2, 'Intelligence': 3,'Agility': 8, 'Luck': 1}

    print(hero.stats)
    # {'HP': 128, 'MP': 42, 'SP': 100, 'Strength': 15, 'Perception': 4, 'Endurance': 8, 'Charisma': 2, 'Intelligence': 3, 'Agility': 8, 'Luck': 1}

    print(hero.get_negative_effects())
    # []

    print(hero.get_positive_effects())
    # []

    # накладываем эффект
    brs1 = Berserk(hero)
    print(brs1.get_stats())
    # {'HP': 178, 'MP': 42, 'SP': 100, 'Strength': 22, 'Perception': 1, 'Endurance': 15, 'Charisma': -1, 'Intelligence': 0, 'Agility': 15, 'Luck': 8}

    print(brs1.get_negative_effects())
    # []

    print(brs1.get_positive_effects())
    # ['Berserk']

    # накладываем эффекты
    brs2 = Berserk(brs1)
    cur1 = Curse(brs2)
    print(cur1.get_stats())
    # {'HP': 228, 'MP': 42, 'SP': 100, 'Strength': 27, 'Perception': -4, 'Endurance': 20, 'Charisma': -6, 'Intelligence': -5, 'Agility': 20, 'Luck': 13}

    print(cur1.get_positive_effects())
    # ['Berserk', 'Berserk']
    # ['Berserk', 'Berserk']

    print(cur1.get_negative_effects())
    # ['Curse']
    # ['Curse']

    # снимаем эффект Berserk
    cur1.base = brs1
    print(cur1.get_stats())
    # {'HP': 178, 'MP': 42, 'SP': 100, 'Strength': 20, 'Perception': -1, 'Endurance': 13, 'Charisma': -3, 'Intelligence': -2, 'Agility': 13, 'Luck': 6}

    print(cur1.get_positive_effects())
    # ['Berserk']

    print(cur1.get_negative_effects())
    # ['Curse']
