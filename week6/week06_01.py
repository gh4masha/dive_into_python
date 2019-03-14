# server

import asyncio





class ClientServerProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        resp = self.process_data(data.decode())
        self.transport.write(resp.encode())


    def get_metrics(self, metric):
        return 'fkjdfnkd'


    def process_data(self, request):
        parts_of_request = request.split(' ')

        if parts_of_request[0]=='get':
            if len(parts_of_request)==2:
                return self.get_metrics(parts_of_request[1])
            elif:
                return 'error\n\n'
        elif parts_of_request[0]=='put':
            if len(parts_of_request)==4:
                self.put_metrics(parts_of_request[1], parts_of_request[1], parts_of_request[1])
            elif:
                return 'error\n\n'


        return 1

    def put_metrics(self, name, value, time):

        self.storage

        pass


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
