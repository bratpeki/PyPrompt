"""
MODULE DEPENDENT COMMANDS
"""

from json import load

try:
	import pyprompt_alias
	import pyprompt_dir_file
	import pyprompt_dir
	import pyprompt_file
	import pyprompt_global
	import pyprompt_online
	import pyprompt_system
	import pyprompt_time
	import pyprompt_user
	import pyprompt_version

except Exception:
	try:
		import source.pyprompt_alias as pyprompt_alias
		import source.pyprompt_dir_file as pyprompt_dir_file
		import source.pyprompt_dir as pyprompt_dir
		import source.pyprompt_file as pyprompt_file
		import source.pyprompt_global as pyprompt_global
		import source.pyprompt_online as pyprompt_online
		import source.pyprompt_system as pyprompt_system
		import source.pyprompt_time as pyprompt_time
		import source.pyprompt_user as pyprompt_user
		import source.pyprompt_version as pyprompt_version

	except Exception as e:
		print("Exception:", e)
		input("Press any key to continue...")
		exit()

import source.pyprompt_common_func

base = pyprompt_dir_file.path.dirname(pyprompt_dir_file.path.realpath(__file__))

try:
	settings = load(open(pyprompt_dir_file.path.join(base, "settings\\settings.json")))
	alias = load(open(pyprompt_dir_file.path.join(base, "alias\\alias.json")))
except Exception as e:
	print("Exception:", e)
	input("Press any key to continue...")
	exit()


def echo(keyword):
	"""
	Echo an inserted keyword or value corresponding to a special key (ex. $user)
	A list of keys is available as the key "$lsk"

	Exmples:

		root> echo TEST
		TEST

		root> echo "Hello
		> World!"
		HelloWorld!

		root> echo $version
		1.0

		root> echo $lsk
		$user   Returns the system's username
		$system Returns the system name
		...
	"""

	if keyword == "$lsk":
		keyword = ""
		keys, descs = [], []
		for i in pyprompt_user.keys:
			keys.append(i)
			k = source.pyprompt_common_func.getLongestWord(keys)
			descs.append(pyprompt_user.keys[i][1])
			d = source.pyprompt_common_func.getLongestWord(descs)
		for i in range(len(keys)):
			keyword += f"%-{k}s %-{d}s\n" % (keys[i], descs[i])
		keyword = keyword[:-1]

	else:
		sortedDict = {}
		for i in sorted(pyprompt_user.keys, key=len)[::-1]:
			sortedDict[i] = pyprompt_user.keys[i]
		for i in sortedDict:
			keyword = keyword.replace(i, sortedDict[i][0])

	return keyword
