# Filename
# A class that defines a basic filename interface
#
# Members:
#     path: a string representing the folder path to a file
#     name: a string representing the actual filename

class Filename:
	path = ""
	name = ""

	# Don't strictly need to define __init__()
	# but it can be used to perform additional
	# setup for the interface
	def __init__(self):
		pass

	# Defining __repr__() allows print(filename_var)
	# to give a "nicely" formatted result
	def __repr__(self):
		return str(self.__class__) + ": " + str(self.__dict__)
