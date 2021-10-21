# !/usr/bin/env python3


''' template for ops435 assignment 1 script
    put your script level docstring here...
    you can have more than one line of docstring.
    Please personlize the following author declaration:
-----------------------------------------------------------------------
OPS435 Assignment 1 - Winter 2021
Program: a1_[Seneca_name].py (replace [Seneca_name] with your Seneca User name)
Author: "Esrak Fahim"
The python code in this file (a1_[Seneca_name].py) is original work written by
"Esrak Fahim". No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading.
I understand that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.
'''

import os
import sys


def leap_year(obj):

    '''
    The leap_year(obj) function will take a year in 4-digit 'YYYY' format.
    It will return True if given year is a leap year.
    '''
    ...

    if obj % 400 == 0:
	return True
    elif obj % 100 == 0:
	return False
    elif obj % 4 == 0:
	return True
    else:
	return False
    
    return status

def sanitize(obj1,obj2):
  
  '''
    The sanitize(obj1, obj2) function will take two string objects
    The first string object is the object to be sanitized,
    and the 2nd string object contains characters that are allowed.
    '''
    ...

    san = ''
    for i in range(len(obj1)):
        if obj1[i] in obj2:
            san = san + obj1[i]
    return san
    return results


def size_check(obj, intobj):
    '''
    The size_check(obj, introbj) function will take a collection data type
    object and the expected number of items as an integer in this order and
    it will return 'True' or 'False' after it is called.
    '''
    ...

    if len(obj) == intobj:
        status = True
    else:
        status = False

    return status


def range_check(obj1, obj2):
    '''
    The range_check(obj2, obj2) function will take an integer
    object (e.g. year) and a tuple with 2 integer values respectively.
    Regarding tuples, the first value indicates the lower bound and
    the second one indicates the upper bound of an integer range.
    '''
    ...

    if obj2 == (1900, 9999):
        if obj1 in range(1900, 9999):
            return True
    else:
        return False

    elif obj2 == (1, 12):
        if obj1 in range(1, 13):
            return True
        else:
            return False

    elif month == 1:
        if obj2 == (1, 31):
            if obj1 in range(1, 32):
                return True
            else:
                return False

    elif month == 2:
        if leap_year(year):
            if obj1 in range(1,30):
                return True
            else:
                return False
        else:
            if obj1 in range (1,29):
                return True
            else:
                return False

    elif month == 3:
        if obj2 == (1,31):
            if obj1 in range (1,32):
                return True
            else:
                return False

    elif month == 4:
        if obj2 == (1,30):
            if obj1 in range (1,31):
                return True
            else:
                return False

    elif month == 6:
        if obj2 == (1,30):
            if obj1 in range (1,31):
                return True
            else:
                return False

    elif month == 7:
        if obj2 == (1,31):
            if obj1 in range (1,32):
                return True
            else:
                return False


    elif month == 8:
        if obj2 == (1,31):
            if obj1 in range (1,32):
                return True
            else:
                return False

    elif month == 9:
        if obj2 == (1,30):
            if obj1 in range (1,31):
                return True
            else:
                return False


    elif month == 10:
        if obj2 == (1,31):
            if obj1 in range (1,32):
                return True
            else:
                return False


    elif month == 11:
        if obj2 == (1,30):
            if obj1 in range (1,31):
                return True
            else:
                return False


    elif month == 12:
        if obj2 == (1,31):
            if obj1 in range (1,32):
                return True
            else:
                return False

    return status


def usage():
    '''
    The usage() function will be called (and displayed to the standard input)
    when the command line arguments are not equal to 2.
    '''
    ...
    status = "Usage: a1_emfahim.py YYYYMMDD|YYYY/MM/DD|YYYY-MM-DD|YYYY.MM.DD"

    return status


if __name__ == "__main__":
    # step 1
    if len(sys.argv) != 2:
        print(usage())
        sys.exit()
    # step 2
    month_name = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                  'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    days_in_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
                     7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    user_raw_data = sys.argv[1]
    # step 3
    allow_chars = '0123456789'
    dob = sanitize(user_raw_data, allow_chars)
    print('Sanitized user data:', dob)
    # setp 4
    result = size_check(dob, 8)
    if result == False:
        print("Error 09: wrong data entered")
        sys.exit()
    # step 5
    year = int(dob[0:4])
    month = int(dob[4:6])
    day = int(dob[6:])
    # step 6
    result = range_check(year, (1900, 9999))
    if result == False:
        print("Error 10: year out of range, must be 1900 or later")
        sys.exit()
    result = range_check(month, (1, 12))
    if result == False:
        print("Error 02: Wrong month entered")
        sys.exit()
    result = leap_year(year)
    if result == True:
        days_in_month[2] = 29
    result = range_check(day, (1, days_in_month[month]))
    if result == False:
        print("Error 03: wrong day entered")
        sys.exit()
    # step 7
    new_dob = str(month_name[month - 1]) + ' ' + str(day) + ', ' + str(year)
    # step 8
    print("Your date of birth is:", new_dob)
