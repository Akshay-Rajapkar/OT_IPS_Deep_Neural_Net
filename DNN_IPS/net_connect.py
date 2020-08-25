#!/usr/bin/env python
import netfilterqueue
import numpy as np
from joblib import load
from csv_operations import *
import scapy.all as scapy
from protocol import *
from net_scan import *

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    features = np.array(check_fields(scapy_packet,lst_mac))
    prob_pred = model.predict(features)
    packet_type = str(*class_label_pred.inverse_transform([np.argmax(prob_pred)]))
    write_data(details.append(packet_type))
    if packet_type == "Normal":
        packet.accept()
    else:
        write_alerts(details.append(packet_type))
        packet.drop()


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
# print("\n\n")
# print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
# print("Date & Time"+" "*13 +"Source IP"+" "*14 + "Destination IP"+" "*11 + "Source MAC"+" "*14 + "Destination MAC"+" "*9 + "Protocol"+"\t" +"Flags"+ " "*3 + "Src Port" +"\t" + "Dst Port"+ "\t" + "Length")
# print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

first_write()
model = load("DNN_model.joblib")
class_label_pred = load("dnn_le_pca.joblib")

lst_mac = record_scan("192.168.0.1/24")
try:
    queue.run()
except:
    pass
