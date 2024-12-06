# Lab 3

This python package is designed to carry out Huffman encoding and decoding.


* Pycharm IDE was used for running this package, information as follows:

PyCharm 2022.3.2 (Community Edition)
Build #PC-223.8617.48, built on January 24, 2023
Runtime version: 17.0.5+1-b653.25 x86_64
VM: OpenJDK 64-Bit Server VM by JetBrains s.r.o.
macOS 13.2
GC: G1 Young Generation, G1 Old Generation
Memory: 1024M
Cores: 8
Metal Rendering is ON
Non-Bundled Plugins:
    com.leinardi.pycharm.pylint (0.14.0)

* A Macintosh operating system Ventura 13.2 was used.


## Running Lab3

1. Download and install python on your computer
2. Run the program in the terminal as a module: python -m Lab3_package <frequency table file> <encoded file> 
           <clear text file> <output file>


### Lab3 Usage:

usage: python -m lab3 [-h] frequency_table_file encoded_file cleartext_file output_file

positional arguments:
  frequency_table_file     Frequency Table File Pathname
  encoded_file             Encoded File Pathname
  cleartext_file           Clear Text File Pathname
  output_file              Output File Pathname

* make sure input file paths are correct to successfully run the program. Will be located ~/Lab3/Lab3_package/<input>

optional arguments:
  -h, --help  show this help message and exit


## Project Layout:

- Lab3/: The parent folder holding all the project files
  - README: This guide the user is currently reading. Explains package usage
  - Lab3_package: The main module within the package
    - __init__.py: Used to show what functions, variables, classes, etc are exposed when scripts import this module.
    - __main__.py: The entrypoint to the program when ran as a program. 
    - runtime_metrics.py: Creates a class to measure runtime metrics
    - lab3.py: Defines functions to take input and output files to process as well as conduct the encoding and decoding
    - heap.py: Creates a min heap object to organize the frequency table
    - huffman.py: Defines functions to create a huffman encoding tree 
