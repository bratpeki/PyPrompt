from os import path, mkdir, rename, chdir, getcwd, remove
from shutil import rmtree


def deleteDirFile(args):
	"""
	Delete a directory or file on the given path
	"""

	try:
		path_ = path.abspath(path.join(*args))
		if (
			input("Are you sure you want to delete %s? [Y/N] " % path_)
			.lower()
			.strip()
			!= "y"
		):
			return None
		if path.isfile(path_) or path.islink(path_):
			remove(path_)
			return "Deleted %s (File)" % path_
		elif path.isdir(path_):
			rmtree(path_)
			return "Deleted %s (Directory)" % path_
		else:
			return "Could not find %s" % path_

	except Exception:
		currDir = getcwd()
		chdir("..")
		return deleteDirFile([currDir])


def makeDirFile(args):

	"""
	Make a directory or file on the given path
	"""

	try:
		path_ = path.abspath(path.join(*args))
	except Exception:
		return "No arguments have been passed"
	try:
		if path.exists(path_):
			return "%s already exists" % path_
		else:
			if "." in path_:
				file = open(path_, "w")
				file.close()
			else:
				mkdir(path_)
	except Exception:
		return "Could not create %s" % path_
	else:
		return "Successfully created %s" % path_


def renameDirFile(args):

	"""
	Rename a directory or file on the given path

	Examples:

		root> rn music rnb rnb2012
		Renamed root\\music\\rnb to root\\music\\rnb2012
		root>

		root\\music\\rnb> rn rnb2012
		Renamed root\\music\\rnb to root\\music\\rnb2012
		root\\music\\rnbrnb2012>
	"""

	if not len(args):
		return "No arguments have been passed"
	elif len(args) == 1:
		n1 = getcwd()
		n2 = path.join(path.abspath(".."), args[0])
		goto = n2
	else:
		n1 = path.abspath(*args[:-1])
		n2 = path.abspath(args[-1])
		goto = getcwd()

	if n1 == path.abspath(".."):
		return "Illegal working space"

	chdir("..")

	try:
		rename(n1, n2)
	except Exception:
		chdir(goto)
		return "Could not rename %s to %s" % (n1, n2)
	else:
		chdir(goto)
		return "Renamed %s to %s" % (n1, n2)
