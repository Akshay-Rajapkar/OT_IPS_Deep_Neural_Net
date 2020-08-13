import scapy.all as scapy
from datetime import datetime
from csv_operations import *
lst = [1, 2, 6, 17, 41, 97]
dict = {1:"ICMP", 2:"IGMP", 6:"TCP", 17:"UDP", 41:"IPv4", 97:"EtherIP"}


def check_fields(packet, lst_mac):
    details = ["0"] * 9
    details[0] = str(datetime.now().replace(microsecond=0))

    if packet.haslayer(scapy.IP):
        details[1] = packet[scapy.IP].src
        details[2] = packet[scapy.IP].dst
        details[5] = packet[scapy.IP].proto

    if details[5] in lst:
        details[5] = dict[details[5]]
    else:
        details[5] = "Other"

    if packet.haslayer(scapy.TCP):
        details[6] = packet[scapy.TCP].sport
        details[7] = packet[scapy.TCP].dport
        if packet.haslayer(scapy.Raw):
            if "\x00\x00\x00\x00" in packet[scapy.Raw].load:
                details[5] = "Modbus"

    if packet.haslayer(scapy.UDP):
        details[6] = packet[scapy.UDP].sport
        details[7] = packet[scapy.UDP].dport

    for d in lst_mac:
        if d["ip"] == details[1]:
            details[3] = d["mac"]
        elif d['ip'] == details[2]:
            details[4] = d["mac"]

    #first_read(details)
    return check_repeat(details)



if __name__ == "__main__":
    check_fields(packet)
    show_fields(details)
