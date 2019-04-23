from datetime import datetime

class addEntry:
    #For each row after the title row, add another entry 
    def add_date(self, read_file, write_file):
        for item in read_file:
            item.append(' ' + datetime.today().strftime('%Y-%m-%d %X'))
            write_file.writerow(item)