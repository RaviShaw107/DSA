def max (num1, num2):
    if num1> num2:
        return num1
    else:
        if num2> num1:
            return num2
        
x= int(input("enter 1st number"))
y= int(input("enter 2nd number"))

greater = max(x,y)
print(greater,"is greater")