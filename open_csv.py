import csv

class CsvReadFile:

    #Open csv file to read data from
    def read_file(self, file_name):
        return open(file_name, 'r')

class CsvWriteFile:
    #Open csv file to write data to
    def write_file(self, file_name):
        return open(file_name, 'w', newline='')