#!/usr/bin/env python
import netfilterqueue
import scapy.all as scapy
from protocol import *
from net_scan import *


def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if check_fields(scapy_packet, lst_mac):
    #print(scapy_packet.show())
        packet.accept()
    else:
        packet.drop()


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
print("\n\n")
print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("Date & Time"+" "*13 +"Source IP"+" "*14 + "Destination IP"+" "*11 + "Source MAC"+" "*14 + "Destination MAC"+" "*9 + "Protocol"+"\t" + "Src Port" +"\t" + "Dst Port")
print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")

fields = ["Date & Time", "Source IP", "Destination IP", "Source MAC", "Destination MAC", "Protocol", "Src Port", "Dst Port"]


def start():
    with open('Baselines.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)


with open('Alerts.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)

#start()
lst_mac = record_scan("10.0.2.1/24")
try:
    queue.run()
except:
    pass
