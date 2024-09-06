import csv

print("Welcome")

FILE_NAME = "./files/movies.csv"
with open(FILE_NAME, newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(f"{row[0]}, {row[1]}")


print("Good bye")