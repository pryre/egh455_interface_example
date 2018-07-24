# Filename
# A class that defines a basic filename handler
# This path also demonstrates methods to ensure specific input types
# are provided to functions.
#
# Members:
#     filename: A basic filename interface
# Functions:
#     full_path_is_set(): Returns true if a full path has been set
#
#     get_name(): Returns the name of the file
#     get_path(): Returns the path of the file
#     get_full_path(): Returns the full path to the file
#     get_filename(): Returns the internal filename interface
#
#     set_name( name ): Sets the internal filename's name
#     set_path( path ): Sets the internal filename's path
#     set_full_path( full_path ): Sets the internal filename's using a full path
#     set_filename( filename ): Set the internal filename interface

from interfaces.filename import Filename

class FilenameHandler:
	def __init__(self):
		self.filename = Filename()

	def __repr__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def full_path_is_set(self):
		return self.filename.path and self.filename.name

	def get_name(self):
		return str(self.filename.name)

	def get_path(self):
		return str(self.filename.path)

	def get_full_path(self):
		return self.get_path() + self.get_name()

	def get_filename(self):
		return self.filename

	def set_name(self, name):
		if not isinstance(name, str):
			raise TypeError("set_name(): must pass a str type variable")

		self.filename.name = str(name)

	def set_path(self, path):
		if not isinstance(path, str):
			raise TypeError("set_path(): must pass a str type variable")

		self.filename.path = str(path)

	def set_full_path(self, full_path):
		if not isinstance(full_path, str):
			raise TypeError("set_full_path(): must pass a str type variable")

		split = str(full_path).rsplit('/',1)

		# Handle the case where we're given an empty local variable
		if len(split) == 1:
			path = "./"
			name = split[0]
		else:
			# We need to tack on the trailing slash that is cut from the path
			path = split[0] + "/"
			name = split[1]

		self.set_path(path)
		self.set_name(name)

	def set_filename(self, filename):
		self.filename = filename
