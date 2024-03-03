# This is a python program to take a year from a user and show if the year is a leap year or not
# for a year to be a leap year, it should be excatly divisible by 4 but not exactly divisble by 100 but are exactly divisble by 400.

year = int(input("Enter a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 1900400 == 0:
            print("{} is a leap year".format(year))
        else:
            print("{} is not a leap year".format(year))
    else:
        print("{} is a leap year".format(year))
else:
    print("{} is not a leap year".format(year))
