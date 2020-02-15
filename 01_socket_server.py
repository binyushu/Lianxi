# -*-coding:utf-8-*-

import socket


def main():
    while True:
        # 1.创建套接字
        server = socket.socket()

        # 2.绑定本地IP和端口
        server.bind(("", 8080))

        # 3.让默认的套接字由主动变为被动listen
        server.listen(128)

        # 4.等待客户端的连接
        new_client_socket, new_clent_addr = server.accept()
        print(new_clent_addr)


        while True:
            # 5.接受客户端发送过来的请求
            recv_data = new_client_socket.recv(1024)
            print(recv_data.decode("gbk"))

            new_client_socket.send("haahhha".encode('utf-8'))

        # 6.关闭新创建的套接字
        new_client_socket.close()

    # 7.关闭套接字
    server.close()


if __name__ == '__main__':
    main()
