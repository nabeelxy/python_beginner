#Python list data structure
mylist = ["Anne", "Mary", "Betty", "Ahmed", "Sam"]

#Print all names except Betty
for name in mylist:
	#if the name is Betty, we simply ignore the loop
	#(continue) and go to the next iteration
	if name == "Betty":
		continue

	print (name)