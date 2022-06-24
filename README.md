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
