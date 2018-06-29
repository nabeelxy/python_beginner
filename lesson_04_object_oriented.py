class Calculator:
	#two attributes val1 and val2
	#they are intialized to zero
	val1 = 0
	val2 = 0

	#Constructor
	#This is called when an object of the class
	#is created
	def __init__(self, value1, value2):
		self.val1 = value1
		self.val2 = value2

	#one addition method - it uses the values 
	#stored in the class level attributes val1
	#val2
	def addition_default(self):
		sum = self.val1 + self.val2
		return sum

    #another addition method, it uses the two
    #input parameter values passed to it
	def addition(self, value1, value2):
		sum = value1 + value2
		return sum

#Create a Calculator object
cal1 = Calculator(10, 15)

#call the addition_default method
sum1 = cal1.addition_default()
print ("sum1: ", sum1)

#call the addition method
sum2 = cal1.addition(25, 15)
print ("sum2: ", sum2)