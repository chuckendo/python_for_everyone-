def cal_mile_per_gallon(miles_driven, gallons):
    mpg = miles_driven / gallons
    mpg = round (mpg, 1)
    return mpg

def print_welcome(message):
    print("=" * len(message))
    print(message)
    print("=" * len(message) + "\n")

def main():
    # print a variable of mpgs by car
    print(f"mpg: {cal_mile_per_gallon(100, 25)}")
    print(f"mpg: {cal_mile_per_gallon(125, 15)}")
    print(f"mpg: {cal_mile_per_gallon(280, 25)}")

if __name__ == "__main__":
    main()