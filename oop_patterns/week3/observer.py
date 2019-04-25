# {"title": "Покоритель", "text": "Дается при выполнении всех заданий в игре"}

from abc import ABC, abstractmethod


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
    @abstractmethod
    def update(self, achievement):
        pass


class ShortNotificationPrinter(AbstractObserver):

    def __init__(self):
        self.achievements = set()

    def update(self, achievement):
        if achievement["title"] not in self.achievements:
            self.achievements.add(achievement["title"])


class FullNotificationPrinter(AbstractObserver):

    def __init__(self):
        self.achievements = list()

    def update(self, achievement):
        if achievement not in self.achievements:
            self.achievements.append(achievement)


shortNotificationPrinter = ShortNotificationPrinter()
fullNotificationPrinter = FullNotificationPrinter()

observableEngine = ObservableEngine()
observableEngine.subscribe(shortNotificationPrinter)
observableEngine.subscribe(fullNotificationPrinter)

observableEngine.notify({"title": "title1", "text": "text1"})
observableEngine.notify({"title": "title2", "text": "text2"})
observableEngine.notify({"title": "title1", "text": "text1"})
observableEngine.notify({"title": "title4", "text": "text4"})

print(shortNotificationPrinter.achievements)
print('------------')
print(fullNotificationPrinter.achievements)