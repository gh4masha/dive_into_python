import socket
import datetime


class ClientError(Exception):
    pass


class Client:
    def __init__(self, host, port, timeout):
        self.host = host
        self.port = port
        self.timeout = timeout

    def put(self, server_metric, value, timestamp):

        with socket.create_connection(address=(self.host, self.port), timeout=self.timeout) as sock:

            data = 'put ' + str(server_metric) + ' ' + str(format(value, '.3f')) + ' ' + str(timestamp) + '\n'
            # print(data)
            try:
                sock.sendall(data.encode("utf8"))
                socket_result = sock.recv(1024)
                result = socket_result.decode("utf8")
                if not str(result).startswith('ok'):
                    raise ClientError
            except:
                raise ClientError

    def get(self, metric_name):
        with socket.create_connection(address=(self.host, self.port), timeout=self.timeout) as sock:
            data = 'get ' + metric_name + '\n'
            try:
                sock.sendall(data.encode("utf8"))
                socket_result = sock.recv(1024)

                lines = socket_result.decode('utf8').split('\n')

                if lines[0] != 'ok':
                    raise ClientError

                result = dict()

                for i in range(1, len(lines)):
                    l = lines[i]
                    if len(l) < 2:
                        break
                    parts = l.split(' ')
                    if result.get(parts[0]) is not None:

                        t = result.get(parts[0])
                        t.append((int(parts[2]), float(parts[1])))
                        result.update({parts[0]: t})

                    else:
                        result[parts[0]] = [(int(parts[2]), float(parts[1]))]

                return result
                # print(socket_result)
            #     ok\npalm.cpu 10.5 1501864247\neardrum.cpu 15.3 1501864259\n\n

            except:
                pass

# client = Client("127.0.0.1", 10002, timeout=15)
#
# client.put("palm.cpu", 0.5, timestamp=1150864247)
# client.put("palm.cpu", 2.0, timestamp=1150864248)
# client.put("palm.cpu", 0.5, timestamp=1150864248)
#
# client.put("eardrum.cpu", 3, timestamp=1150864250)
# client.put("eardrum.cpu", 4, timestamp=1150864251)
# client.put("eardrum.memory", 4200000)
#
# client.get("*")
