class addColumn:

    #Take the title row and append an extra title
    def add_title(self, read_file, write_file):
        fields = next(read_file)
        fields.append('Parsed')
        write_file.writerow(fields)