#There are no arrays in Python
#There are lists, tuples and dictionaries in Python

#List:

x = [10, 20.32, 'John', "c", (6 + 2j)]
#As Python doesn't consider data types, the list x can have any type of data

print(x)
#No loop is needed to print the list

print(len(x)) #size/length of the array/list

print(x[1:3]) #print from element 1 to 3 (element 3 is not included)
print(x[1])   #print element 1
print(x[1:])  #print from element 1 to the end
print(x[:3])  #print from the beginning (element 0) to element 3 (element 3 - not included)

print()

x = [10, 20, 46, 78, 32, 12, 43, 12]

print(x[1:3])
print(x[1])
print(x[1:])
print(x[:3])

print()

print(max(x))
print(min(x))
print(sum(x))

print()

#Modifying the list (Assign items/values to the list)
x[2] = 0
print(x)
