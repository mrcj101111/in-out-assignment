import csv
from datetime import datetime

#Open csv file to read data from
with open('input.csv', 'r') as csv_file:
    #Open csv file to write new data to
    with open('new_output.csv', 'w') as csv_output:
        writer = csv.writer(csv_output, delimiter=';', quoting=csv.QUOTE_NONE,
        escapechar=' ')
        reader = csv.reader(csv_file, skipinitialspace=True)

        #Take the title row and append 'Parsed' to it
        fields = next(reader)
        fields.append('Parsed')
        writer.writerow(fields)

        #For each row after the title row, add another entry under the parsed 
        # column that displays the date and time
        for item in reader:
            item.append(datetime.today().strftime('%Y-%m-%d %X'))
            writer.writerow(item)
