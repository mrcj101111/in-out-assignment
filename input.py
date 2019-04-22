import csv
from datetime import datetime

with open('input.csv', 'r') as csv_file:
    with open('new_output.csv', 'w') as csv_output:
        writer = csv.writer(csv_output, delimiter=';', quoting=csv.QUOTE_NONE, escapechar=' ')
        reader = csv.reader(csv_file, skipinitialspace=True)

        fields = next(reader)
        fields.append('Parsed')
        writer.writerow(fields)

        for item in reader:
            item.append(datetime.today().strftime('%Y-%m-%d'))
            writer.writerow(item)



