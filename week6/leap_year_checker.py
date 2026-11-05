def is_leap(year: int) -> bool:
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


def leap_year_checker(year: int) -> str:
    return f"{year} is a leap year" if is_leap(year) else f"{year} is not a leap year"


# bonus
def next_leap_year(year: int, count: int = 3) -> list[int]:
    leap_years = []
    candidate = year + 4 - year % 4

    while len(leap_years) < count:
        if is_leap(candidate):
            leap_years.append(candidate)
        candidate += 4

    return leap_years

print(leap_year_checker(2024))
print(leap_year_checker(1900))
print("Next 3 leap years after 2000 is", next_leap_year(2000))
print("Next 3 leap years after 2023 is", next_leap_year(2023))
