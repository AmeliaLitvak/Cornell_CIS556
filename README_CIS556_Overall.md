# Cornell CIS556: Python Data Processing and Flight School Auditing

## Overview

This repository contains three connected Python projects centered on
structured data, file processing, date/time computation, and a larger
flight-school auditing application.

The projects progress from reusable programming techniques for external
data and time calculations to an integrated command-line application
that analyzes multiple datasets and identifies flight lessons that
violate operating requirements.

## Project 1: Flight School Auditor

The Flight School Auditor is the primary application project. It
processes flight lessons together with student, instructor, aircraft,
weather, daylight, maintenance, and insurance-minimum data.

The completed core analyzes weather-related operating violations. For
each lesson, the program can determine factors such as pilot
certification, applicable minimums, VFR/IFR status, flight area,
instructor presence, day/night conditions, and weather at takeoff.

The application can identify violations involving:

-   visibility;
-   wind and crosswind conditions;
-   cloud ceiling; and
-   combinations of unsafe weather conditions.

It can also generate an annotated CSV report describing the detected
violations.

Major modules include `app.py`, `violations.py`, `pilots.py`,
`utils.py`, `__main__.py`, and `tests.py`. Optional modules describe
extensions for endorsement and aircraft inspection/maintenance
violations.

## Project 2: File Input/Output, CSV, JSON, and Path Handling

This project focuses on moving data between files and Python data
structures.

Exercises include:

-   counting lines in text files;
-   generating text-file output;
-   constructing cross-platform paths with `os.path`;
-   reading CSV files into two-dimensional lists;
-   writing two-dimensional lists to CSV;
-   reading JSON into Python lists and dictionaries; and
-   writing structured Python data back to formatted JSON.

The project provides the file-processing foundation needed by larger
applications that work with persistent datasets.

## Project 3: Date, Time, Time Zones, and Daylight Calculations

This project develops reusable utilities for temporal data.

Exercises include:

-   determining weekdays with `datetime.date`;
-   combining dates and times into ISO-formatted timestamps;
-   comparing `date` and `datetime` objects;
-   measuring elapsed time with `timedelta`;
-   parsing flexible timestamp strings;
-   handling invalid timestamp input;
-   assigning and preserving time zones;
-   reading sunrise and sunset information from nested JSON data; and
-   determining whether an event occurs during daylight hours.

The project uses `python-dateutil` and `pytz` in addition to Python's
standard `datetime` functionality.

## Repository Progression

Together, the three projects demonstrate a progression from reusable
data-handling utilities to integrated application development:

1.  External data is loaded from text, CSV, and JSON files.
2.  Structured data is represented with lists and dictionaries.
3.  Dates and timestamps are converted into objects that can be compared
    and calculated.
4.  Time zones and daylight information are incorporated into real-world
    decisions.
5.  Multiple datasets and helper modules are combined in the Flight
    School Auditor.
6.  Automated tests verify individual functions and application
    behavior.
7.  Results can be written back to CSV for further analysis.

## Key Concepts Demonstrated

-   Python file input/output
-   CSV processing
-   JSON parsing and serialization
-   Two-dimensional lists
-   Nested dictionaries
-   Cross-platform file paths
-   `datetime` programming
-   ISO 8601 timestamps
-   Time-zone handling
-   Sunrise and sunset calculations
-   Exception handling
-   Conditional logic and iteration
-   Data searching and filtering
-   Modular application design
-   Command-line arguments
-   Multi-dataset integration
-   Automated testing
-   Helper-function decomposition

## Technologies and Libraries

-   Python 3
-   Cornell `introcs`
-   Python `csv`
-   Python `json`
-   Python `datetime`
-   Python `os.path`
-   `python-dateutil`
-   `pytz`

## Author

Amelia Litvak
