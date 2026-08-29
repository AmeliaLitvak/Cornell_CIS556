# Project 2: File Input/Output, CSV, JSON, and Path Handling

## Overview

This project explores how Python programs read, write, and organize data
stored in external files. It progresses from basic text-file operations
to structured CSV and JSON data, while also demonstrating portable
file-path construction with `os.path`.

The exercises emphasize an important programming skill: moving data
between files and Python data structures so that it can be processed by
larger applications.

## Project Components

### Text File Input and Output

The project includes functions for basic text-file processing:

-   `count_lines(filepath)` opens a text file and counts the number of
    lines it contains.
-   `write_numbers(filepath, n)` creates a text file containing the
    numbers from `0` through `n-1`, with one number per line.

These exercises demonstrate opening files in read and write modes,
iterating through file contents, converting values to strings, and
properly closing files.

### Cross-Platform File Paths

The project demonstrates use of Python's `os.path` module to construct
file paths that work across Windows, macOS, and Linux.

The `read_file(directory, file)` example uses `os.path.join()` instead
of manually inserting directory separators. This allows the same code to
work on operating systems that represent paths differently.

### CSV File Processing

CSV data is represented in Python as a two-dimensional list, where each
nested list represents one row.

The project implements:

-   `read_csv(filename)` to read a CSV file into a 2D Python list.
-   `write_csv(data, filename)` to write a 2D list to a CSV file.

Because CSV files do not preserve Python type information, values read
from CSV files are initially represented as strings. Supporting examples
demonstrate how numeric data can be converted when necessary.

### JSON File Processing

The project also works with JSON, which can preserve structured data
such as dictionaries, lists, strings, numbers, booleans, and null
values.

The implemented functions are:

-   `read_json(filename)` to load JSON data and convert it into the
    corresponding Python data structure.
-   `write_json(data, filename)` to serialize Python data into a JSON
    file.

JSON output is formatted with four-space indentation to make the
resulting files easier to read.

### Structured and Nested Data

The supplied JSON files demonstrate several levels of structured data,
including dictionaries containing other dictionaries and lists. Weather
data is used as an example of a larger real-world dataset containing
timestamps, visibility, wind, temperature, sky conditions, weather
conditions, and observation codes.

This illustrates why JSON is useful for representing complex
hierarchical information that would be difficult to express in a simple
text or CSV file.

## Testing

The project includes automated test scripts that verify the
file-processing functions.

Tests check that:

-   text files contain the expected number of lines;
-   generated text files exactly match expected output;
-   CSV files are correctly converted to 2D lists;
-   written CSV files match reference files;
-   JSON files are correctly converted into Python values;
-   written JSON data matches the expected structure and indentation;
    and
-   output files are successfully created.

The tests use Cornell's `introcs` assertion functions as well as
`os.path` for locating supporting files relative to the test scripts.

## Data Files

Supporting files include examples used to test reading and writing
operations, including:

-   plain-text input and expected-output files;
-   CSV datasets and expected CSV output;
-   small JSON dictionaries and lists;
-   nested JSON structures; and
-   a larger weather dataset used to demonstrate realistic hierarchical
    data.

These files provide test cases for moving information between persistent
storage and Python's built-in data structures.

## Concepts Demonstrated

-   File input and output
-   Reading and writing text files
-   File iteration
-   File paths and directories
-   Cross-platform path construction with `os.path`
-   CSV parsing with Python's `csv` module
-   Two-dimensional lists
-   CSV serialization
-   JSON parsing with Python's `json` module
-   JSON serialization
-   Dictionaries and nested data structures
-   Lists stored in JSON
-   Data type conversion
-   File-based automated testing
-   Resource management and closing files

## Requirements

-   Python 3
-   Cornell `introcs` package
-   Python standard-library modules:
    -   `os.path`
    -   `csv`
    -   `json`

## Author

Amelia Litvak
