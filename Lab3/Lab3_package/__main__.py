# This module is used to process command line arguments and launch the program
from pathlib import Path
import argparse
import Lab3_package

# Create the parser
arg_parser = argparse.ArgumentParser()

# Add an argument to the parser
arg_parser.add_argument("input_freq_table", type=str, help="Input Frequency Table File Pathname")
arg_parser.add_argument("input_encoded", type=str, help="Input Encoded File Pathname")
arg_parser.add_argument("input_decoded", type=str, help="Input Decoded File Pathname")
arg_parser.add_argument("output_file", type=str, help="Output File Pathname")

# Parse the argument
args = arg_parser.parse_args()

# pathlib.Path
freq_table_path = Path(args.input_freq_table)
encoded_path = Path(args.input_encoded)
decoded_path = Path(args.input_decoded)
out_path = Path(args.output_file)

# Raises error if the input file's path or name is incorrect
try:
    with freq_table_path.open('r') as input_file:
        Lab3_package.frequency_table(input_file)
except FileNotFoundError:
    print(f'FILE NAME "{freq_table_path}" NOT FOUND. CHECK INPUT FILE NAME OR PATH.')


try:
    with encoded_path.open('r') as input_file, out_path.open('w') as output_file:
        Lab3_package.process_encoded_files(input_file, output_file)
except FileNotFoundError:
    print(f'FILE NAME "{encoded_path}" NOT FOUND. CHECK INPUT FILE NAME OR PATH.')

try:
    with decoded_path.open('r') as input_file, out_path.open('w') as output_file:
        Lab3_package.process_decoded_files(input_file, output_file)
except FileNotFoundError:
    print(f'FILE NAME "{decoded_path}" NOT FOUND. CHECK INPUT FILE NAME OR PATH.')
