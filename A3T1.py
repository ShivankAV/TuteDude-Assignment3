a=int(input("\33[95m Enter a number: "))
def factorial(n):
    fact=1
    if n==1:
       fact=1
    else:
       for i in range(1,n+1):
            fact=fact*i
    print(f"Factorial of {n} is: ",fact)
factorial(a)

