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
        self.stats = self.base.get_stats().copy()
        self.positive_effects = self.base.positive_effects.copy()
        self.negative_effects = self.base.negative_effects.copy()

    # def get_stats(self):  # Возвращает итоговые хараетеристики
    #     return self.stats.copy()

    def get_positive_effects(self):
        return self.base.get_positive_effects()

    def get_negative_effects(self):
        return self.base.get_negative_effects()


class AbstractPositive(AbstractEffect):
    def __init__(self, base):
        super().__init__(base)

    # def get_stats(self):  # Возвращает итоговые хараетеристики
    #     # после применения эффекта
    #     pass


class Berserk(AbstractPositive):

    def __init__(self, base):
        super().__init__(base)


    def get_positive_effects(self):
        eff = self.base.get_positive_effects()
        eff.append("Berserk")
        return eff.copy()
        # return self.positive_effects.copy()

    def get_stats(self):
        stats = self.base.get_stats()
        stats["Strength"] = stats.get("Strength") + 7
        stats["Endurance"] = stats.get("Endurance") + 7
        stats["Agility"] = stats.get("Agility") + 7
        stats["Luck"] = stats.get("Luck") + 7
        stats["Perception"] = stats.get("Perception") - 3
        stats["Charisma"] = stats.get("Charisma") - 3
        stats["Intelligence"] = stats.get("Intelligence") - 3
        stats["HP"] = stats.get("HP") + 50
        return stats.copy()


class Blessing(AbstractPositive):
    def __init__(self, base):
        super().__init__(base)

    def get_positive_effects(self):
        eff = self.base.get_positive_effects()
        eff.append("Blessing")
        return eff.copy()

    def get_stats(self):
        stats = self.base.get_stats()
        stats["Strength"] = stats.get("Strength") + 2
        stats["Endurance"] =stats.get("Endurance") + 2
        stats["Agility"] = stats.get("Agility") + 2
        stats["Luck"] = stats.get("Luck") + 2
        stats["Perception"] = stats.get("Perception") + 2
        stats["Charisma"] = stats.get("Charisma") + 2
        stats["Intelligence"] = stats.get("Intelligence") + 2
        return stats.copy()


class AbstractNegative(AbstractEffect):
    def __init__(self, base):
        super().__init__(base)


class Weakness(AbstractNegative):
    def __init__(self, base):
        super().__init__(base)

    def get_negative_effects(self):
        eff = self.base.get_negative_effects()
        eff.append("Weakness")
        return eff.copy()

    def get_stats(self):
        stats = self.base.get_stats()
        stats["Strength"] = stats.get("Strength") - 4
        stats["Endurance"] = stats.get("Endurance") - 4
        stats["Agility"] = stats.get("Agility") - 4
        return stats


class EvilEye(AbstractNegative):
    def __init__(self, base):
        super().__init__(base)

    def get_negative_effects(self):
        eff = self.base.get_negative_effects()
        eff.append("EvilEye")
        return eff.copy()

    def get_stats(self):
        stats = self.base.get_stats()
        stats["Luck"] = stats.get("Luck") - 10
        return stats.copy()


class Curse(AbstractNegative):
    def __init__(self, base):
        super().__init__(base)

    def get_negative_effects(self):
        eff = self.base.get_negative_effects()
        eff.append("Curse")
        return eff.copy()

    def get_stats(self):
        stats = self.base.get_stats()
        stats["Strength"] = stats.get("Strength") - 2
        stats["Endurance"] = stats.get("Endurance") - 2
        stats["Agility"] = stats.get("Agility") - 2
        stats["Luck"] = stats.get("Luck") - 2
        stats["Perception"] = stats.get("Perception") - 2
        stats["Charisma"] = stats.get("Charisma") - 2
        stats["Intelligence"] = stats.get("Intelligence") - 2
        return stats.copy()


if __name__ == '__main__':
    hero = Hero()

    print(hero.get_stats())
    # # {'HP': 128, 'MP': 42, 'SP': 100, 'Strength': 15, 'Perception': 4, 'Endurance': 8, 'Charisma': 2, 'Intelligence': 3,'Agility': 8, 'Luck': 1}
    #
    # print(hero.stats)
    # # {'HP': 128, 'MP': 42, 'SP': 100, 'Strength': 15, 'Perception': 4, 'Endurance': 8, 'Charisma': 2, 'Intelligence': 3, 'Agility': 8, 'Luck': 1}
    #
    # print(hero.get_negative_effects())
    # # []
    #
    # print(hero.get_positive_effects())
    # # []
    #
    # # накладываем эффект
    brs1 = Berserk(hero)
    # # for i in range(10):
    # #     brs1 = Berserk(brs1)
    # print(brs1.get_stats())
    # # {'HP': 178, 'MP': 42, 'SP': 100, 'Strength': 22, 'Perception': 1, 'Endurance': 15, 'Charisma': -1, 'Intelligence': 0, 'Agility': 15, 'Luck': 8}
    #
    # print(brs1.get_negative_effects())
    # # []
    #
    # print(brs1.get_positive_effects())
    # # ['Berserk']
    #
    # # накладываем эффекты
    # brs2 = Berserk(brs1)
    # cur1 = Curse(brs2)
    # print(cur1.get_stats())
    # # {'HP': 228, 'MP': 42, 'SP': 100, 'Strength': 27, 'Perception': -4, 'Endurance': 20, 'Charisma': -6, 'Intelligence': -5, 'Agility': 20, 'Luck': 13}
    #
    # print(cur1.get_positive_effects())
    # # ['Berserk', 'Berserk']
    #
    # print(cur1.get_negative_effects())
    # # ['Curse']
    #
    # # снимаем эффект Berserk
    # cur1.base = brs1
    # print(cur1.get_stats())
    # # {'HP': 178, 'MP': 42, 'SP': 100, 'Strength': 20, 'Perception': -1, 'Endurance': 13, 'Charisma': -3, 'Intelligence': -2, 'Agility': 13, 'Luck': 6}
    #
    # print(cur1.get_positive_effects())
    # # ['Berserk']
    #
    # print(cur1.get_negative_effects())
    # # ['Curse']

    ey = EvilEye(hero)
    ey1 = EvilEye(ey)
    print(ey.get_stats())

    ey1.base = brs1
    print(ey1.get_stats())
    print(ey1.base)
    # {'HP': 128, 'MP': 42, 'SP': 100, 'Strength': 15, 'Perception': 4, 'Endurance': 8, 'Charisma': 2, 'Intelligence': 3,'Agility': 8, 'Luck': -9}