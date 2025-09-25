


def factorial(n):
    if n<2:
        return 1
    else:
        return n*factorial(n-1)
user_input=int(input("enter your number"))
result=factorial(user_input)
print("the factorial of" ,user_input,"is" ,result)





