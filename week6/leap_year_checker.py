def leap_year_checker(year: int) -> str:
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return f"{year} is a leap year"
    else:
        return f"{year} is not a leap year"

print(leap_year_checker(2024))
print(leap_year_checker(1900))
print(leap_year_checker(2000))
print(leap_year_checker(2023))
