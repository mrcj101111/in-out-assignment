import csv

with open('input.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    line_count = 0
    for row in csv_reader:
        print(row)
        
csv_file.close()