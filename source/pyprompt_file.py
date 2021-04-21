from os import path


def readFile(filePath):
	"""
	Read the contents of a provided file into the buffer

	Example:

		root> read hello.py
		def _hello_():
			\"\"\" This command prints "Hello!" to the screen. \"\"\"
			print ("Hello!")

		if __name__ == "__main__":
			_hello_()
	"""

	try:
		file = open(filePath, "r")
	except Exception:
		if filePath == "":
			return "No file provided"
		else:
			return "Could not find %s" % path.abspath(filePath)
	return file.read()


def makeFile(args):

	"""
	Make a file on the given path
	"""

	if not len(args):
		return "Argument not passed"

	path_ = path.abspath(path.join(*args))
	try:
		file = open(path_, "w")
		file.close()
	except Exception:
		return "Could not create %s" % path_
	else:
		return "Successfully created %s" % path_
