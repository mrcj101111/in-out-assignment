import csv
from open_csv import CsvReadFile, CsvWriteFile
from add_column import addColumn
from add_entry import addEntry

class AmendCsv:

    #Create new variable which runs the function to open the csv file
    # to read from
    csv_read_file = csv.reader(CsvReadFile.read_file(CsvReadFile,'input.csv'))

    #Create new variable which runs the function to open the csv file
    # to write to
    csv_write_file = csv.writer(CsvWriteFile.write_file(CsvReadFile, 'new_output.csv'))

    #Take the title row and append 'Parsed' to it
    addColumn.add_title(addColumn, csv_read_file, csv_write_file)

    addEntry.add_entry(addEntry, csv_read_file, csv_write_file)
