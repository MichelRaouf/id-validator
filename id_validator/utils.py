import re
from datetime import datetime

GOVERNORATES = {
    "01": "Cairo", "02": "Alexandria", "03": "Port Said", "04": "Suez",
    "11": "Damietta", "12": "Dakahlia", "13": "Sharqia", "14": "Qalyubia",
    "15": "Kafr El Sheikh", "16": "Gharbia", "17": "Monufia", "18": "Beheira",
    "19": "Ismailia", "21": "Giza", "22": "Beni Suef", "23": "Fayoum",
    "24": "Minya", "25": "Assiut", "26": "Sohag", "27": "Qena",
    "28": "Aswan", "29": "Luxor", "31": "Red Sea", "32": "New Valley",
    "33": "Matruh", "34": "North Sinai", "35": "South Sinai", "88": "Outside Egypt"
}

def validate_national_id(nid):
    if not re.fullmatch(r"\d{14}", nid):
        return False, "Invalid format. The ID must be 14 digits."

    century_code = nid[0]
    birth_date_str = nid[1:7]
    governorate_code = nid[7:9]
    serial_number = nid[9:13]
    gender_digit = int(nid[12])
    check_digit = nid[13]

    if century_code == "2":
        birth_year = "19" + birth_date_str[:2]
    elif century_code == "3":
        birth_year = "20" + birth_date_str[:2]
    else:
        return False, "Invalid century code in ID."

    try:
        birth_date = datetime.strptime(birth_year + birth_date_str[2:], "%Y%m%d")
    except ValueError:
        return False, "Invalid birth date in ID."

    governorate = GOVERNORATES.get(governorate_code, "Unknown")

    gender = "Male" if gender_digit % 2 == 1 else "Female"

    return True, {
        "birth_date": birth_date.strftime("%Y-%m-%d"),
        "governorate": governorate,
        "gender": gender,
        "serial_number": serial_number,
        "check_digit": check_digit
    }
