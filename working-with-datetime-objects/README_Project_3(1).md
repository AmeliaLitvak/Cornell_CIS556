# Project 3: Date, Time, Time Zones, and Daylight Calculations

## Overview

This project develops Python skills for working with dates and times
using the `datetime` module and related libraries. The exercises
progress from basic `date`, `time`, and `datetime` operations to
timestamp parsing, elapsed-time comparisons, time-zone handling, and
sunrise/sunset calculations based on structured JSON data.

The resulting functions provide reusable date/time utilities that
support larger data-processing applications.

## Project Components

### Date and Datetime Fundamentals

The project implements `christmas_day(year)` to determine the ISO
weekday number for Christmas in a given year and `iso_str(d, t)` to
combine separate date and time objects into an ISO-formatted timestamp
with microsecond precision.

### Comparing Dates and Times

`is_before(d1, d2)` compares two events and returns whether the first
occurs before the second. The function accepts either `date` or
`datetime` objects and treats a plain date as midnight when it must be
compared with a datetime.

### Measuring Elapsed Time

`past_a_week(d1, d2)` determines whether the second event occurs at
least seven days after the first. It uses `datetime.timedelta` and
supports combinations of `date` and `datetime` values.

### Parsing Timestamps

`str_to_time(timestamp)` uses `dateutil.parser.parse` to convert textual
timestamps into Python `datetime` objects. Invalid timestamps are
handled with exception handling and return `None` rather than
terminating the program.

The later version of `str_to_time(timestamp, tzsource=None)` extends
this functionality with time-zone support. It preserves time zones
already present in timestamps and can assign a time zone from either a
named zone or another datetime object.

### Sunrise and Sunset Data

The project uses `daycycle.json`, a structured dataset containing
sunrise and sunset times by year and calendar date. The dataset also
identifies the applicable time zone.

`sunset(date, daycycle)` looks up the sunset for a given date,
constructs an ISO timestamp, and converts it into a datetime object.
Missing data returns `None`.

### Daylight Determination

`daytime(time, daycycle)` determines whether a supplied datetime occurs
after sunrise and before sunset. It combines nested-dictionary lookup,
timestamp construction, date/time parsing, and time-zone handling.

This functionality is tested across multiple years, seasons, and time
zones.

## Testing

The supplied automated tests verify:

-   ISO weekday calculations for Christmas across multiple years;
-   ISO formatting with and without microseconds;
-   comparisons between `date` and `datetime` objects;
-   seven-day elapsed-time boundaries;
-   valid and invalid timestamp parsing;
-   sunrise/sunset lookups from JSON data;
-   missing-year handling;
-   timestamps with explicit time-zone offsets;
-   assignment of time zones to naive timestamps; and
-   daylight calculations in New York and Chicago time zones.

Tests use Cornell's `introcs` assertion utilities together with Python's
`datetime`, `json`, and `os.path` modules.

## Data File

### `daycycle.json`

The supporting JSON dataset contains location and time-zone information
along with daily sunrise and sunset times organized by year and `MM-DD`
keys. The project uses this nested structure to perform real date/time
calculations rather than relying only on hard-coded examples.

## Concepts Demonstrated

-   Python `datetime` objects
-   `date`, `time`, and `datetime` classes
-   ISO weekday calculations
-   ISO 8601 formatting
-   Comparing dates and timestamps
-   `datetime.timedelta`
-   Elapsed-time calculations
-   Timestamp parsing
-   Exception handling
-   Time-zone-aware and naive datetimes
-   `python-dateutil`
-   `pytz`
-   Nested JSON data
-   Sunrise and sunset lookup
-   Daylight calculations
-   Automated testing
-   Boundary-condition testing

## Requirements

-   Python 3
-   Cornell `introcs` package
-   `python-dateutil`
-   `pytz`
-   Python standard-library modules:
    -   `datetime`
    -   `json`
    -   `os.path`

## Author

Amelia Litvak
