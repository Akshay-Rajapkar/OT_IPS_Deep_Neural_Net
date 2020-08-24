import csv

filename = "new_Baselines.csv"


with open(filename, 'r') as csvfile:
    write_rows = []
    csvreader = csv.reader(csvfile)
    fields = csvreader.next()
    for row in csvreader:
        write_rows.append(row)

print(len(write_rows))

read_rows = []
with open("Baselines.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = csvreader.next()
    for row in csvreader:
        read_rows.append(row)

print(len(read_rows))

for alert_entry in read_rows:
    for entry in write_rows:
	for i in range(1, 9):
	    if alert_entry[i] != entry[i]:
		break
	else:
	    print("matched")


