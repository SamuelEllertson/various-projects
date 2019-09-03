#!/usr/bin/env python
 
from threading import Thread
import socket
import sys

def main():
    
    Thread(target=printSocket, daemon=True).start()
    exitHandler()

def printSocket():
    HOST = '127.0.0.1'
    PORT = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()

        while True:
            conn, addr = s.accept()
            Thread(target=handleConnection, args=(conn, addr), daemon=True).start()

def handleConnection(conn, addr):
    with conn:
        print(f"{addr} connected")

        while True:
            data = str(conn.recv(1024), encoding="utf-8")

            if not data:
                break

            print(f"{addr}: {data}")

def exitHandler():
    try:
        while True:
            data = input("")

            if data == "exit":
                gracefulExit()
    except:
        gracefulExit()

def gracefulExit():
    print("shutting down")
    sys.exit()


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stdin.reconfigure(encoding='utf-8')
    main()