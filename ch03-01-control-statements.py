# # #page 67 boolean expression
# # light_color = input("What's the stoplight color? ").lower()

# # print(f"red? {light_color == 'red'}")
# # print(f"yellow? {light_color == 'yellow'}")
# # print(f"green? {light_color == 'green'}")

# # if light_color == "red":
# #     print(f"Light color is red - stop!")
# # elif light_color == "yellow":
# #     print("Light color is yellow - slow down!")
# # elif light_color == "green":
# #     print("Light color is green - go!")
# # number = int(input("Enter a whole number: "))

# # # even number? An even number has no remainder when divided by 2
# # print(f"number % 2 == 0? {number % 2 == 0}")
# # if number % 2 == 0:
# #     print("this is an even number")
# # else:
# #     print("this is an odd number")


# # # page 69 Logical Operators
# # # AND, OR, NOT
# # age = 37
# # city = "Chicago"

# # # over 35 and living Chicago?
# # if age >= 30 and city == "Chicago":
# #     print("Yep, over 35 is in Chi-Town")

# # # under 30 or living in Chicago
# # if age < 30 or city == "Chicago":
# #     print("under thirty or chicago")

# # #page 75 cover numeric to letter grade
# # numeric_grade = int(input("Please enter a numeric grade:"))

# # #convert to letter grade on the following scale:
# # # A >= 90, B >= 80, C >= 70, D >= 60, F below 60
# # # assume 0 <= numeric_grade <= 100
# # letter_grade = "F"
# # if numeric_grade >= 90:
# #     letter_grade = "A"
# # elif numeric_grade >= 80:
# #     letter_grade = "B"
# # elif numeric_grade >= 70:
# #     letter_grade = "C"
# # elif numeric_grade >= 60:
# #     letter_grade = "D"

# # print(f"numeric {numeric_grade}, letter {letter_grade}")

# # combine an AND an OR in on IF statement
# # deter a discount based on:
# # 1) Customer type: Retail (R) or Corporate (C)
# #   - C: 5%
# #   - R: 0%
# # 2) Invoice Total - Retail customers
# #   - 500: 2%
# #   - 1500: 4%

# customer_type = input("Customer Type (c/r): ").lower()
# invoice_total = float(input("Invoice Total? "))

# # customer selection
# if customer_type == "c":
#     discount_pct = 0.05
# elif customer_type == "r":
#     discount_pct = 0.0

# # customer discount
# if invoice_total >= 1500:
#     discount_pct = 0.04
# elif invoice_total >= 500:
#     discount_pct = 0.02
# else:
#     discount_pct = 0.0

# print(f"customer_type: {customer_type}")
# print(f"invoice_total: {invoice_total}")
# print(f"discount_pct: {discount_pct}")

# # page 85 while loop
# choice = input("Are you ready to go home (Y/N)").upper()
# while choice == "Y":
#     print("Good choice")
#     choice = input("Are you ready to go stay home (Y/N)").upper()
#     print("Your are fired!")

# you used the while loop to keep a block of code going until you decide to break the loop

# page 87 - for loop in range
# rang with stop value 5
# print(f"range(5): {range(5)}")
# for i in range(5): # range start from 0 and ends at 4
#     print(i, end=" ") # end=" " replaces the new line character with a "space"
# print("\n======")
# for i in range(1,5): # range start from 1 and ends at 4
#     print(i, end=" ") 
# print("\n======")
# for i in range(0,21,2): # range start from 0 and increment the count in 2s until the end of the range
#     print(i, end=" ") 
# print("\n======")
# for i in range(50,-1,-5): # range start from 50 decrement in -5s to -1
#     print(i, end=" ") 
# print("\n======")

# sum = 0
# for x in range(0,20):
#     sum += x # the value of x will keep adding until the range is complete
#     print(sum, end=" ") 
# print("\n======")

# page 93 - walrus operator
# an infinite loop to process user data
print ("Enter a -1 to quite")
print ("-------------------")
while True:
    score = int(input("Enter score: "))
    if score == -1:
        break
    print(f"You entered: {score}")
print("See you later!")
print("\n======")

# same code as above but with the walrus operator
print ("Enter -1 to quit.")
print ("-----------------")
while (score := input ("Enter score: ")) != "-1":
    print(f"You entered: {score}")
print("Bye")