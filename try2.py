import csv

filename = "Baselines.csv"


with open(filename, 'r') as csvfile:
    write_rows = []
    csvreader = csv.reader(csvfile)
    fields = csvreader.next()
    for row in csvreader:
        write_rows.append(row)

print(len(write_rows))
test = ['2020-02-18 12:11:39', '192.168.0.20', '192.168.0.50', '00:90:e8:5e:d1:66', '40:f2:e9:9d:44:6b', 'Modbus', '502', '54955', '1']
print(test)
lst = []


def test1(test):
    for entry in write_rows:
        count = 0
        for i in range(1, len(entry)):
            print(test[i], entry[i])
            if test[i] == entry[i]:
                count += 1
                
        if count == 8:
            print(test)
            #print("matched")
            break
    else:
        #print("not matched")
        pass
    print(test)

print(lst)
count1 = 0
for i in lst:
    if i ==8:
        count1 += 1
print(count1)

test1(test)