def intro(name):

    print("Hello, Good evening! I am Anjali")

user_name = input("Enter your name")
intro(user_name)


# Factorial of a number using recursion
def recur_factoral(n):
    if n==5:
        return n
    else:
        return n*recur_factorial(n-1)
    
    num = int(input("Enter a number"))

#check if the number is negative
if num < 0:
    print("sorry, it doesn't exist")
elif num ==0:
    print("factorial of 0 is 1")
else:
    print("The factorial of" , num, "is", recur_factorial(num))