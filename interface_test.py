import sys

from filename_handler import FilenameHandler
from interfaces.filename import Filename

def main():
	# Testing class functionallity
	print("Testing class functionallity")

	test_file = FilenameHandler()

	if not test_file.full_path_is_set():
		print("\tFilenameHandler is currently unset")

	# Testing class capabilities
	print("\nTesting class capabilities")
	test_str = "./test/image.jpg"
	print("\tSetting filename to: " + test_str)
	test_file.set_full_path(test_str)

	if test_file.full_path_is_set():
		print("\tTest path: " + test_file.get_path())
		print("\tTest name: " + test_file.get_name())
		print("\tTest full path: " + test_file.get_full_path())
	else:
		raise RuntimeError("Error setting filename")

	print("\tChecking FilenameHandler.__repr__(): " + str(test_file))

	# Testing interface functionallity
	print("\nTesting interface functionallity")
	interface_fn = test_file.get_filename()

	if isinstance(interface_fn, Filename):
		print("\tChecking Filename.__repr__(): " + str(interface_fn))
	else:
		raise RuntimeError("get_filename() didn't return a Filename interface")

	test_name = "image2.png"
	interface_fn.name = test_name
	print("\tSetting name to " + test_name + ": " + str(interface_fn))

	test_file.set_filename(interface_fn)
	print("\tUpdating FilenameHandler: " + test_file.get_full_path())

if __name__ == "__main__":
	main()
