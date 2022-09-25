#  checks and prints whether the number is even or odd.
num = int(input("Enter the number "))
if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")

# checks and prints whether the character is a consonant or a vowel.
char = input("Enter the character ")
vowel = ["a", "e", "i", "o", "u", "y"]
if char.lower() in vowel:
    print(f"{char} is vowel")
else:
    print(f"{char} is consonant")


# prints the n-th Fibonacci number
n = int(input("Enter the number "))
a, b = 0, 1
for i in range(1, n):
    a, b = b, a + b
print(a)

# sum of digits
num = int(input("Enter the number "))
num = abs(num)
sum = 0
while num != 0:
    sum += num % 10
    num //= 10
print(f"sum of digits is {sum}")

#
for i in range(5):
    for j in range(5):
        if i == 0 or i == 4 or j == 0 or j == 4:
            print("*", end=" ")
        else:
            print("  ", end="")
    print()
