#!/usr/bin/python

import string, sys
from scapy.all import *

host='192.168.3.100'

def arpping(host):
  try:
      ans,unans=srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=host))
      for s,r in ans:
          print "{0} is the MAC address for host {1}".format(r.src, r.psrc)
  except Exception, e:
      print e

def main():
  arpping(host)

if __name__ == '__main__':
  main()
