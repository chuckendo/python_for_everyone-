# print - accepts a parameter and doesn't return anything





# int - access a paramter a vlue of type int
one_str = "1"
one_int = int(one_str)

# print () - accepts no arguments/parameters
print()

# a functin we write that accepts no parms and doesn't return anything

def print_welcome():
    print("Welcome to the chapter 4 demonstration.app!")
    print()


print_welcome()

# a function that accepts one parameter and return
def print_welcome(message):
    print(message)
    print()

print_welcome("Wow Function are so rad!")

# function accepts 2 arguments, returns a value
# computer the miles per gallons, given miles driven and gallons
def cal_mile_per_gallon(miles_driven, gallons):
    mpg = miles_driven / gallons
    mpg = round (mpg, 1)
    return mpg

print(f"mpg: {cal_mile_per_gallon(100, 25)}")

prius_mile = 350
prius_gallons = 8

print(f"Prius mpg: {cal_mile_per_gallon(prius_mile, prius_gallons)}")