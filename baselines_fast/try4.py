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
repeat = []
for i in range(l):
    for j in range(i+1, l-1):
        count = 0
        for k in range(1,len(write_rows[i])):
            if write_rows[i][k] == write_rows[j][k]:
                count += 1
        if count == 8:
            repeat.append(j)


repeat= sorted(repeat)
repeat = list(set(repeat))
print(len(repeat))

for i in range(len(write_rows)):
    if i not in repeat:
        with open('unique.csv', 'a') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows([write_rows[i]])

unique_rows = []
with open("unique.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        unique_rows.append(row)

print(len(unique_rows))
l1 = len(unique_rows)
for i in range(l1):
    for j in range(i+1, l1-1):
        count = 0
        for k in range(1,len(unique_rows[i])):
            if unique_rows[i][k] == unique_rows[j][k]:
                count += 1
        if count == 8:
            print("matched")
