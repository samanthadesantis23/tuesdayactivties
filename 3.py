from datetime import date

def list_years(dates: list):
    # Extract years from each date and sort them in ascending order
    years = [d.year for d in dates]
    return sorted(years)
    
from datetime import date

# Example list of date objects
dates = [
    date(2023, 5, 15),
    date(2005, 8, 22),
    date(2018, 3, 10),
    date(1999, 1, 1)
]

# Call the list_years function
sorted_years = list_years(dates)

# Print the sorted years
print(sorted_years)