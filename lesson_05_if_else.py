#The function takes one input parameter named side.
#It can take values "H" or "T".
#If side is "H", it prints one string.
#Otherwise, it prints another string.
def print_coin_side(side):
	if side == "H":
		print ("It's a head!")
	else:
		print ("It's a tail!")


#call the function twice with two different
#input values.
print_coin_side("H")
print_coin_side("T")