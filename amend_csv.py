import csv
import argparse
from datetime import datetime


class AmendCsv:

    def __init__(self):
        self.input_file = None

    # Create function to open the csv file to read from
    def read_file(self, file_name):
        return csv.reader(open(file_name, 'r', newline=''))

    # Create function to open the csv file to write to
    def write_file(self, input_file_name, output_file_name):
        input_file = self.read_file(input_file_name)
        writer = csv.writer(open(output_file_name, 'w', newline=''))

        # Take the title row and append an extra title
        fields = next(input_file)
        fields.append('Parsed')
        writer.writerow(fields)

        # For each row after the title row, add another entry
        for item in input_file:
            item.append(' ' + datetime.today().strftime('%Y-%m-%d %X'))
            writer.writerow(item)


if __name__ == "__main__":

    # Parse file so that user can enter their input and output files in terminal
    parser = argparse.ArgumentParser()
    parser.add_argument("-input", action='store', dest="input", help="input filename", required=True)
    parser.add_argument("-output", action='store', dest="output", help="output filename", required=True)
    args = parser.parse_args()
    csv_parser = AmendCsv()
    csv_parser.write_file(args.input, args.output)
