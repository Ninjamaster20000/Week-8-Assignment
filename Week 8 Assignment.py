import math

#1.	Stores your first name as a variable. Use all lowercase letters when you declare it.
firstName = "kyle"

#2.	Stores your last name as a variable. Use all uppercase letters when you declare it.
lastName = "KRATKIEWICZ"

#3.	Prints out, "Hello, <first name> <last name>" with the first name converted to uppercase letters and the last name converted to lowercase letters using string functions.
print("Hello,", firstName.upper(), lastName.lower())

#4.	Prints out two newlines.
print("\n\n")

#5.	Creates a new variable that stores your first and last name together with a space between both parts.
name = "Kyle Kratkiewicz"

#6.	Slices your last name from the variable you created in step 5 and prints it out. This must take place on one line. 
print(name[5:16])

#7.	Replaces your last name in the variable you created in step 5 with "<your last name>, Walsh College Student"; print out the new value of this variable.
name = name.replace("Kratkiewicz", "Kratkiewicz, Walsh College Student")
print(name)

#8.	Prints out the following:
#"Start by doing what's necessary; then do what's possible; and suddenly you are doing the impossible - Francis of Assisi"
#Your output must have quotes at the beginning and the end of your outputted text.
print('''"Start by doing what's necessary; then do what's possible; and suddenly you are doing the impossible - Francis of Assisi"''')

#9.	Stores 2 decimal numbers as variables.
num1 = 1.25
num2 = .8


#10.	Stores one addition, one subtraction, one multiplication, and one division operation of these variables as variables.
add = num1 + num2
sub = num1 - num2
mult = num1 * num2 
div = num1 / num2


#11.	Prints out each of the four results as:
#<numeric value of variable 1> plus <numeric value of variable 2> equals <value of variable that stored the result of addition>
#<numeric value of variable 1> minus <numeric value of variable 2> equals <value of variable that stored the result of subtraction>
#...etc. Each output should be on its own line and utilize a different technique for displaying the requested information (concatenation, string formatting expressions, string formatting method calls, f-Strings).
print(str(num1) + " plus " + str(num2) + " equal " + str(add))
print("%s minus %s equals %s" % (num1, num2, sub))
print("{} times {} equals {}".format(num1, num2, mult))
print(f"{num1} divided by {num2} equals {div}")

#12.	Creates a new variable called sq_root that stores the square root of the variable that holds the result of the multiplication operation you performed in step 10 to two decimal places. Print out this value as:
#The square root of <value of variable that stored the result of multiplication> equals <the variable you just calculated for this step>
#You may pick your own method for displaying this information.
sq_root = math.sqrt(mult)
print("The square root of", mult, "equals", "%.2f" % sq_root)

#13.	Stores the current month as a string variable (e.g. March, June, etc.) and day of the month as a numeric variable.
month = "October"
day = 27

#14.	Outputs "Today is day <day of month> of the month of <month variable>." This should be on a new line and tabbed over two times. You may pick your own method for displaying this information, but it should be different than the technique you used in step 12.
print("\n\t\tToday is day " + str(day) + " of the month of " + month + ".")