from socket import *
s = socket()
s.connect(("localhost",15000))
s.send()
