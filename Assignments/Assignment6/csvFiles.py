import csv

OS = [["Mac OS", "10.6"], ["Windows", "10"], ["Android", "7"]]

with open("A:\\Python Projects\\Assignments\\Temp\\os.txt", "w", newline="") as file:
    writer = csv.writer(file, delimiter="|")
    writer.writerows(OS)

with open("A:\\Python Projects\\Assignments\\Temp\\os.txt", newline="") as file:
    reader = csv.reader(file, delimiter="|")
    for row in reader:
        print(row[0], row[1])