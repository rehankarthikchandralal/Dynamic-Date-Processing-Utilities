import datetime
class DDPU():
    def days_in_month(self,year, month):

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

        return days

    def is_valid_date(self,year, month, day):

        # Check if the year is within the valid range
        if not (datetime.MINYEAR <= year <= datetime.MAXYEAR):
            return False
        
        # Check if the month is valid (between 1 and 12)
        if month < 1 or month > 12:
            return False

        # Check if the day is valid for the given month and year
        days_in_given_month = self.days_in_month(year, month)
     
        if day < 1 or day > days_in_given_month:
            return False

        # If all checks pass, return True
        return True

    def days_between(self,year1, month1, day1, year2, month2, day2):

            # Check if both dates are valid
            if not (self.is_valid_date(year1, month1, day1) and self.is_valid_date(year2, month2, day2)):
                print("ERROR:INVALID Date")
                return None
            
            # Create datetime.date objects for both dates
            date1 = datetime.date(year1, month1, day1)
            date2 = datetime.date(year2, month2, day2)
            
            # If the second date is earlier than the first, return 0
            if date2 < date1:
                print("ERROR:Second date is earlier than first")
                return None
            
            # Return the difference in days
            return (date2 - date1).days
    
    def age_in_days(self,year, month, day):
            
            # Check if the input date is valid
            if not self.is_valid_date(year, month, day):
                print("ERROR:INVALID Date")                
                return None
            
            # Get today's date
            today = datetime.date.today()
            
            # Check if the input date is in the future
            birth_date = datetime.date(year, month, day)
            if birth_date > today:
                print("ERROR:input date is in the future")
                return None
            
            # Use the days_between function to calculate the age in days
            return self.days_between(year, month, day, today.year, today.month, today.day)
    
test = DDPU()

#Test Code
# result_days=test.days_in_month(2023,12)
# print(result_days)
# print(test.is_valid_date(2022,11,3))
# print(test.days_between(2023, 1, 1, 2023, 1, 10))  # Output: 9
# print(test.days_between(2023, 2, 28, 2023, 3, 5))  # Output: 5
# print(test.days_between(2023, 2, 28, 2023, 2, 25))  # Output: None (second date is earlier)
# print(test.days_between(2023, 2, 30, 2023, 3, 1))  # Output: None (invalid first date)
# print(test.age_in_days(2000, 1, 1))  # Output: the number of days from Jan 1, 2000 to today
# print(test.age_in_days(2025, 1, 1))  # Output: None (future date)
# print(test.age_in_days(2023, 2, 30)) # Output: None (invalid date)
