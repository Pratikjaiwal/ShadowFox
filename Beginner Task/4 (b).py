australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
uae = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
india = ["Mumbai", "Bangalore", "Chennai", "Delhi"]
def find_country():
    city_name = input("Enter a city name: ").strip()
    if city_name in australia:
        country = "Australia"
    elif city_name in uae:
        country = "UAE"
    elif city_name in india:
        country = "India"
    else:
        country = "unknown"
    if country != "unknown":
        print(f"{city_name} is in {country}")
    else:
        print(f"{city_name} is not in the predefined lists.")
find_country()