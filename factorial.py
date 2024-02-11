fact = 1

num = int(input("enter a number"))

for item in range(1, num+1):
    fact = fact*item

print("factorial=", fact)