from __future__ import print_function

from scapy.all import rdpcap


def handler(event, context):  
    # Load PCAP file
    pcap = rdpcap('/root/scripts/packet_replay.pcap')

    # Iterate over each packet in the PCAP file
    for pkt in pcap:
        print(pkt.summary())

if __name__ == '__main__':  
    handler(event=None, context=None)
