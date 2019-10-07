from scapy.all import *

send(IP(src="17.127.231.15", dst="192.168.3.100")/ICMP())
