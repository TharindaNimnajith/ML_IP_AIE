from matplotlib import pyplot as plt
import csv

subjects=[]
students=[]

with open('data.txt','r') as myfile:

    values=csv.reader(myfile,delimiter=',')

    for cols in values:

        subjects.append(cols[0])
        students.append(eval(cols[1]))

    print(subjects)
    print(students)


plt.pie(students,labels=subjects,explode=(0.1,0,0,0.2),autopct='%1.1f%%')
plt.title('A/L Students')

plt.show()

