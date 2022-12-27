

def leap_year(year):
    """Will check if a given year is a leap year or not. Returns 'True' for leap year."""
    if year % 4 == 0 and (year % 100 != 0 or (year % 100 == 0 and year % 400 == 0)):  # nested logic functions
        return True
    else:
        return False

# year = int(input("Which year do you want to check? "))


def days_in_month(year, month):  # looking for days in a month, given the year to account for leap years
    """Will return the number of days in a month given the year. Month range is 1 to 12.
        Leap Years have one extra day in February."""
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # list of default days
    leap_year(year)  # calling leap year function
    if leap_year(year):  # if (true); leap year function will return true or false
        month_days[1] = 29  # add + 1 to feb by setting feb to 29
        return month_days[month - 1]  # account for zero index, user will enter 1 for jan or 2 for feb, etc.
    else:                             # note the list[list_index] format, implied month is index variable
        return month_days[month - 1]  # return unmodified list item


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)  # returns list item, list item assigned to external variable "days"
print(days)                        # print returned list item


