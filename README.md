# Design of Intrusion Prevention System for OT Networks using Deep Neural Network

## Introduction
  The Automation industries that uses Supervisory Control and Data Acquisition (SCADA) systems are
highly vulnerable for Network threats. Systems that are air-gapped and isolated from the internet are
highly affected due to insider attacks like Spoofing, DOS and Malware threats that affects confidentiality,
integrity and availability of system elements and degrade its performance even though security measures are
taken. In this paper, a behavior-based intrusion prevention system (IPS) is designed for OT networks. The
proposed system is implemented on SCADA test bed with two systems replicates automation scenarios in
industry. 
  This project describes 4 main classes of cyber-attacks with their subclasses against SCADA systems
and methodology with design of components of IPS system, database creation, Baselines and deployment of
system in environment. IPS system identifies not only IT protocols but also Industry Control System (ICS)
protocols Modbus and DNP3 with their inside communication fields using deep packet inspection (DPI).
The analytical results show 99.88% accuracy on binary classification and 97.95% accuracy on multiclass
classification of different attack vectors performed on network with low false positive rate. These results are
also validated by actual deployment of IPS in SCADA systems with the prevention of DOS attack.


## Dataset
  In SCADA communication, most of packets and control signals are repeated over a time and hence it
is essential to remove such duplicate entries from the database. A data cleaning operation is performed to
clean the database and unique set of communication is achieved as a Baselines of SCADA communication.
after comparing features of each entry and discarding duplicate traffic, the final database consist of 55998
normal data baselines and 49152 records corresponds to attack data.
 ![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)
 The protocol distribution of Normal and Malicious traffic shown in Fig. above.
 ![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)
 
 
 

## Deployment

Set IP tables before run

```bash
  sysctl net.ipv4.ip_forward=1
```
Connect in system's network
```bash
  sudo python3 connection.py
  sudo python3 net_connect.py
```
