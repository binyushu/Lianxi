# -*-coding:utf-8-*-

import socket

server = socket.socket()
server.bind(("0.0.0.0", 8080))
server.listen()
new_socket, new_addr = server.accept()



while True:
    new_socket.send("欢迎来到服务端".encode("utf-8"))
    tmp_data = new_socket.recv(1024)
    print(tmp_data.decode("utf-8"))
    input_data = input()
    new_socket.send(input_data.encode("utf-8"))


# print(data)
# new_socket.close()
