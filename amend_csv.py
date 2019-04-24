import csv
from datetime import datetime


class AmendCsv:

    def __init__(self):
        self.input_file = None

    # Create function to open the csv file to read from
    def read_file(self, file_name):
        return csv.reader(open(file_name, 'r', newline=''))

    # Create function to open the csv file to write to
    def write_file(self, title, input_file_name, output_file_name):
        input_file = self.read_file(input_file_name)
        writer = csv.writer(open(output_file_name, 'w', newline=''))

        # Take the title row and append an extra title
        fields = next(input_file)
        fields.append(title)
        writer.writerow(fields)

        # For each row after the title row, add another entry
        for item in input_file:
            item.append(' ' + datetime.today().strftime('%Y-%m-%d %X'))
            writer.writerow(item)


if __name__ == "__main__":

    csv_parser = AmendCsv()
    csv_parser.write_file('Parsed', 'input.csv', 'new_output.csv')
