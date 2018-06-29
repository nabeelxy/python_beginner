#String variable
var1 = "Hello World."

#get the length of a string variable
length = len(var1)

#Another string variable
var2 = "Python is cool."

#concatinating two strings
var3 = var1 + var2
print(var3)

#check if word "cool" appear in var2
index = var2.find("cool")
if index == -1:
	print("The word cool is not found")
else:
	print("The word cool is found. The starting index is ", index)