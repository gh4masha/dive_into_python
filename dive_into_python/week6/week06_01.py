# server

import asyncio


class ClientServerProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport

    storage = {}

    def data_received(self, data):
        resp = self.process_data(data.decode())
        if resp is None:
            self.transport.write('error\n\n'.encode('utf8'))
        else:
            self.transport.write(resp.encode())


    def get_metrics(self, metric):
        result = ''
        if metric == '*':
            for key in self.storage:
                for items in self.storage.get(key):
                    result = key + ' ' + items[1] + items[0] + '\n'
        elif self.storage.get(metric) is not None:
            for items in self.storage.get(metric):
                result = metric + ' ' + items[1] + items[0] + '\n'
        else:
            return 'error\n\n'

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
        try:
            if self.storage.get(name) is not None:

                t = self.storage.get(name)
                t.append((int(time), float(value)))
                self.storage.update({name: t})

            else:
                self.storage[name] = [(int(time), float(value))]
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
