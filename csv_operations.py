import csv
rows = []


def initialize():
    read_baselines = []
    with open("Baselines.csv", 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = csvreader.next()
        for row in csvreader:
            read_baselines.append(row)
    return read_baselines


def write_csv(write_rows):
    with open('Alerts.csv', 'a') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(write_rows)


def show_fields(details):
    space = [16-len(details[1]), 16-len(details[2]), 12-len(details[3]), 12-len(details[4]), 8-len(details[5]), 8-len(str(details[6]))]
    print(details[0]+"\t"+details[1]+" "*space[0]+"\t"+details[2]+" "*space[1]+"\t"+ details[3]+"\t"+ details[4]+"\t"+ details[5]+" "*space[4]+"\t"+ str(details[6])+" "*space[5]+"\t"+ str(details[7]))
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")


def check_repeat(details):
    read_rows = []
    with open("Baselines.csv", 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = csvreader.next()
        for row in csvreader:
            read_rows.append(row)

    for entry in read_rows:
        for i in range(1, 9):
            if details[i] != entry[i]:
                break
        else:
            print("matched")
            return True
    else:
        print("not matched")
        show_fields(details)
        write_csv([details])
        return False


def first_read(details):
    write_rows = [details]
    with open('Baselines.csv', 'a') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(write_rows)
    show_fields(details)

