import re
from datetime import datetime

GOVERNORATES = {
    "01": "Cairo", "02": "Alexandria", "03": "Port Said", "04": "Suez",
    "11": "Damietta", "12": "Dakahlia", "13": "Sharqia", "14": "Qalyubia",
    # Add more governorates as needed
}

def validate_national_id(nid):
    if not re.fullmatch(r"\d{14}", nid):
        return False, "Invalid format. The ID must be 14 digits."

    century_code = nid[0]
    birth_date_str = nid[1:7]
    governorate_code = nid[7:9]

    # Determine birth year
    if century_code == "2":
        birth_year = "19" + birth_date_str[:2]
    elif century_code == "3":
        birth_year = "20" + birth_date_str[:2]
    else:
        return False, "Invalid century code in ID."

    # Validate birthdate
    try:
        birth_date = datetime.strptime(birth_year + birth_date_str[2:], "%Y%m%d")
    except ValueError:
        return False, "Invalid birth date in ID."

    # Get governorate
    governorate = GOVERNORATES.get(governorate_code, "Unknown")

    return True, {
        "birth_date": birth_date.strftime("%Y-%m-%d"),
        "governorate": governorate
    }
