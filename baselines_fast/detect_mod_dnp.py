import netfilterqueue
import scapy.all as scapy
import subprocess


def process_packet(packet):
    #print(packet)
    hw_addr = packet.get_hw()
    hw_addr1 = packet.get_hw()
    if hw_addr:
        #print(type(hw_addr))
        #print(hw_addr)
        #print(hw_addr1)
        #print(":".join("{:02x}".format(ord(c)) for c in hw_addr[0:6]))
        #print(":".join("{:02x}".format(ord(c)) for c in hw_addr[6:]))
        #print("\n\n")
        pass
    scapy_packet = scapy.IP(packet.get_payload())
    #print(scapy_packet.show())
    size = scapy_packet[scapy.IP].len
    #print(size, type(size))

    if scapy_packet.haslayer(scapy.TCP):
        flag = scapy_packet[scapy.TCP].flags
        #print(flag, type(flag))
        if scapy_packet.haslayer(scapy.Raw):
            load = scapy_packet[scapy.Raw].load
            #print(str(load),"\t", type(load))
            if (scapy_packet[scapy.IP].src == "192.168.0.5") and (b"\x05\x64" in scapy_packet[scapy.Raw].load):
                print("packet")
                print(scapy_packet.show())
    packet.accept()

subprocess.call(["sudo", "iptables", "-I", "FORWARD", "-j", "NFQUEUE", "--queue-num", "0"])
queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
try:
    queue.run()
except:
    subprocess.call(["sudo", "iptables", "-F"])
