#!/usr/bin/python
#
# stream version
# todo: benchmark

server = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
server.bind("/tmp/Connection.sock")
while True:
   server.listen(1)
   conn, addr = server.accept()
   while True:
      if datagram := conn.recv(1024):
         print(datagram)
conn.close()