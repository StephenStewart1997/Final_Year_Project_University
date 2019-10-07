from __future__ import print_function
from scapy.all import *
import random
 
# Define end host and TCP port range
host = '192.168.3.100'
portRange = [20, 21, 22, 23, 25, 53, 67, 68, 69, 80, 123, 143, 161, 162, 443]
 
# Send SYN with random Src Port for each Dst port
for dstPort in portRange:
    srcPort = random.randint(1025,65534)
    resp = sr1(IP(dst=host)/TCP(sport=srcPort,dport=dstPort,flags="S"),timeout=1,verbose=0)
 
    if resp is None:
        print('{}:{} is filtered (silently dropped).'.format(host, str(dstPort)))
 
    elif(resp.haslayer(TCP)):
        if(resp.getlayer(TCP).flags == 0x12):
            # Send a gratuitous RST to close the connection
            send_rst = sr(IP(dst=host)/TCP(sport=srcPort,dport=dstPort,flags='R'),timeout=1,verbose=0)
            print('{}:{} is open.'.format(host, str(dstPort)))
        elif (resp.getlayer(TCP).flags == 0x14):
            print('{}:{} is closed.'.format(host, str(dstPort)))
 
    elif(resp.haslayer(ICMP)):
        if(int(resp.getlayer(ICMP).type)==3 and int(resp.getlayer(ICMP).code) in [1,2,3,9,10,13]):
            print('{}:{} is filtered (silently dropped).'.format(host, str(dstPort)))
#filtered(silently dropped) = no response
