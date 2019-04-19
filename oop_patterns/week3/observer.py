# {"title": "Покоритель", "text": "Дается при выполнении всех заданий в игре"}

from abc import ABC


class Engine():
    pass


class ObservableEngine(Engine):
    def __init__(self):
        self.engine = 1
        self.__subscribers = set()

    def subscribe(self, subscriber):
        self.__subscribers.add(
            subscriber)

    def unsubscribe(self, subscriber):
        self.__subscribers.remove(subscriber)

    def notify(self, message):
        for subscriber in self.__subscribers:
            subscriber.update(message)


class AbstractObserver(ABC):
    def update(self, achievement):
        pass


class ShortNotificationPrinter(AbstractObserver):

    def __init__(self):
        self.achievements = set()

    def update(self, achievement):
        if achievement["title"] not in self.achievements:
            self.achievements.append(achievement["title"])


class FullNotificationPrinter():

    def __init__(self):
        self.achievements = list()

    def update(self, achievement):
        if achievement["text"] not in self.achievements:
            self.achievements.append(achievement["text"])
