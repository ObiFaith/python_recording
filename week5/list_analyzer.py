numbers = [12, 5, 27, 8, 14]

def list_analyzer(numbers: list[int]) -> dict[str, int]:
    analyzer = {
        "Smallest": numbers[0],
        "Largest": numbers[0],
        "Total": 0,
        "Average": 0.0,
    }

    smallest = largest = numbers[0]
    for num in numbers:
        if num < smallest:
            analyzer["Smallest"] = num
        elif smallest < largest < num:
            analyzer['Largest'] = num

        analyzer['Total'] += num

    analyzer["Average"] = analyzer['Total'] / len(analyzer)

    return analyzer

print("".join([f"{item}: {value}" for item, value in list_analyzer(numbers).items()]))
