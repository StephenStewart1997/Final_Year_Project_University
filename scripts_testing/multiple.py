from scapy.all import send, IP, ICMP

send(IP(dst="192.168.3.100")/ICMP())
send(IP(dst="192.168.4.100")/ICMP())
