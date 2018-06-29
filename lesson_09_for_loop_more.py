#Print each letter in a word
print("Printing letters:")
for letter in "Python":
	print(letter)


#Print from 1 to 10
print("Printing numbers 1 to 10:")
#range(1, 11) function returns the list [1, 2, .., 10]
for num in range(1, 11):
	print(num)

#Iterating a list by index
#len(mylist) returns the number of items in the list (4)
#range(len(mylist)) is equivalient to range(0, len(mylist))
#in this case, it is, range(0, 4) which returns the list 
#[0, 1, 2, 3]
mylist = ["banana", "apple", "mango", "strawberry"]
print("My fruits list:")
for index in range(len(mylist)):
	print(mylist[index])