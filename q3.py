# Create a dict having all the alphabets as key and its mirror as value
abc = dict()
base = ord('a')
for i in range(26):
	abc[chr(base + i)] = chr(base-1 + (26-i))
print(abc)