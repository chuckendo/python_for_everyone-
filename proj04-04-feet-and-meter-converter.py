def feet_to_meters(meters):
    feet = round((meters / 0.3048),2)
    return feet

def meters_to_feet(feet):
    meters = round((feet * 0.3048),2)
    return meters

# print(meters_to_feet(3))
print("\nFeet and Meters Converter\n")
print("Conversion Menu:")
print("a. Feet to Meters")
print("b. Meters to Feet")

while True:
    selection = input("\nPlease select a conversion (a/b): ").lower()
    number = round(float(input("Please enter a number: ")),2)
    if selection == "a":
        print(f"Enter feet: {number}")
        print(f"{meters_to_feet(number)} meters\n")
    elif selection == "b":
        print(f"Enter meter: {number}")
        print(f"{feet_to_meters(number)} feet\n")
    question = input("Would you like to perform another conversion: (y/n): ")
    
    if question == "y":
        continue
    else:
        break
