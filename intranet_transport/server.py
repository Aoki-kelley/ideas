import socket
import time
import threading


class ServerTCP:
    def __init__(self):
        """初始化函数"""
        self.DATA_HEADER_LENGTH = 16
        self.server_config = (None, None)
        self.machine = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.machine.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        except Exception as e:
            print("server init fail: ", repr(e))

    def __str__(self):
        return "Socket ClientTCP {}".format(self.server_config)

    def __del__(self):
        self.machine.close()
        del self

    def listen_start(self, bind_ip, bind_port, listen_max, func=None):
        """开启监听 func为可指定的处理数据的函数"""
        self.server_config = (bind_ip, bind_port)
        self.machine.bind(self.server_config)
        self.machine.listen(listen_max)

        while True:
            cli, addr = self.machine.accept()
            if cli:
                print(time.time(), end="|")
                print("connection from {}".format(addr))
                receiver_thread = threading.Thread(target=self.receive_data_from_client, args=(cli, func))
                receiver_thread.start()
                # self.receive_data_from_client(cli, func)

    def listen_stop(self):
        """结束监听"""
        self.machine.close()

    def receive_data_from_client(self, client_socket, func=None):
        """接收数据 接收的数据格式为定长的数据长度信息+数据 func为可指定的处理数据的函数"""
        try:
            data_from_client = client_socket.recv(self.DATA_HEADER_LENGTH)  # 读取数据头信息,即实际数据长度
            data_size = int(data_from_client[0:self.DATA_HEADER_LENGTH])
            receive_buf = b""
            if data_size:
                while data_size:
                    tmp_buf = client_socket.recv(data_size)
                    data_size -= len(tmp_buf)
                    receive_buf += tmp_buf
            if func is not None:
                func(receive_buf)
            else:
                print(receive_buf)
            del client_socket
        except Exception as e:
            print("receive error: ", repr(e))


class ServerUDP:
    def __init__(self, bind_ip, bind_port, callback=False):
        """初始化函数"""
        self.DATA_HEADER_LENGTH = 16
        self.RECEIVE_DATA_MAX_LENGTH = 300000
        self.callback = callback
        try:
            self.machine = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
            self.machine.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.machine.bind((bind_ip, bind_port))
        except Exception as e:
            print("client init fail: ", repr(e))

    def __str__(self):
        return "Socket ClientUDP"

    def wait_data_from_client(self, func=None):
        """等待数据 接收的数据格式为定长的数据长度信息+数据 func为可指定的处理数据的函数"""
        while True:
            data_from_client, client_info = self.machine.recvfrom(self.RECEIVE_DATA_MAX_LENGTH)
            print(time.time(), end="|")
            print("receive data from {}".format(client_info))
            if client_info:
                self.data_handler(data_from_client, client_info, func)

    def data_handler(self, data, client_info, func=None):
        try:
            data_size = int(data[0:self.DATA_HEADER_LENGTH])
            receive_buf = b""
            if data_size:
                receive_buf = data[self.DATA_HEADER_LENGTH:]
            if func is not None:
                func(receive_buf)
            else:
                print(receive_buf)

            if self.callback:  # 开启回传
                self.machine.sendto(str(len(receive_buf)).encode(), client_info)

        except Exception as e:
            print("receive fail: ", repr(e))


if __name__ == "__main__":
    # # TCP TEST
    # server_tcp_test = ServerTCP()
    # server_tcp_test.listen_start("localhost", 8000, 5)

    # UDP TEST
    server_udp_test = ServerUDP("localhost", 8000)
    server_udp_test.wait_data_from_client()
