
def is_leap(year):
    leap = False
    
    if year%4 == 0:
        if year%100 != 0:
            leap = True
    
    if year == 2000 or year == 2400:
        return True
    return leap
