#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author:   S.H.
Version:  0.1
Date:     2014-12-22
Description:
  Multiply host, single port.
"""

import socket
import os

f = open("ip.txt", "r")
print("===Scan Starting...===")
for line in f.readlines():
  hostIP = socket.gethostbyname(line)
  # print(hostIP)
  port = 80
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  result = sock.connect_ex((hostIP,port))
  if result == 0:
    print("Port {} is OPEN on:\t\t\t {}".format(port, hostIP))
  else:
    print("Port {} is NOT open on {}".format(port, hostIP))
  sock.close()
f.close()
print("===Scan Complement===")
