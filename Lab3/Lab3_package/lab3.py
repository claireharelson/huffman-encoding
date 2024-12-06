# This script takes input and output files in to process
from sys import stderr
from time import time_ns
from typing import TextIO

from Lab3_package.runtime_metrics import RuntimeMetric
from Lab3_package.huffman import huffman_tree
from Lab3_package.huffman import merge_items
from Lab3_package.huffman import encode
from Lab3_package.huffman import decode
from Lab3_package.heap import Heap


def frequency_table(input_file: TextIO):
    """
    Creates a heap from an input file containing a frequency table
    input_file: an opened text file set to read mode
    """
    next_line = input_file.readline()
    frequency_list = []
    frequency_heap = Heap()

    while next_line is not None and next_line != "":
        try:
            value = str(next_line.strip())
            if len(value) == 5:
                new_value = f'{value[0]}{value[4]}'
                frequency_list.append(new_value)
            else:
                new_value = f'{value[0]}{value[4:]}'
                frequency_list.append(new_value)
        except ValueError:
            print(f'Error parsing {next_line} for string', file=stderr)
            continue
        finally:
            next_line = input_file.readline()

    for item in frequency_list:
        frequency_heap.insert(item)
    new_heap = frequency_heap.traverse()
    new_nodes = [('blank', 0)]
    for node in new_heap:
        if len(node) == 8:
            new_nodes.append((node[2], int(node[6])))
        else:
            new_nodes.append((node[2], int(node[6] + node[7])))

    merged = merge_items(new_nodes[1:])
    huffman_tree(merged)


def encode_string(value: str) -> (str, RuntimeMetric):
    """
    Converts a clear text string into an encoded string
    value: clear text string to convert
    return: metrics on algorithm performance and encoded string
    """
    start_time = time_ns()
    encoded_string = encode(value.upper())
    end_time = time_ns()
    metric = RuntimeMetric(len(value), end_time - start_time)
    return encoded_string, metric


def decode_string(value: str) -> (str, RuntimeMetric):
    """
    Converts an encoded string into a decoded clear text string
    value: encoded string to convert
    return: metrics on algorithm performance and decoded clear text string
    """
    start_time = time_ns()
    decoded_string = decode(value)
    end_time = time_ns()
    metric = RuntimeMetric(len(value), end_time - start_time)
    return decoded_string, metric


def process_encoded_files(input_file: TextIO, output_file: TextIO) -> None:
    """
    Reads encoded values from an input file and writes them as clear text values to an output file
    input_file: an opened text file set to read mode
    output_file: an opened text file set to write mode
    """
    total_conversions = 0
    metrics = []
    next_line = input_file.readline()

    while next_line is not None and next_line != "":
        try:
            value = str(next_line)
        except ValueError:
            print(f'Error parsing {next_line} for string', file=stderr)
            continue
        finally:
            next_line = input_file.readline()

        output_string, runtime_metric = decode_string(value)
        output_file.write(str(output_string))
        output_file.write('\n')
        metrics.append(runtime_metric)
        total_conversions += 1

    output_file.write("\n")
    for metric in metrics:
        output_file.write(f"Statement of size {metric.get_size()} took {metric.get_runtime()}ns to decode.\n")


def process_decoded_files(input_file: TextIO, output_file: TextIO) -> None:
    """
    Reads clear text values from an input file and writes them as encoded values to an output file
    input_file: an opened text file set to read mode
    output_file: an opened text file set to write mode
    """
    total_conversions = 0
    metrics = []
    next_line = input_file.readline()

    while next_line is not None and next_line != "":
        try:
            value = str(next_line)
        except ValueError:
            print(f'Error parsing {next_line} for string', file=stderr)
            continue
        finally:
            next_line = input_file.readline()

        output_string, runtime_metric = encode_string(value)
        output_file.write(str(output_string))
        output_file.write('\n')
        metrics.append(runtime_metric)
        total_conversions += 1

    output_file.write("\n")
    for metric in metrics:
        output_file.write(f"Statement of size {metric.get_size()} took {metric.get_runtime()}ns to encode.\n")
