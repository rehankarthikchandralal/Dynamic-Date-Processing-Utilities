import datetime


class DDPU():


    def days_in_month(year, month):

        """
        Inputs:
        year  - an integer between 
        representing the year
        month - an integer between 1 and 12 representing the month

        Returns:
        The number of days in the input month.
        """

        if ((year > datetime.MINYEAR) & (year < datetime.MAXYEAR)):
            print("The year is",year)
        else:
            print("ERROR:INVALID input",year)
            return None
        if ((month > 0) & (month < 13)):
            print("The month is",month)
        else:
            print("ERROR:INVALID input",month)
            return None
        # Start date for the given month and year
        start_date = datetime.date(year, month, 1)
        
        # Calculate the first day of the next month
        if month == 12:
            end_date = datetime.date(year + 1, 1, 1)
        else:
            end_date = datetime.date(year, month + 1, 1)
        
        # The difference in days between end_date and start_date
        days = (end_date - start_date).days
        print(days)
        
        return days

    result_days=days_in_month(2023,12)
    print(result_days)
    # def is_valid_date(year, month, day):
    #     """
    #     Inputs:
    #     year  - an integer representing the year
    #     month - an integer representing the month
    #     day   - an integer representing the day

    #     Returns:
    #     True if year-month-day is a valid date and
    #     False otherwise
    #     """
    #     return False

    # def days_between(year1, month1, day1, year2, month2, day2):
    #     """
    #     Inputs:
    #     year1  - an integer representing the year of the first date
    #     month1 - an integer representing the month of the first date
    #     day1   - an integer representing the day of the first date
    #     year2  - an integer representing the year of the second date
    #     month2 - an integer representing the month of the second date
    #     day2   - an integer representing the day of the second date

    #     Returns:
    #     The number of days from the first date to the second date.
    #     Returns 0 if either date is invalid or the second date is
    #     before the first date.
    #     """
    #     return 0

    # def age_in_days(year, month, day):
    #     """
    #     Inputs:
    #     year  - an integer representing the birthday year
    #     month - an integer representing the birthday month
    #     day   - an integer representing the birthday day

    #     Returns:
    #     The age of a person with the input birthday as of today.
    #     Returns 0 if the input date is invalid or if the input
    #     date is in the future.
    #     """
    #     return 0


