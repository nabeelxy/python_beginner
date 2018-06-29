#mylist is a list of values
#in this case, it is a list of names
#list can have mixed values (for example, string and 
#integer). In this example, we only have strings.
mylist = ["Anne", "Mary", "Betty", "Ahmed", "Sam"]

#This tells python to iterate through each item in 
#the list mylist and do what is inside the for 
#loop block (we simply print the item)
#Notice that in each iteration list item is loaded
#to the variable named "name".
for name in mylist:
	print (name)