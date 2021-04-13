#Data Types

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

print(int(str(two_digit_number)[0]) + int(str(two_digit_number)[1]) )

#Notes:
#Boolean: starts always with the first capital letter: False True
#Integer: cannot be inside quotes(like in Javascript). "_" is used as a thousand separator. i.e. 24_123_654 = 24123654. 
#	The len() function takes only strings, it does not parse integers.
#String: Position reference is done with square brackets, i.e. "Car"[2] => "r"

#type() function is used to find the type of a variable
#Casting:
#	str(var) => casts to string.
#	float(var) => casts to float. It can take strings or numbers.

#input() function in python will take input given by the user through the prompt as a string

