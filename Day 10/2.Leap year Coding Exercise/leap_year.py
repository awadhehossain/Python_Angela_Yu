def is_leap_year(year):
    """Hi my name is"""
    
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True

    else:
        return False

output=is_leap_year(int(input("Type a year for leap year check:\n")))
print(output)