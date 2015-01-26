#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author:   S.H.
Version:  0.1
Date:     2015-01-17
Description: 
  Scan ip:
    74.125.131.0/24
    74.125.131.99-125
    74.125.131.201
  Only three format above.
  Read ip form a ip.txt, and scan all port(or a list port).
"""


import os
import io
import socket

fileOpen = open("ip.txt", 'r')
for line in fileOpen.readlines():
  fileTemp = open("temp.txt", 'a')
  if line.find("-") != -1:
    list = line[:line.index("-")]
    ip = [int(a) for a in list.split(".")]
    b = int(line[line.index("-")+1:])
    for i in range(ip[3], b+1):
      fileTemp.write(str(ip[0])+"."+str(ip[1])+"."+str(ip[2])+"."+str(i)+"\n")
  elif line.find("/") != -1:
    list = line[:line.index("/")]
    ip = [int(a) for a in list.split(".")]
    for i in range(256):
      fileTemp.write(str(ip[0])+"."+str(ip[1])+"."+str(ip[2])+"."+str(i)+"\n")
  else:
    fileTemp.write(line)
fileTemp.close()
fileOpen.close()

# print("process is here.")

f = open("temp.txt", 'r')
print("===Scan Staring===")
for line in f.readlines():
  hostIP = socket.gethostbyname(line)
  # print(hostIP)
  # for port in range(65535):
  
  portList = [80, 8080]
  for port in portList:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((hostIP, port))
    if result == 0:
      print("Port {} is OPEN on:\t\t\t {}".format(port, hostIP))
    else:
      print("Port {} is NOT open on {}".format(port, hostIP))
    sock.close()
f.close()
os.remove("temp.txt")
print("===Scan Complement===")
