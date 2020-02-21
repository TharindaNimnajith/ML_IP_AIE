#Variable Length Argument Type Functions

def func(a, *b):
    print(a, b)

#func() #ERROR
func(10) #No ERROR
func(10, 20)
func(10, 20, 30)
func(10, 20, 30, 40, 50, 60, 'Hello')

#b is a variable length tuple
#The length of the tuple is a variable
#First 10 is assigned to a
#Then all the other values passed are assigned to the tuple

#A value must be passed for a parameter
#The b tuple can have zero elements as the length of it is a variable
