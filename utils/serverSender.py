import socket
import json
from utils.path import get_file_from_working_dir


class ServerData:
    def __init__(self, ip: str = "0.0.0.0", port: int = 0) -> None:
        self.ip: str = ip
        self.port: int = port

    def __str__(self) -> str:
        return f"{self.ip}:{self.port}"


class ServerSender:
    def __init__(self, serverData: ServerData) -> None:
        self.server_data: ServerData = serverData

    def send(self, data: str) -> None:
        clientSocket = socket.socket(socket.AF_INET,
                                     socket.SOCK_STREAM)
        clientSocket.connect((self.server_data.ip,
                              self.server_data.port))

        data = str(data)
        clientSocket.send(data.encode())
        clientSocket.close()


def update_server_data(input_data: ServerData, config_file: str = "") -> None:
    read_data = read_server_data(config_file).__dict__
    input_data = input_data.__dict__

    for key, value in input_data.items():
        if value is not None:
            read_data[key] = value

    write_server_data(ServerData(**read_data))


def write_server_data(input_data: ServerData, config_file: str = "") -> None:
    path = str(get_file_from_working_dir('user_data/server', 'server_data.json') if config_file == "" else config_file)
    with open(path, "w") as config:
        json.dump(input_data.__dict__, config)


def read_server_data(config_file: str = "") -> ServerData:
    path = str(get_file_from_working_dir('user_data/server', 'server_data.json') if config_file == "" else config_file)
    with open(path, "r") as config:
        server_json = json.loads(config.read())

    return ServerData(**server_json)


def load_server(config_file: str = "") -> ServerSender:
    data = read_server_data(config_file)

    return ServerSender(data)
