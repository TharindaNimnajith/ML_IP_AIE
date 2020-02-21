x = input()
print(x)

print()

x = input('Enter a number for x: ') #Assume x = 6
y = input('Enter a number for y: ') #Assume y = 4

ans = x + y

print(x) #6
print(y) #4

print(ans) #64

#Python takes all inputs as strings

print()

#Using evaluation to overcome the issue:

x = eval(input('Enter a number for x: '))
y = eval(input('Enter a number for y: '))

ans = x + y

print(x)
print(y)

print('Answer =', ans)

#The user can even input a mathematical function for the variables
#The evaluation of the mathematical function is taken
#For example input 10 * 3 + 5 for x (Evaluation will be: x = 35)

#After adding eval() function, when you input strings, you have to input them
#in the standard way (ex: 'Hello', "Hello" etc.)

##There are 2 types of Python languages: 2.x versions & 3.x versions
##In 2.x versions no need to use eval() function

