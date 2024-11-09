# README: DDPU Class for Date and Time Calculations

## Overview

The `DDPU` class provides methods for working with dates:
- Calculate the number of days in a given month and year.
- Validate if a date is valid.
- Calculate the number of days between two dates.
- Calculate the age of a person in days from their birth date.

It uses Python's built-in `datetime` module.

## Methods

### 1. `days_in_month(self, year, month)`
Returns the number of days in a specific month and year. Returns `None` for invalid input.

### 2. `is_valid_date(self, year, month, day)`
Returns `True` if the date is valid; otherwise, `False`.

### 3. `days_between(self, year1, month1, day1, year2, month2, day2)`
Returns the number of days between two dates. Returns `None` if any date is invalid or the second date is earlier than the first.

### 4. `age_in_days(self, year, month, day)`
Returns the age in days based on the given birth date. Returns `None` if the date is invalid or in the future.

## Usage Example

```python
test = DDPU()

# Get the number of days in a month
print(test.days_in_month(2023, 12))  # Output: 31

# Check if a date is valid
print(test.is_valid_date(2022, 11, 3))  # True

# Calculate the days between two dates
print(test.days_between(2023, 1, 1, 2023, 1, 10))  # 9

# Calculate the age in days
print(test.age_in_days(2000, 1, 1))  # Number of days since Jan 1, 2000

