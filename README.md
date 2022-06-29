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
 ## image1
 The protocol distribution of Normal and Malicious traffic shown in Fig. above.
 ## image2
 
 
## Binary classification evaluation metrics
  The designed DNN model is evaluated on test set. Accuracy, Sensitivity, Recall, Specificity, precision, f1-
score are the metrics used to check the effectiveness of proposed intrusion prevention model on real SCADA
data as discussed in below Table. The 70% data points are used for training model and 30% data points use
for testing and validating model performance.

| Precision | Recall    | TPR | FPR | F1-score |
| :-------- | :------- | :--- |:--- |:-------- |
| 100       | 99.75    | 99.75| 0.24| 99.98    |

Proposed model able to classify normal and malicious traffic with accuracy of 99.89% with low false
positive rate (FPR) indicates that less probability of misclassification of malicious traffic as normal

## Multi-class classification evaluation metrics
  The same model is trained and tested for different classes of attacks gives accuracy of 97.95% and all
evaluation metrics for each class is explain in Table.

| Classess               | Precision | Recall | F1-score |
| :--------------------- | :-------- | :----- |:-------- |
| Normal                 | 100       | 98     | 99       |
| DOS Modbus flooding    | 90        | 98     | 94       |
| DOS UDP scan           | 97        | 91     | 94       |
| MITM                   | 97        | 100    | 98       |
| Malware stealth scan   | 99        | 99     | 99       |
| Ping scan              | 100       | 100    | 100      |
| UDP port & service scan| 100       | 97     | 98       |


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
