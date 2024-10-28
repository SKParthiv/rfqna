# Take in an input which is a Dictionary called phone having name as the key and phone no. as the value.
# Accept a name and display the phone no.. Accept a phone number and display the name.
# If the data is not found say name/phone not found
phone = dict()
while True:
	name = input("Enter a name: ")
	phoneno = int(input("Enter the Phone Number of " + name + ": "))
	phone[name] = phoneno
	x = input("Enter anything to terminate: ")
	if x != '':
		break

while True:
	norp = input("Enter the name or phone no. of the person you need details of: ")
	if norp.isdigit():
		for i in phone:
			if phone[i] == int(norp):
				print("Name of that person is: ", i)
				break
			else:
				print("Name/Phone No. not found")
	elif norp in phone:
		print("The phone no. of that person is: ", phone[norp])
	else:
		print("Name/Phone No. not found")
	x = input("Enter anything to terminate: ")
	if x != '':
		break