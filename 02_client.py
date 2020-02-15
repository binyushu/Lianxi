# -*-coding:utf-8-*-

import socket


def main():
    # 1.创建套接字
    tcp_client_socket = socket.socket()
    # 2.连接服务器
    # 创建连接服务器的IP和端口
    server_addr = tcp_client_socket.connect(("192.168.192.1",8080))

    # 3.发送数据
    send_tada = input("请输入要发送的数据:\n")
    tcp_client_socket.send(send_tada.encode("utf-8"))

    # 4.关闭套接字
    tcp_client_socket.close()


if __name__ == '__main__':
    main()
