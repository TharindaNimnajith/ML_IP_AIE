mark=eval(input('Enter the marks of the Student:'))

if(mark<0 or mark>100):

    grade='not valid'

elif(mark<35):

    grade='F'

elif(mark<45):

    grade='S'

elif(mark<65):

    grade='C'

elif(mark<75):

    grade='B'

elif(mark<=100):

    grade='A'

else:

    grade='Not Valid'


print('Grade=',grade)
