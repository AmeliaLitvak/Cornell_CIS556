"""
A simple function computing time elapsed

Author: Amelia Litvak
Date:   September 27, 2025
"""
import datetime


def past_a_week(d1,d2):
    """
    Returns True if event d2 happens at least a week (7 days) after d1.
    
    If d1 is after d2, or d2 is less than a week after d1, this function returns False.
    Values d1 and d2 can EITHER be date objects or datetime objects.  If a date object,
    assume that it happens at midnight of that day. 
    
    Parameter d1: The first event
    Precondition: d1 is EITHER a date object or a datetime object
    
    Parameter d2: The second event
    Precondition: d2 is EITHER a date object or a datetime object
    """
    # HINT: Check the type of d1 or d2. If not a datetime, convert it for comparison
    d1type = type(d1)                    # Implement this function
    d2type = type(d2)

    if d1type == d2type:
        return d2 - d1 >= datetime.timedelta(weeks=1)
    elif d1type == datetime.datetime:
        return datetime.datetime(d2.year,d2.month,d2.day,0,0,0) - d1 >= datetime.timedelta(weeks=1)
    else:
        return d2 - datetime.datetime(d1.year,d1.month,d1.day,0,0,0) >= datetime.timedelta(weeks=1)
