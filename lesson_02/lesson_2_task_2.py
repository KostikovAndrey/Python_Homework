def is_year_leap(year):
    return year % 4 == 0


years = [2033, 2208, 2011, 2222, 2024, 1201]

for year in years:
    result = is_year_leap(year)
    print(f"год {year}: {result}")
