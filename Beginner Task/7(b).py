your_expenses = {
    "Hotel": 1200,
    "Food": 800,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 200
}
partner_expenses = {
    "Hotel": 1000,
    "Food": 900,
    "Transportation": 600,
    "Attractions": 400,
    "Miscellaneous": 150
}
total_your_expenses = sum(your_expenses.values())
total_partner_expenses = sum(partner_expenses.values())
print(f"Your total expenses: ${total_your_expenses}")
print(f"Your partner's total expenses: ${total_partner_expenses}")
if total_your_expenses > total_partner_expenses:
    print("You spent more money overall.")
elif total_partner_expenses > total_your_expenses:
    print("Your partner spent more money overall.")
else:
    print("You both spent the same amount of money.")
significant_difference = 0
category_with_difference = ""
for category in your_expenses:
    difference = abs(your_expenses[category] - partner_expenses[category])
    if difference > significant_difference:
        significant_difference = difference
        category_with_difference = category
print(f"The category with the most significant difference is '{category_with_difference}' with a difference of ${significant_difference}.")