from abc import ABC, abstractmethod


class Pet:
    def __init__(self, name=None):
        self.name = name


class AbstrDog(Pet, ABC):
    pass


class Dog(AbstrDog):
    def __init__(self, name=None, breed=None):
        super().__init__(name)
        self.breed = breed
        self.name = 'test'


dog = Dog("rick", "buldog")

