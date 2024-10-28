emp = tuple()
avg = 0
while True:
    n = int(input("Enter the Employee No.: "))
    name = input("Enter the name of Employee No. "+ str(n) + ": ")
    salary = int(input("Enter the salary of Mr./Ms. " + name + ": "))
    emp += ((n, name, salary),)
    avg += salary
    enter = input("Type 'terminate' to terminate giving inputs: ")
    if enter == 'terminate':
        break
avg = avg / len(emp)
for i in emp:
    if i[2] > avg:
        print(i)
mi = emp[0]
sorted_tuple = tuple()
for j in range(len(emp)):
    for i in emp:
        if mi[2] > i[2] and i not in sorted_tuple:
            mi = i
    sorted_tuple += (mi,)
    mi = (emp[0][0], emp[1][1], avg*len(emp))
print(sorted_tuple)