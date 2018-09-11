# Anne Harris
# CS344 - 400
# Program Py
# Description: This program creates 3 files in the same directory, each named
#   differently. Each file contains exactly 10 random lowercase characters
#   The eleventh character is a newline character. The program sends output
#   to stdout and prints the contents of the three files. It will then print out two
#   random integers between 1 and 42, and the prodcut on two seperate lines

# import libaries
import string
import random
import sys

# Function to generate random lowercase characters
# modeled off of stack overflow article titled: Random string generation with 
# upper case letter and digits in Python
def string_generator(size = 10, chars = string.ascii_lowercase):
	return ''.join(random.choice(chars) for _ in range(size))

# Main Function
def main():
	# create 3 files
	for x in range(3):
		# create file name
		file_name = "akhFile" + str(x)
		# open file
		f = open(file_name, "w")

		# get random string
		random_string = string_generator()
		# append a new line
		random_string = random_string + "\n"

		# write line to file
		f.write(random_string)
		sys.stdout.write(random_string)

		#close file
		f.close()

	# get random numbers between 1 and 42
	rand_num_1 = random.randint(1,42)
	rand_num_2 = random.randint(1,42)

	# print numbers
	print(rand_num_1)
	print(rand_num_2)

	# get product of two numbers
	product = rand_num_1 * rand_num_2

	# print product
	print(product)

if __name__ == "__main__":
	main()
