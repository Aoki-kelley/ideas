import socket
import time


class ClientTCP:
    def __init__(self):
        """初始化函数"""
        self.DATA_HEADER_LENGTH = 16
        self.connect_config = (None, None)
        try:
            self.machine = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
            self.machine.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        except Exception as e:
            print("client init fail: ", repr(e))

    def __str__(self):
        return "Socket ClientTCP {}".format(self.connect_config)

    def __del__(self):
        self.machine.close()
        del self

    def connect_to_server(self, server_ip, server_port):
        """连接服务器"""
        self.connect_config = (server_ip, server_port)
        try:
            self.machine.connect(self.connect_config)
            # print(self.machine.connect_ex(self.connect_config))
            print("connect to {} success".format(self.connect_config))
        except socket.error:
            print("connect to {} fail".format(self.connect_config))

    def connect_close(self):
        """关闭连接"""
        self.connect_config = (None, None)
        self.machine.close()

    def send_data_to_server(self, data, func=None):
        """发送到服务器 发送的数据格式为定长的数据长度信息+数据 func为可指定的处理数据的函数"""
        print(time.time(), end="|")
        try:
            print("send data to {}".format(self.connect_config))
            data_length_s = ("%{}d".format(self.DATA_HEADER_LENGTH) % len(data)).encode()  # 数据头信息长度补偿
            data = data_length_s + data
            if func is not None:
                self.machine.send(func(data))
            else:
                self.machine.send(data)
            print("send success")
        except Exception as e:
            print("send fail: ", repr(e))


class ClientUDP:
    def __init__(self, callback=False):
        """初始化函数"""
        self.DATA_HEADER_LENGTH = 16
        self.callback = callback
        try:
            self.machine = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
            self.machine.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        except Exception as e:
            print("client init fail: ", repr(e))

    def __str__(self):
        return "Socket ClientUDP"

    def send_data_to_server(self, server_ip, server_port, data, func=None):
        """发送到服务器 发送的数据格式为定长的数据长度信息+数据 func为可指定的处理数据的函数"""
        print(time.time(), end="|")
        try:
            print("send data to {}".format((server_ip, server_port)))
            data_length_s = ("%{}d".format(self.DATA_HEADER_LENGTH) % len(data)).encode()  # 数据头信息长度补偿
            data = data_length_s + data

            if func is not None:
                self.machine.sendto(func(data), (server_ip, server_port))
            else:
                self.machine.sendto(data, (server_ip, server_port))

            if self.callback:  # 开启服务端回传
                try:
                    self.machine.settimeout(2)
                    server_callback_length_s, server_info = self.machine.recvfrom(self.DATA_HEADER_LENGTH)  # 等待服务器回应
                    if server_info:
                        print(time.time(), end="|")
                        print("receive callback from {}".format(server_info, server_info))
                        if int(server_callback_length_s) != int(data_length_s):
                            print("warning! server_callback_length_s is not equal to data_length_s")
                    self.machine.settimeout(None)
                except socket.timeout:
                    self.machine.settimeout(None)
                    print("warning!dont receive callback from server")

        except Exception as e:
            print("send fail: ", repr(e))


if __name__ == "__main__":
    # # TCP TEST
    # for i in range(10):
    #     client_tcp_test = ClientTCP()
    #     client_tcp_test.connect_to_server("localhost", 8000)
    #     client_tcp_test.send_data_to_server("test data {}".format(i).encode())
    #     time.sleep(0.1)
    #     del client_tcp

    # UDP TEST
    client_udp_test = ClientUDP()
    for i in range(5):
        client_udp_test.send_data_to_server("localhost", 8001, "test data {}".format(i).encode())
        time.sleep(0.1)
