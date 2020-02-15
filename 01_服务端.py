# -*-coding:utf-8-*-

import socket

#创建套接字
server = socket.socket()

#绑定IP和端口
server.bind(("0.0.0.0", 8080))

#让默认的套接字由主动变为被动listen
server.listen()

#等待客户连接，阻塞
new_socket, new_addr = server.accept()



while True:
    new_socket.send("欢迎来到服务端".encode("utf-8"))
    tmp_data = new_socket.recv(1024)
    print(tmp_data.decode("utf-8"))
    input_data = input()
    new_socket.send(input_data.encode("utf-8"))


# print(data)
# new_socket.close()
