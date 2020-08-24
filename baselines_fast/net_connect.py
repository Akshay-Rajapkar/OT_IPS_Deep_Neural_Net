#!/usr/bin/env python
import netfilterqueue
import scapy.all as scapy
from protocol import *
from net_scan import *


def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    check_fields(scapy_packet, lst_mac)
    #print(scapy_packet.show())
    packet.accept()


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
print("\n\n")
print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("Date & Time"+" "*13 +"Source IP"+" "*14 + "Destination IP"+" "*11 + "Source MAC"+" "*14 + "Destination MAC"+" "*9 + "Protocol"+"\t" +"Flags"+ " "*3 + "Src Port" +"\t" + "Dst Port"+ "\t" + "Length")
print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

fields = ["Date & Time", "Source IP", "Destination IP", "Source MAC", "Destination MAC", "Protocol","Flags", "Src Port", "Dst Port", "Length"]


def start():
    with open('Baselines.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)


start()
lst_mac = record_scan("192.168.0.1/24")
try:
    queue.run()
except:
    pass
