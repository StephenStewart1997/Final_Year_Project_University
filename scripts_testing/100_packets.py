#!/usr/bin/env python

"""
This script sends an echo reply
with a user defined messsage
"""

from scapy.all import *
send(IP(dst="192.168.3.100")/ICMP()/"100 packets", count=100)
