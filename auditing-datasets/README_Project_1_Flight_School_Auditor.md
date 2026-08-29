# Flight School Auditor

## Overview

This project implements a command-line auditing application for a flight
school's records. It processes flight lessons together with pilot,
weather, daylight, aircraft, instructor, maintenance, and
insurance-minimum datasets to identify flights that violate operating
requirements.

The completed core focuses on weather-related violations and
demonstrates CSV/JSON processing, nested data structures, date and time
calculations, time zones, file I/O, validation, testing, and modular
application design.

## Core Functionality

For each flight lesson, the application can determine the student's
certification level, applicable insurance minimums, day/night status,
VFR/IFR status, instructor presence, flight area, and weather conditions
at takeoff. It then checks visibility, wind, crosswind, and ceiling
conditions and can produce an annotated CSV report of violations.

## Project Modules

### `app.py`

Coordinates the audit. `discover_violations()` collects weather
violations, reports the number found, and optionally writes them to CSV.
`execute()` handles command-line arguments.

### `violations.py`

Implements the main weather-analysis logic, including visibility, wind,
crosswind, and cloud-ceiling checks. `get_weather_report()` finds the
observation associated with takeoff, using the most recent earlier
report when necessary. `get_weather_violation()` classifies results as
`Visibility`, `Winds`, `Ceiling`, `Weather`, `Unknown`, or no violation.
`list_weather_violations()` audits the lesson dataset.

### `pilots.py`

Determines pilot qualifications at the time of a flight and selects the
applicable insurance minimums. Minimums depend on certification level,
flight area, instructor presence, VFR/IFR status, and day/night
conditions.

### `utils.py`

Provides shared utilities for reading/writing CSV files, reading JSON,
converting timestamps to `datetime` objects, handling time zones,
determining daylight status, and looking up records by identifier.

### `__main__.py`

Provides the command-line entry point.

### `tests.py`

Contains tests for required project functionality.

### Optional Modules

`endorsements.py` and `inspections.py` describe optional extensions. The
endorsement extension covers solo status, aircraft endorsements, IFR
qualifications, and instructor qualifications. The inspection extension
covers annual inspections, 100-hour inspections, and aircraft
maintenance/repair status. These optional modules are included but are
not presented as completed core functionality.

## Data Files

-   `lessons.csv` --- flight lesson records.
-   `students.csv` --- student certification, rating, and endorsement
    information.
-   `minimums.csv` --- insurance-mandated operating minimums.
-   `weather.json` --- timestamped observations containing visibility,
    wind, crosswind, gusts, cloud layers, temperature, and weather
    conditions.
-   `daycycle.json` --- sunrise/sunset data used for day/night
    calculations.
-   `instructors.csv` --- instructor qualification records.
-   `fleet.csv` --- aircraft capability, endorsement, inspection, and
    hours information.
-   `repairs.csv` --- aircraft maintenance and repair records.

## Output

When an output filename is supplied, the application can generate a CSV
violation report containing student, airplane, instructor, takeoff,
landing, filed flight rules, area, and violation reason.

## Concepts Demonstrated

-   Modular Python programming
-   CSV and JSON processing
-   File input/output
-   Nested lists and dictionaries
-   Date/time and time-zone calculations
-   Data validation
-   Structured-data searching and filtering
-   Conditional logic and iteration
-   Exception handling
-   Command-line arguments
-   Multi-dataset integration
-   Testing and helper-function decomposition

## Requirements

-   Python 3
-   Cornell `introcs` package
-   Supplied project CSV and JSON datasets

## Author

Amelia Litvak
