#Difference between tuples & lists:
#Lists - Square Brackets []
#Tuples - Round Brackets ()

x = (10, 20, 46, 78, 32, 12, 43, 12)

#Trying to modify the tuple (Trying to assign items/values to the tuple)
#x[2] = 0  #Gives an error message
#TypeError: 'tuple' object does not support item assignment
#Tuple is a read only list
#All the other functions can be performed to the tuples similar to the lists

print(max(x))
print(min(x))
print(sum(x))

print()

print(x[1:3])
print(x[1])
print(x[1:])
print(x[:3])
