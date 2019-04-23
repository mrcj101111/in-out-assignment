import csv
from datetime import datetime
from open_csv import CsvReadFile, CsvWriteFile

class AmendCsv:

    #Create new variable which runs the function to open the csv file
    # to read from
    csv_read_file = csv.reader(CsvReadFile.read_file(CsvReadFile,'input.csv'))

    #Create new variable which runs the function to open the csv file
    # to write to
    csv_write_file = csv.writer(CsvWriteFile.write_file(CsvReadFile, 'new_output.csv'))

    #Take the title row and append 'Parsed' to it
    fields = next(csv_read_file)
    fields.append('Parsed')
    csv_write_file.writerow(fields)

    #For each row after the title row, add another entry under the parsed 
    # column that displays the date and time
    for item in csv_read_file:
        item.append(' ' + datetime.today().strftime('%Y-%m-%d %X'))
        csv_write_file.writerow(item)
