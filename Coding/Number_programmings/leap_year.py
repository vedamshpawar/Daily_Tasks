def leap_year(year):
    if (year % 100 != 0 and year % 4 == 0) or (year % 400 == 0):
        return f'{year} is leap year'
    else:
        return f'{year} is not leap year'

year = int(input('enter a year: '))
print(leap_year(year))