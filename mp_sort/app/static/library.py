from org.transcrypt.stubs.browser import *
import random




array = []
array_str = ""

def gen_random_int(number, seed):
	# console.log("random")
	random.seed(seed)
	array = list(range(0, number))
	random.shuffle(array)
	return array



def generate():
	global array
	global array_str
	number = 10
	seed = 200
	array = gen_random_int(number, seed)
	# console.log('run')
	array_str= ",".join(array) + "."
	# console.log('array_str')


	# call gen_random_int() with the given number and seed
	# store it to the global variable array
	#pass

	#array = None
	# convert the items into one single string
	# the number should be separated by a comma
	# and a full stop should end the string.
	#pass

	#array_str = None

	# This line is to placed the string into the HTML
	# under div section with the id called "generate"
	document.getElementById("generate").innerHTML = array_str

def bubble_sort(array_sort):
	# console.log("testing", array_sort)
    n = len(array_sort)
    swapped = True
    while swapped:
        swapped = False
        new_n = 0
        for inner_index in range(1,n):
            first_number = array_sort[inner_index - 1]
            second_number = array_sort[inner_index]
            if first_number > second_number:
                swapped = True
                array_sort[inner_index - 1], array_sort[inner_index] = array_sort[inner_index], array_sort[inner_index - 1]
                new_n = inner_index
        n = new_n

def sortnumber1():

	array_str = ""
	bubble_sort(array)
	array_str = ",".join(array) + "."
	console.log("run", array)



	document.getElementById("sorted").innerHTML = array_str

def sortnumber2():
	'''	This function is used in Exercise 2.
		The function is called when the sort button is clicked.

		You need to do the following:
		- Get the numbers from a string variable "value".
		- Split the string using comma as the separator and convert them to
			a list of numbers
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str
	'''
	# The following line get the value of the text input called "numbers"
	value = document.getElementsByName("string")[0].value

	# Throw alert and stop if nothing in the text input
	if value == "":
		window.alert("Your textbox is empty")

	# Throw alert and stop if nothing in the text input

	else:
		array = value.split(",")
		bubble_sort(array)
		array_str = ",".join(array) + "."


	# Your code should start from here
	# store the final string to the variable array_str
	pass

	document.getElementById("sorted").innerHTML = array_str
