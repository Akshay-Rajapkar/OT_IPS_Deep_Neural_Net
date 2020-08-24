import scapy.all as scapy
from datetime import datetime
from net_scan import record_scan
lst = [1, 2, 6, 17, 41, 97]
dict = {1:"ICMP", 2:"IGMP", 6:"TCP", 17:"UDP", 41:"IPv4", 97:"EtherIP"}
lst_flags = [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 16, 17, 18, 20, 24, 25, 32, 33, 34, 36, 40, 48, 194]
dict_flags = {1: "F", 2: "S", 3: "SF", 4: "R", 5: "RF", 6: "RS", 8: "P", 9: "PF", 10: "PS", 12: "PR", 16: "A", 17: "AF",
              18: "AS", 20: "AR", 24: "AP", 25: "APF", 32: "U", 33: "UF", 34: "US", 36: "UR", 40: "UP", 48:"UA", 194:"SEC" }
select_param = [1, 2, 5, 6, 7, 8, 9]


def check_fields(packet, lst_mac):
    details = ["0"] * 10
    details[0] = str(datetime.now().replace(microsecond=0))

    if packet.haslayer(scapy.IP):
        details[1] = packet[scapy.IP].src
        details[2] = packet[scapy.IP].dst
        details[5] = packet[scapy.IP].proto
        details[9] = packet[scapy.IP].len

    if details[5] in lst:
        details[5] = dict[details[5]]
    else:
        details[5] = "Other"

    if packet.haslayer(scapy.TCP):
        details[7] = packet[scapy.TCP].sport
        details[8] = packet[scapy.TCP].dport
        details[6] = packet[scapy.TCP].flags

        if details[6] in lst_flags:
            details[6] = dict_flags[details[6]]
        else:
            details[6] = str(details[6])

        if packet.haslayer(scapy.Raw):
            if b"\x00\x00\x00\x00" in packet[scapy.Raw].load:
                details[5] = "Modbus"
            elif b"\x05\x64" in packet[scapy.Raw].load:
                details[5] = "DNP3"

    if packet.haslayer(scapy.UDP):
        details[7] = packet[scapy.UDP].sport
        details[8] = packet[scapy.UDP].dport
        if packet.haslayer(scapy.Raw):
            if b"\x00\x00\x00\x00" in packet[scapy.Raw].load:
                details[5] = "Modbus"
            elif b"\x05\x64" in packet[scapy.Raw].load:
                details[5] = "DNP3"

    for d in lst_mac:
        if d["ip"] == details[1]:
            details[3] = d["mac"]
        elif d['ip'] == details[2]:
            details[4] = d["mac"]

    if details[3] == "0":
        new_entry = record_scan(details[1])
        details[3] = new_entry[0]["mac"]
        lst_mac.append(new_entry[0])
    if details[4] == "0":
        new_entry = record_scan(details[2])
        details[4] = new_entry[0]["mac"]
        lst_mac.append(new_entry[0])


    return [details[i] for i in select_param]


if __name__ == "__main__":
    check_fields(packet)
    show_fields(details)
