australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
uae = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
india = ["Mumbai", "Bangalore", "Chennai", "Delhi"]
def check_same_country():
    city_1 = input("Enter the first city: ").strip()
    city_2 = input("Enter the second city: ").strip()
    if city_1 in australia:
        country_1 = "Australia"
    elif city_1 in uae:
        country_1 = "UAE"
    elif city_1 in india:
        country_1 = "India"
    else:
        country_1 = "unknown"
    if city_2 in australia:
        country_2 = "Australia"
    elif city_2 in uae:
        country_2 = "UAE"
    elif city_2 in india:
        country_2 = "India"
    else:
        country_2 = "unknown"
    if country_1 == "unknown" or country_2 == "unknown":
        print("One or both of the cities are not in the predefined lists.")
    elif country_1 == country_2:
        print(f"Both cities are in {country_1}")
    else:
        print("They don't belong to the same country")
check_same_country()