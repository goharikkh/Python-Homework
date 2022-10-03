# 1 Create a string that consists of the user’s numbers separated by plus signs.
string = ""
for i in range(5):
    num = str(input("Enter the number "))
    string += " + " + num
print(string[2:])


# 2 valid phone number checker
import re
valid = "^\\[0-9][0-9][0-9]{3,3,4}$"

if re.match(valid, input("Enter the phone number ")):
    print("Valid")
else:
    print("Invalid")



# 3 Use a list comprehension to produce a list that consists of all palindromic numbers between 100 and 1000.
res = [i for i in range(100, 1000) if str(i) == str(i)[::-1]]
print(res)

# 4
L = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
gap = [L[i + 1] - L[i] for i in range(len(L) - 1)]
print(max(gap))
print(gap.count(2) / len(gap) * 100)

# 5
product = dict()
while True:
    # product[input("Enter the name of product ")] = int(input("Enter the price of that product "))
    product_name = input("Enter the name of product ")
    if product_name == "":
        break
    price = int(input("Enter the price of that product "))
    product[product_name] = price

print(product)

while True:
    product_name = input("Enter the name of product ")
    if product_name == "":
        break
    if product_name not in product.keys():
        print("There isn't such a product")
    else:
        print(product[product_name])

# 6
di = [{'name':'Todd', 'phone':'555-1414', 'email':'todd@mail.net'},
{'name':'Helga', 'phone':'555-1618', 'email':'helga@mail.net'}, {'name':'Princess', 'phone':'555-3141', 'email':''},
{'name':'LJ', 'phone':'555-2718', 'email':'lj@mail.net'}]

print("ends with 8")
for i in di:
    if i['phone'].endswith("8"):
        print(i["name"])

print("without email")
for i in di:
    if i["email"] == "":
        print(i["name"])


# 7
matrix = [[9, 2, 3, 8, 5],
          [6, 7, 85, 12, 8],
          [32, 2, 9, 10, 5],
          [3, 10, 3, 75, 8],
          [77, 2, 3, 4, 5]]
count = dict()
for i in range(len(matrix)):
    for j in range(len(matrix)):
        count[matrix[i][j]] = count.get(matrix[i][j], 0) + 1

lst = list(set(count.values()))
lst.sort(reverse=True)
lst = lst[:3]
for i in lst:
    for j in count.keys():
        if count[j] == i:
            print(str(j) + " ; " + str(count[j]))
