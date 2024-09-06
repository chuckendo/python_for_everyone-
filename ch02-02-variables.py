# declare some variables
# page 35

# snake_case
first_name = "Bob"

# camelCase
lastName = "Marley"

# spinal-case
middle_name = "Nesta"

print(first_name + " " + lastName + " " + middle_name)
print("-- page.39--")
a = 25
b = 4 

print(a / b)
print(a // b)
print(a % b)

a = 5
b = 8
c = a + b


# formatted print string "f" literal
print(f"c = {c}")

# compand assignment operator
# c+=a is the same as c = c + a
c += a
print(f"c = {c}")

count = 0
# increment count by 1
count += 1
print(f"count = {count}")

# page 47 escape sequences

# print columns using \t tab

print("col1\tcol2\tcol3")

#implicit line continuation:
print("Name: "+ first_name + "\n" +
      "Age: " +str(43))

print(f"Name:  {first_name}\n"
      f"Age: {45}")

# page 51 sep and end arguments
print("abc",end="")
print("def")

print(1,2,3,4, sep="!")

# page 58 input() from a user
# get users name from console

name = input("Enter your Fucking name ✌(-‿-)✌: ")
print(f"You entered: {name}")

#float and int
price = float(input("Enter quantity: "))
qty = int(input("Enter quantity: "))
print(f"price * qty = {price * qty}")

#round function:
miles_driven = 150
gallons_used = 5.875

mpg = miles_driven / gallons_used

print(f"mpg = {mpg}")