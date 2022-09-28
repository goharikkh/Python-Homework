#1  weight in kilograms and converts it to pounds
weight = int(input("Enter weight in kg "))
print(f"Weight in pound {weight * 2.2}")

# 2 generates and prints 50 random integers, each between 3 and 6
import random
for i in range(50):
    print(random.randint(3, 6))

# 3 computes | x − y | /  x+y
x = float(input("Enter the number x "))
y = float(input("Enter the number y "))
print(f"|x - y| = {abs(x - y) / (x + y) }")

# 4  determine how many leap years there have been between 1600 and that year.
year = int(input("Enter the year "))
count = 0
start = 1600
if year < start:
    start, year = year, start
for i in range(start, year + 1):
    if i % 100 == 0 and i % 400 != 0:
        continue
    elif i % 4 == 0:  # if i // 4 == i / 4
        count += 1
print(count)


# 5 perfect number
num = int(input("Enter the number "))
sum_ = 1
for i in range(2, num // 2 + 1):
    if num % i == 0:
        sum_ += i
if sum_ == num:
    print(f"{num} is perfect")
else:
    print(f"{num} isn't perfect")
