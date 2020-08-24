import csv
rows = []


def write_csv(write_rows):
    with open('new_Baselines.csv', 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(write_rows)


def show_fields(details):
    space = [16-len(details[1]), 16-len(details[2]), 12-len(details[3]), 12-len(details[4]), 8-len(details[5]), 8-len(str(details[7])), 8-len(str(details[8])), 4-len(details[6])]
    print(details[0]+"\t"+details[1]+" "*space[0]+"\t"+details[2]+" "*space[1]+"\t"+ details[3]+"\t"+ details[4]+"\t"+ details[5]+" "*space[4]+"\t"+ details[6] + " "*space[7] + "\t" +str(details[7])+" "*space[5]+"\t" + str(details[8]) + " "*space[6] + "\t" + str(details[9]))
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")


def check_repeat(details):
    read_rows = []
    with open("Baselines.csv", 'r', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        for row in csvreader:
            read_rows.append(row)

    for entry in read_rows:
        for i in range(1, 9):
            if details[i] != entry[i]:
                break
        else:
            print("matched")
            break
    else:
        print("not matched")
        show_fields(details)
        write_csv([details])


def first_read(details):
    write_rows = [details]
    with open('Baselines.csv', 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(write_rows)
    show_fields(details)

