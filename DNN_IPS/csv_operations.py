import csv
rows = []
fields = ["Date & Time", "Source IP", "Destination IP", "Source MAC", "Destination MAC",
            "Protocol","Flags", "Src Port", "Dst Port", "Length"]


def first_write():
    with open('Alerts.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)

    with open('Data.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)

def write_alerts(write_rows):
    with open('Alerts.csv', 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(write_rows)

def write_data(write_rows):
    with open('Data.csv', 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(write_rows)


def show_fields(details):
    space = [16 - len(details[1]), 16 - len(details[2]), 12 - len(details[3]), 12 - len(details[4]), 8 - len(details[5]), 8 - len(str(details[7])), 8 - len(str(details[8])), 4 - len(details[6])]
    print(details[0] + "\t" + details[1] + " " * space[0] + "\t" + details[2] + " " * space[1] + "\t" + details[3] + "\t" + details[4] + "\t" + details[5] + " " * space[4] + "\t" + details[6] + " " * space[7] + "\t" + str(details[7]) + " " * space[5] + "\t" + str(details[8]) + " " * space[6] + "\t" + str(details[9]))
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
