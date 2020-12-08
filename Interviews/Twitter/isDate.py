# isDate(a, b, c)
# isDate(2020, 12, 1) -> true
# isDate(1, 2, 3) -> AMBIGUOUS

# generate perumations of the input (3! = 6)

import itertools

def isDate(a, b, c) -> int:
    
    # check all are defined
    if a is None or b is None or c is None:
        raise ValueError
    
    # check all are integers
    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        raise ValueError
    
    # check all are greater than 0
    if not (a > 0 and b > 0 and c > 0):
        raise ValueError
    
    permutations = itertools.permutations([a, b, c])
    
    validDates = 0
    
    for permutation in permutations:
        
        month = permutation[0]
        day = permutation[1]
        year = permutation[2]
        
        
        # This could be a constant, not initializing each time this method is called
        lastDayOfMonth = {}
        
        lastDayOfMonth[1] = 31
        lastDayOfMonth[2] = 28
        # ---
        lastDayOfMonth[12] = 31
        
        # Check if month is valid
        # if not (month <= 12):
        if month <= 12:
            continue
        
        isLeap = True if year % 4 == 0 else False
        
        # check day is valid
        # if on a leap year and month is February, check if day is within the special date range for Feb on a leap year
        if isLeap and month == 2:
            # special case
            if not (day <= 29):
                continue
        else:
            # normal case
            if not (day <= lastDayOfMonth[month - 1]):
                continue
                
        # if all checks passed
        validDates += 1
    
    return validDates

#valid years any positive integer 1 -> infinity?
#valid months 1 -> 12
#valid days 1 -> 31

# first identify months that are possible to choose (max 3)
# given a month choice, check if we can satisfy a date of that month with the unchosen inputs

# Choose a year last, (most forgiving)
# Check if last unchosen input is a valid year 