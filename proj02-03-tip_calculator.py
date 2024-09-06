meal_cost = float(input("Cost of meal: "))
tip_percent = float(input("How much did you tip: "))

tip = meal_cost * (tip_percent / 100)
total_cost = meal_cost + tip

print("You tipped: ", round(tip, 2))
print("Your total charge: ", round(total_cost, 2))