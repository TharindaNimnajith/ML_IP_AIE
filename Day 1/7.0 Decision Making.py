marks = eval(input('Enter Marks: '))

#Logical operators are used using keywords: and, or, not
#Don't use &&, ||, !

if(marks < 0 or marks > 100):
    grade = 'Not Valid'
    
elif(marks < 35):
    grade = 'F'

elif(marks < 45):
    grade = 'S'

elif(marks < 65):
    grade = 'C'

elif(marks < 75):
    grade = 'B'

else:
    grade = 'A'

print('Grade = ', grade)
