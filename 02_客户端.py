# -*-coding:utf-8-*-

import socket

clinet = socket.socket()
clinet.connect(("127.0.0.1", 8080))
server_data = clinet.recv(1024)
print("服务端：{}".format(server_data.decode("utf-8")))


while True:
    input_data = input("请输入要输入的数据：\n")
    clinet.send(input_data.encode("utf-8"))
    server_data = clinet.recv(1024)
    print("服务端：{}".format(server_data.decode("utf-8")))
    

# clinet.close()
