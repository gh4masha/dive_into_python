class SomeObject:
    def __init__(self):
        self.integer_field = 0
        self.float_field = 0.0
        self.string_field = ""


EventGet(<type>) создаёт событие получения данных соответствующего типа
EventSet(<value>) создаёт событие изменения поля типа type(<value>)
Необходимо реализовать классы

class NullHandler:

class IntHandler:

class FloatHandler:

class StrHandler:


if __name__=='__main__':
    chain = IntHandler(FloatHandler(StrHandler(NullHandler())))