"""
Это вспомогательный скрипт для тестирования сервера из задания на неделе 6.

Для запуска скрипта на локальном компьютере разместите рядом файл client.py,
где содержится код клиента, который открывается по прохождении задания
недели 5.

Сначала запускаете ваш сервер на адресе 127.0.0.1 и порту 8888, а затем
запускаете этот скрипт.
"""
import sys
import socket
import time


class ClientError(Exception):
    """Общий класс исключений клиента"""
    pass


class ClientSocketError(ClientError):
    """Исключение, выбрасываемое клиентом при сетевой ошибке"""
    pass


class ClientProtocolError(ClientError):
    """Исключение, выбрасываемое клиентом при ошибке протокола"""
    pass


class Client:
    def __init__(self, host, port, timeout=None):
        # класс инкапсулирует создание сокета
        # создаем клиентский сокет, запоминаем объект socke.socket в self
        self.host = host
        self.port = port
        try:
            self.connection = socket.create_connection((host, port), timeout)
        except socket.error as err:
            raise ClientSocketError("error create connection", err)

    def _read(self):
        """Метод для чтения ответа сервера"""
        data = b""
        # накапливаем буфер, пока не встретим "\n\n" в конце команды
        while not data.endswith(b"\n\n"):
            try:
                data += self.connection.recv(1024)
            except socket.error as err:
                raise ClientSocketError("error recv data", err)

        # не забываем преобразовывать байты в объекты str для дальнейшей работы
        decoded_data = data.decode()

        status, payload = decoded_data.split("\n", 1)
        payload = payload.strip()

        # если получили ошибку - бросаем исключение ClientError
        if status == "error":
            raise ClientProtocolError(payload)

        return payload

    def put(self, key, value, timestamp=None):
        timestamp = timestamp or int(time.time())

        # отправляем запрос команды put
        try:
            self.connection.sendall(
                f"put {key} {value} {timestamp}\n".encode()
            )
        except socket.error as err:
            raise ClientSocketError("error send data", err)

        # разбираем ответ
        self._read()

    def get(self, key):
        # формируем и отправляем запрос команды get
        try:
            self.connection.sendall(
                f"get {key}\n".encode()
            )
        except socket.error as err:
            raise ClientSocketError("error send data", err)

        # читаем ответ
        payload = self._read()

        data = {}
        if payload == "":
            return data

        # разбираем ответ для команды get
        for row in payload.split("\n"):
            key, value, timestamp = row.split()
            if key not in data:
                data[key] = []
            data[key].append((int(timestamp), float(value)))

        return data

    def close(self):
        try:
            self.connection.close()
        except socket.error as err:
            raise ClientSocketError("error close connection", err)


def run(host, port):

    client1 = Client(host, port, timeout=5)
    client2 = Client(host, port, timeout=5)

    try:
        client1.connection.sendall(b"malformed command test\n")
        client1._read()
        client2.connection.sendall(b"malformed command test\n")
        client2._read()
    except ClientSocketError as err:
        print(f"Ошибка общения с сервером: {err.__class__}: {err}")
        sys.exit(1)
    except ClientProtocolError:
        pass
    else:
        print("Неверная команда, отправленная серверу, должна возвращать ошибку протокола")
        sys.exit(1)

    try:
        client1.put("k1", 0.25, timestamp=1)
        client2.put("k1", 2.156, timestamp=2)
        client1.put("k1", 0.35, timestamp=3)
        client2.put("k2", 30, timestamp=4)
        client1.put("k2", 40, timestamp=5)
        client1.put("k2", 40, timestamp=5)
    except Exception as err:
        print(f"Ошибка вызова client.put(...) {err.__class__}: {err}")
        sys.exit(1)

    expected_metrics = {
        "k1": [(1, 0.25), (2, 2.156), (3, 0.35)],
        "k2": [(4, 30.0), (5, 40.0)],
    }

    try:
        metrics = client1.get("*")
        if metrics != expected_metrics:
            print(f"client.get('*') вернул неверный результат. Ожидается: {expected_metrics}. Получено: {metrics}")
            sys.exit(1)
    except Exception as err:
        print(f"Ошибка вызова client.get('*') {err.__class__}: {err}")
        sys.exit(1)

    expected_metrics = {"k2": [(4, 30.0), (5, 40.0)]}

    try:
        metrics = client2.get("k2")
        if metrics != expected_metrics:
            print(f"client.get('k2') вернул неверный результат. Ожидается: {expected_metrics}. Получено: {metrics}")
            sys.exit(1)
    except Exception as err:
        print(f"Ошибка вызова client.get('k2') {err.__class__}: {err}")
        sys.exit(1)

    try:
        result = client1.get("k3")
        if result != {}:
            print(f"Ошибка вызова метода get с ключом, который еще не был добавлен. Ожидается: пустой словарь. Получено: {result}")
            sys.exit(1)
    except Exception as err:
        print(f"Ошибка вызова метода get с ключом, который еще не был добавлен: {err.__class__} {err}")
        sys.exit(1)

    print("Похоже, что все верно! Попробуйте отправить решение на проверку.")


if __name__ == "__main__":
    run("127.0.0.1", 8888)