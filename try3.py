import csv

filename = "Baselines.csv"


with open(filename, 'r') as csvfile:
    write_rows = []
    csvreader = csv.reader(csvfile)
    fields = csvreader.next()
    for row in csvreader:
        write_rows.append(row)

print(len(write_rows))
print(type(write_rows))
l = len(write_rows)

for i in range(l):
    for j in range(i+1, l-1):
        count = 0
        for k in range(1,len(write_rows[i])):
            if write_rows[i][k] == write_rows[j][k]:
                count += 1
        if count == 8:
            print("matched")
            print(i,j)
            break