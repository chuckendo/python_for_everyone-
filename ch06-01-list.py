# list names [] and built on a index
names = ["Chuck", "Habby", "Tanya", "Kyle", "Claudia", "Nadine", "Renaldo", "Alyssa", "Myron", "Aruna", "Charlie"]
#print(f"Name: {names}")

# loop through name w for in range:
for i in range(11):
    print(f"Name: ({i}): {names [i]}")
    print("Bye\n")

#len of names
for i in range(len(names)):
    print(f"Name: ({i}): {names [i]}")
print("Bye\n")

  
# loop through names w/ for in range:
for i in range(len(names)):
    print(f"name({i}): {names[i]}", end=" ")
print("\n" + ("+" * 30))

numbers = [0,2,3,4,5,6,7,8,9,10]
#for eachloop
for nbr in numbers:
    print(nbr)

# Python we can create a list of multiple types
stuff = [1, "one", 1.1]
print(stuff)

print ("---- loop through numbers, multiplying each by 3 ---")
for n in numbers:
    t = n * 3
    print (f"n: {n}, t: {t}")

# referecing the a list
print("---List of Toys---")
toys = ["dolls", "choo choo train", "stuffed animals", "bouncy ball"]
print ("list of toys, start with #1")
for idx in range(len(toys)):
    print(f"{idx + 1}: {toys[idx]}")

# sorting
print("=== Sort the list of toys, alphabetically")
toys.sort()
print(f"toys: {toys}")
print("** Casing matters! Let's fix that...")
toys.sort(key=str.lower)
print (f"toys sorted again: {toys}")

# max min numbers
number = [5,75,-12,246,11,0]
print(f"numbers: {number}")
print(f"number max: {max(number)}")
print(f"number min: {min(number)}")

# slicing
numba = [5,75,-12,246,11,0]
print(f"numba[1:4]: {numba[1:4]}")
print(f"numba[:3]: {numba[:3]}")
print(f"numba[2:]: {numba[2:]}")

# List comprehension
numb = [1,2,3,4,5,6]
print(f"numbers: {numb}")
print("+ new list of even-squares - squared version of the even #s")
even_squares = []
for n in numb:
    if n % 2 == 0:
        even_squares.append(n * n)
print(f"even_squares: {even_squares}")

#tuple
print("define a tuple tuple to represent a movie...")
title = "Creed"
year = 2015
rating = "PG-13"
director = "Rayn Coogler"
run_time   = 133

creed_tuple = (title, year, rating, director, run_time)
print(f"creed tuple: {creed_tuple}")


