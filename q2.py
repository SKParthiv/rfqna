# Take the dict as input and count the no of lists tuples and strings, others in it.
data = dict()
while True:
	key = eval(input("Enter a key: "))
	value = eval(input("Enter the value corresponding to '" + str(key) + "': "))
	data[key] = value
	x = input("Enter anything to terminate: ")
	if x != '':
		break
count = {'lists': 0, 'tuples': 0, 'strings': 0, 'others': 0}
for i in data:
	if type(data[i]) == list:
		count['lists'] += 1
	elif type(data[i]) == tuple:
		count['tuples'] += 1
	elif type(data[i]) == str:
		count['strings'] += 1
	else:
		count['others'] += 1
for i in count:
	print("The number of", i, "is", count[i])