# 1. prime number is only divisible by 1 & itself
# 2. all the prime numbers are odd number except 2
# num ko 3 se num tak check karenge ki wo bichmei kisi se dvide ho rha hai ki nhi
# divide ho rha hai to rule 1 false ho jayega


num = int(input("enter a number"))

def isPrimeNum(num):
    isPrime=False
    i=3

    if num==2 or num==3:
        isPrime=True
    else:
        while i<num:
            if num % i == 0:
                isPrime=False
                break
            i=i+1

    if i == num:
        isPrime=True

    return isPrime

prime=isPrimeNum(num)
if prime:
    print(str(num) + " is Prime.")
else:
    print(str(num) + " is Not a Prime.")