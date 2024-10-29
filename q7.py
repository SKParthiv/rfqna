# Write a program to accept a nested tuple, where each tuple has the name of the students along with the marks of the student. Display the name along with the average marks of the student. and display the details(includes all the marks and name) of highest average and lowest average
stud = tuple()
avg = tuple()
while True:
    name = input("Enter the name of the student: ")
    marks = tuple()
    avg1 = 0
    for i in range(3):
        m = int(input("Enter marks of " + name + " in Subject No. " + str(i+1) + ": "))
        marks += (m,)
        avg1 += m
    avg1 = avg1/3
    avg += ((name, avg1),)
    stud += (((name,) + marks),)
    enter = input("Type 'terminate' to terminate giving inputs: ")
    if enter == 'terminate':
        break
print("Part 1")
for i in avg:
    print(i)
print("Part 2")
m = ("Random guy", 0)
mi = ("Random guy2", avg[0][1] * 3)
for i in avg:
    if m[1] < i[1]:
        m = i
    if mi[1] > i[1]:
        mi = i
print("Lowest avg student is " + mi[0] + " With an average of " + str(mi[1]) + " as his marks are ", end='')
print(stud[avg.index(mi)][1:])
print("Highest avg student is " + m[0] + " With an average of " + str(m[1]) + " as his marks are ", end='')
print(stud[avg.index(m)][1:])