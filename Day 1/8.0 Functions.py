#def keyword is used to define functions
#There is no return type, no curly brackets {}, no semicolons ;
#The indentation must be very clean and clear
#The user defined functions should be defined first at the top of the program
#before calling the function

def function1(a, b):
    print(a, b)
    c = a + b
    return c

ans = function1(10, 20)
print('Answer = ', ans)

print()

print('Answer = ', function1(10, 20))

##There are 4 types of Python functions:
##    1.Required argument type
##    2.Keyword argument type
##    3.Default argument type
##    4.Variable length argument type

