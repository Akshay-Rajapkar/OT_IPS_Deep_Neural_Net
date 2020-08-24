import csv

filename = "Baselines.csv"


with open(filename, 'r') as csvfile:
    write_rows = []
    csvreader = csv.reader(csvfile)
    fields = csvreader.next()
    for row in csvreader:
        write_rows.append(row)

test = ['2020-02-19 11:05:49', '10.0.2.3', '10.0.2.11', '08:00:27:d4:67:e3', '08:00:27:e5:f1:90', 'ICMP', '1', '0', '0']
print(test)

for entry in write_rows:
    for i in range(1, 9):
        if test[i] != entry[i]:
            break
    else:
        print("matched")
        break
else:
    print("not matched")