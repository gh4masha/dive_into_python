class SomeObject:
    def __init__(self):
        self.integer_field = 0
        self.float_field = 0.0
        self.string_field = ""


# EventGet(<type>) создаёт событие получения данных соответствующего типа
# EventSet(<value>) создаёт событие изменения поля типа type(<value>)
# Необходимо реализовать классы


class EventGet:
    def __init__(self, t):
        self.t = t

class EventSet:
    def __init__(self, v):
        self.value = v


# class Handler:
#     def __init__(self, nextHandler):
#         self.nextHandler = nextHandler
#
#     def handle(self, obj, event):
#         pass


class NullHandler:
    def __init__(self, nextHandler):
        self.nextHandler = nextHandler

    def __init__(self):
        pass

    def handle(self, obj, event):
        pass


class IntHandler(NullHandler):
    def __init__(self, nextHandler):
        self.nextHandler = nextHandler

    def handle(self, obj, event):
        if isinstance(event, EventGet) and event.t is int:
            return obj.integer_field
        elif isinstance(event, EventSet) and event.value is int:
            obj.integer_field = event.value
        else:
            return self.nextHandler.handle(obj, event)

class FloatHandler(NullHandler):
    def __init__(self, nextHandler):
        self.nextHandler = nextHandler

    def handle(self, obj, event):
        if isinstance(event, EventGet) and event.t is float:
            return obj.float_field
        elif isinstance(event, EventSet) and event.value is float:
            obj.float_field = event.value
        else:
            return self.nextHandler.handle(obj, event)

class StrHandler(NullHandler):
    def __init__(self, nextHandler):
        self.nextHandler = nextHandler

    def handle(self, obj, event):
        if isinstance(event, EventGet) and event.t is str:
            return obj.string_field
        elif isinstance(event, EventSet) and event.value is str:
            obj.string_field = event.value
        else:
            return self.nextHandler.handle(obj, event)


if __name__=='__main__':

    obj = SomeObject()
    obj.integer_field = 42
    obj.float_field = 3.14
    obj.string_field = "some text"
    chain = IntHandler(FloatHandler(StrHandler(NullHandler())))

    print(chain.handle(obj, EventGet(int)))    #    42
    print(chain.handle(obj, EventGet(float)))  #    3.14
    print(chain.handle(obj, EventGet(str)))    #    'some text'
    print(chain.handle(obj, EventSet(100)))
    print(chain.handle(obj, EventGet(int)))    #    100
    print(chain.handle(obj, EventSet(0.5)))
    print(chain.handle(obj, EventGet(float)))  #    0.5
    print(chain.handle(obj, EventSet('new text')))
    print(chain.handle(obj, EventGet(str)))    #    'new text'
