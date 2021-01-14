import socket
import threading



afn = socket.AF_INET

prot = socket.SOCK_DGRAM



s = socket.socket(afn,prot)
ip = str(input("Enter ip of your Friend os:"))

sr = socket.socket(afn,prot)
ipr = str(input("Enter your ip:"))
port = 3333
sr.bind((ipr,port))


print("\n\t\t\t\tWelcome to chit chat\n\n\n")

def send():
  while(True):
     x = str(input())
     s.sendto(x.encode(), (ip,3333))

def receive():
  while(True):
     x = sr.recvfrom(2048)
     print("\t\t\t\t")
     print("\t\t\t\t\t\t" + x[0].decode())

x1 = threading.Thread(target = send)
x2 = threading.Thread(target = receive)

x1.start()
x2.start()
