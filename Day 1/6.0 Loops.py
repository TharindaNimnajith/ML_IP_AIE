##Indentation is importantant in Python as there are no curly brackets {} to
##identify blocks

#for loops

#Starting value = 0, Ending value = 9, Increment = +1 (Default)
for i in range(10):
    print(i)

print()

#Starting value = 2, Ending value = 9, Increment = +1
for i in range(2, 10):
    print(i)

print()

#Starting value = -10, Ending value = 9, Increment = +2
for i in range(-10, 10, 2):
    print(i)

print()

#Starting value = 10, Ending value = 1, Increment = -2
for i in range(10, 0, -2):
    print(i)

print()

list1 = [10, 34.6, 'John', 'X', 32, 643]

for i in list1:
    print(i)

print()

for i in range(0, 6):
    print(list1[i])

print()

for i in range(0, 5):
    print(list1[i])

print()

for i in range(0, 5):
    print(list1)

print()

#Ten zeros
x = [0 for i in range(10)]
print(x)

print()

#Square numbers of integers from 0 to 9
x = [i * i for i in range(10)]
print(x)

print()

list2 = [10, 20, 30, 40, 50, 60, 70]

for i in range(0, len(list2)):
    print(list2[i])

print()

for i in list2:
    print(i)

print()

#2D Arrays

list1 = [[0 for i in range(5)] for j in range(10)]
print(list1)

print()

#while loop

i = 0

while(i < 10):
    print(i)
    i = i + 1
    #i++
    #i--
    #i += 1
    #i++ or ++i is not valid in Python
    #You can use i += 1 instead
