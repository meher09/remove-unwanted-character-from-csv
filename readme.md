# Remove Unwanted Character from CSV File

This Python-based GitHub repository contains a comprehensive utility script for removing unwanted characters from CSV (Comma Separated Values) files.

The script provides a combination of several important functions to ensure CSV data is clean and ready for further processing.

## Key Features

1. **Byte Order Mark (BOM) Removal:** Byte Order Marks, often seen in text files encoded in UTF-8, can cause unexpected behavior when reading data. This script effectively identifies and removes these characters if they're present in the file.

2. **Character Encoding Detection:** Leveraging the `chardet` library, the script automatically detects the character encoding of the input file to ensure accurate reading of data.

3. **Text Problem Fixing:** With the help of the `ftfy` (fixes text for you) library, the script handles and resolves common issues in text data, like mojibake (incorrectly encoded text), and various forms of data corruption.

4. **Unicode Normalization:** Utilizing the `unicodedata` library, the script normalizes the Unicode characters in the CSV file to their canonical form (NFC), maintaining data consistency.

5. **ASCII Transliteration:** The `unidecode` library is used to transliterate special, non-ASCII characters to their closest ASCII counterparts. This ensures that data can be accurately represented even in environments that only support ASCII characters.


## Installation

To successfully run this script, you will need to install several Python libraries. You can do this using the package installer `pip`.

Open your terminal and type the following commands:

```sh
pip install chardet
pip install ftfy
pip install unidecode
```
Please note that the csv and unicodedata libraries are part of Python's standard library and do not need to be installed separately.

Please note that Python's `pip` command can install multiple packages at once. This can be done by separating package names with a space. Here is an example of how to do it:

```sh
pip install chardet ftfy unidecode
```
## Usage

This script is designed to be flexible and easy to use. To process your CSV file, you'll need to specify the input and output file names directly in the script.

The section to modify is at the bottom of the script:

```python
if __name__ == "__main__":
    input_file_name = "person.csv" # replace with your input file name
    output_file_name = "formatted_person.csv" # replace with your desired output file name

    remove_bom(input_file_name, output_file_name)
```