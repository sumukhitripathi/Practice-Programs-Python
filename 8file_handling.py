# File input and output

import csv

with open("input.txt", "r") as file_ip:
    lines = [line.strip().split(',') for line in file_ip]
    print("Input File:\n", lines)

with open("output.csv", "w") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(lines)

with open("output.csv", "r") as op:
    reader = csv.reader(op)
    print("Output File:\n", op.read())