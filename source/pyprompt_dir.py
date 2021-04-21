from os import getcwd, listdir, path, chdir
from pathlib import Path

import source.pyprompt_common_func as pyprompt_common_func

# orderMagnitude = {
# "B": 1,
# "KB": 1024,
# "MB": 1024**2,
# "GB": 1024**3,
# "TB": 1024**4,
# "PB": 1024**5
# }


def getSize(i):
	if path.getsize(i) == 0:
		return sum(f.stat().st_size for f in Path(i).glob("**/*") if f.is_file())
	else:
		return path.getsize(i)


def listDir(args):

	"""
	List the files and directories in the current working directory

	Arguments:

		-p	Path
		-s	Search
		-e	Specify that search terms must be explicit
		-f	List files only
		-d	List directories only

	Notes:

		Using the arguments "-f" and "-d" provides the same output as using no arguments at all

	Table contents:

		Name			The file's / directory's name
		Created		 The file's / directory's date of creation
		Last Modified   The date when the file / directory was last modified
		Last Accessed   The date when the file / directory was last accessed
		Size			The file's / directory's size in bytes
		Type			The file's / directory's type [File/Dir]

	Examples:

		root> dir -p C:\\ -s Program -e
		CWD: C:\\
		Name				| Created			 | Last Modified	   | Last Accessed	   | Size  | Type
		Program Files	   | 2020-01-31 04:30:17 | 2020-07-06 14:31:10 | 2020-07-06 14:31:10 | 20480 | Dir
		Program Files (x86) | 2020-01-31 04:30:18 | 2020-07-06 14:53:06 | 2020-07-06 14:53:06 | 12288 | Dir
		ProgramData		 | 2020-01-31 04:30:18 | 2020-05-30 20:13:23 | 2020-05-30 20:13:23 | 8192  | Dir
	"""

	path_, search_ = [], []
	files_, dirs_, isExplicit = False, False, False

	argCount = 0
	for arg in args:
		argCount += 1

		try:
			if arg.lower() == "-p":
				path_.append(args[argCount])
			if arg.lower() == "-s":
				search_.append(args[argCount])
			if arg.lower() == "-e":
				isExplicit = True
			if arg.lower() == "-f":
				files_ = True
			if arg.lower() == "-d":
				dirs_ = True
		except Exception:
			return "Missing argument for %s" % arg

	prevPath = getcwd()

	try:
		if path_ != []:
			chdir(path.join(*path_))
	except Exception:
		return "Invalid path: %s" % path.join(*path_)

	out = "CWD: %s\n" % getcwd()

	All, C, LM, LA, Size, Type = (
		["Name"],
		["Created"],
		["Last Accessed"],
		["Last Modified"],
		["Size"],
		["Type"],
	)

	for i in listdir(getcwd()):

		isValid = True

		if files_ == dirs_:
			files_, dirs_ = False, False
		if (files_ and path.isdir(i)) or (dirs_ and path.isfile(i)):
			isValid = False

		if search_ != []:
			for s in search_:
				if not (
					(s.lower() in i.lower() and not isExplicit)
					or (s in i and isExplicit)
				):
					isValid = False

		if isValid:

			All.append(i)
			A_ = pyprompt_common_func.getLongestWord(All)
			C.append(pyprompt_common_func.formatTime(path.getctime(i)))
			C_ = pyprompt_common_func.getLongestWord(C)
			LM.append(pyprompt_common_func.formatTime(path.getmtime(i)))
			LM_ = pyprompt_common_func.getLongestWord(LM)
			LA.append(pyprompt_common_func.formatTime(path.getatime(i)))
			LA_ = pyprompt_common_func.getLongestWord(LA)
			Size.append(str(getSize(i)))
			Size_ = pyprompt_common_func.getLongestWord(Size)
			Type.append("File" if path.isfile(i) else "Dir")

	if len(All) != 1:
		for i in range(len(All)):
			out += f"%-{A_}s | %-{C_}s | %-{LA_}s | %-{LM_}s | %-{Size_}s | %-4s\n" % (
				All[i],
				C[i],
				LA[i],
				LM[i],
				Size[i],
				Type[i],
			)

	chdir(prevPath)
	return out[:-1]


def changeDir(dirs):
	"""
	Change the current working directory

	Use the ".." argument to move over to the parent directory
	"""

	if len(dirs):
		try:
			chdir(path.abspath(path.join(*dirs)))
		except Exception:
			return "Could not change the working directory to %s" % path.abspath(
				path.join(*dirs)
			)
	else:
		return getcwd()
