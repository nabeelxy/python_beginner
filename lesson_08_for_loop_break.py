#Python list data structure
mylist = ["Anne", "Mary", "Betty", "Ahmed", "Sam"]

#Print names before Ahmed only
for name in mylist:
	#if the name is Ahmed, we simply break out of the loop
	if name == "Ahmed":
		break

	print (name)