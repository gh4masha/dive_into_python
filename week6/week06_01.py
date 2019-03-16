# server

import asyncio
import threading

class ClientServerProtocol(asyncio.Protocol):
    
    def __init__(self):
        super(ClientServerProtocol, self).__init__()
        self.mutex = threading.RLock()
        
    def connection_made(self, transport):
        
        self.transport = transport

    storage = {}

    def data_received(self, data):
        resp = self.process_data(data.decode('utf8'))
        if resp is None:
            self.transport.write('error\n\n'.encode('utf8'))
        else:
            # print('storage:',self.storage)
            # print(data,resp)
            self.transport.write(str(resp).encode('utf8'))

    def get_metrics(self, metric):
        with self.mutex:
            result = ''

            metric = metric.replace(' ', '')
            metric = metric.replace('\n', '')
            if metric == '*':
                # return self.storage
                for key in self.storage:
                    for items in self.storage.get(key):
                        # print('get ********* ', key,items[0],items[1], '*********')
                        result = result + str(key) + ' ' + str(items[0]) + ' ' + str(items[1]) + '\n'
                        # print('--------------------------------',result)
            elif self.storage.get(metric) is not None:
                # return self.storage.get(metric)
                for items in self.storage.get(metric):
                    result = result + metric + ' ' + str(items[0]) + ' ' + str(items[1]) + '\n'
            else:
                return 'ok\n\n'
            result = 'ok\n'+result+'\n'
            return result

    def process_data(self, request):
        parts_of_request = request.split(' ')

        if parts_of_request[0] == 'get':
            if len(parts_of_request) == 2:
                return self.get_metrics(parts_of_request[1])
            else:
                return 'error\n\n'
        elif parts_of_request[0] == 'put':
            if len(parts_of_request) == 4:
                self.put_metrics(parts_of_request[1], parts_of_request[2], parts_of_request[3])
                return 'ok\n\n'
            else:
                return 'error\n\n'
        return 'error\n\n'

    def put_metrics(self, name, value, time):
        with self.mutex:
            time=time.replace('\n','')
            time=time.replace(' ','')
            try:
                if self.storage.get(name) is not None:
                    t = self.storage.get(name)
                    if (float(value), int(time)) not in t:
                        t.append((float(value), int(time)))
                        self.storage.update({name: t})

                else:
                    self.storage[name] = [(float(value), int(time))]
                return 'ok\n\n'
            except Exception:
                return 'error\n\n'


def run_server(host, port):
    loop = asyncio.get_event_loop()

    coro = loop.create_server(
        ClientServerProtocol,
        host, port
    )

    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


if __name__ == "__main__":
    run_server("127.0.0.1", 8888)
