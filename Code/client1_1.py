import threading
import socket
#without creating the class
while True:
    clisocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    clisocket.connect(('localhost', 8020))
    print("The client has been connected..")
    print("The message from the server: ", clisocket.recv(256).decode())

    print("Please keep proving the messages to send to server..")


    msg = input("Please write the message (String in quotes): ")
    clisocket.send(bytes(msg, encoding='utf8'))
    clisocket.close()