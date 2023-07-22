import csv
import chardet
import ftfy
import unicodedata
from unidecode import unidecode

def remove_bom(input_filename, output_filename):
    # Detect the file encoding using chardet
    with open(input_filename, 'rb') as input_file:
        rawdata = input_file.read()
        bom_encoding = chardet.detect(rawdata)['encoding']

    with open(input_filename, 'r', encoding=bom_encoding) as input_file:
        # Read the CSV file and skip the header row
        csv_reader = csv.reader(input_file)
        header = next(csv_reader)

        # Remove the BOM from the header if present
        if header[0].startswith('\ufeff'):
            header[0] = header[0][1:]

        # Create a new CSV file with the formatted data
        with open(output_filename, 'w', newline='', encoding='utf-8') as output_file:
            csv_writer = csv.writer(output_file)
            csv_writer.writerow(header)

            # Write the remaining rows to the new CSV file
            for row in csv_reader:
                # Apply ftfy to fix any common text problems
                row = [ftfy.fix_text(cell) for cell in row]

                # Apply Unicode normalization (NFC) to the data
                row = [unicodedata.normalize('NFC', cell) for cell in row]

                # Use unidecode to transliterate special characters to ASCII
                row = [unidecode(cell) for cell in row]

                csv_writer.writerow(row)

if __name__ == "__main__":
    input_file_name = "person.csv"
    output_file_name = "formatted_person.csv"

    remove_bom(input_file_name, output_file_name)
