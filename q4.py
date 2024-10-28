emps = dict()
i = 0
while True:
	i += 1
	emps['emp'+ str(i)] = eval(input("Enter a dictionary with the details with the following keys 'name', 'salary', 'dept': "))
	x = input("Enter anything to terminate: ")
	if x != '':
		break

for i in emps:
	if emps[i]['dept'] == "IT" and emps[i]['salary'] >200000:
		print(emps[i])
