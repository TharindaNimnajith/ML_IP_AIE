x = [10, 20, 46, 78, 32]
print(x[2])

print()

std1 = [123, 'John', 91, 89, 78]
print(std1[0])

print()

#Dictionaries
#Similar to Associative Arrays in PHP
#Using key names instead of the numerical values of the array elements
#Key names can be any name of any type (int, float, string etc.)
#For example a key name can be: 'ID', "ID", 45, 4.52 etc.
#dict1 = {key1: value1, key2: value2, key3: value3, key4: value4}
std1 = {'ID': 123, 'name': 'John', 'maths': 91, 'physics':89, 'chemestry':78}
print(std1['ID'])
print(std1['name'])
print(std1['maths'])
print(std1['physics'])
print(std1['chemestry'])
print(std1)

print()

std1 = {'ID': 123, 45: 'John', 45.2: 91, "physics":89, 'chemestry':78}

print(std1['ID'])
print(std1[45])
print(std1[45.2])
print(std1['physics'])
print(std1["physics"])
print(std1["chemestry"])
print(std1['chemestry'])
print(std1)
