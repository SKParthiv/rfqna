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

# Output
# Enter the Employee No.: 1
# Enter the name of Employee No. 1: Jeff Bezoz
# Enter the salary of Mr./Ms. Jeff Bezoz: 20000000
# Type 'terminate' to terminate giving inputs: 
# Enter the Employee No.: 2
# Enter the name of Employee No. 2: Elon Musk
# Enter the salary of Mr./Ms. Elon Musk: 90000000
# Type 'terminate' to terminate giving inputs: 
# Enter the Employee No.: 3
# Enter the name of Employee No. 3: Tim Cook
# Enter the salary of Mr./Ms. Tim Cook: 70000000
# Type 'terminate' to terminate giving inputs: 
# Enter the Employee No.: 4
# Enter the name of Employee No. 4: Satya Nadela
# Enter the salary of Mr./Ms. Satya Nadela: 60000000
# Type 'terminate' to terminate giving inputs: 
# Enter the Employee No.: 5
# Enter the name of Employee No. 5: Sundar Pichai
# Enter the salary of Mr./Ms. Sundar Pichai: 100000000
# Type 'terminate' to terminate giving inputs: terminate
# (2, 'Elon Musk', 90000000)
# (3, 'Tim Cook', 70000000)
# (5, 'Sundar Pichai', 100000000)
# ((1, 'Jeff Bezoz', 20000000), (4, 'Satya Nadela', 60000000), (3, 'Tim Cook', 70000000), (2, 'Elon Musk', 90000000), (5, 'Sundar Pichai', 100000000))