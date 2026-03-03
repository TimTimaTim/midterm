def days_since_birthday(birthday):
    """
    birthday is a string in format DD-MM-YYYY
    Returns number of days passed (whole years only).
    """

    # Extract birth year
    birth_year = int(birthday.split("-")[2])

    # Set current year manually
    current_year = 2026

    # Calculate full years between
    full_years = current_year - birth_year - 1

    # Convert years to days
    days = full_years * 365

    return days

print(days_since_birthday("29-05-2006"))