"""
A simple function comparing datetime objects.

Author: Amelia Litvak
Date:   September 27, 2025
"""
import datetime


def is_before(d1,d2):
    """
    Returns True if event d1 happens before d2.
    
    Values d1 and d2 can EITHER be date objects or datetime objects.
    If a date object, assume that it happens at midnight of that day. 
    
    Parameter d1: The first event
    Precondition: d1 is EITHER a date object or a datetime object
    
    Parameter d2: The first event
    Precondition: d2 is EITHER a date object or a datetime object
    """
    # HINT: Check the type of d1 or d2. If not a datetime, convert it for comparison
    d1type = type(d1)                    # Implement this function
    d2type = type(d2)

    if d1type == d2type:
        return d1 < d2
    elif d1type == datetime.datetime:
        return d1 < datetime.datetime(d2.year,d2.month,d2.day,0,0,0)
    else:
        return datetime.datetime(d1.year,d1.month,d1.day,0,0,0) < d2
    