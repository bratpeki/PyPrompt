from time import strftime, time

import source.pyprompt_mdc as mdc


def getTime(args):
	"""
	Get the current time.

	The default time format is defined by the key to the "defaultTimeFormat"
	setting varible --> "%d/%m/%Y %H:%M:%S (%a)"

	More string directives are available at https://strftime.org/.

	Arguments:

		-g	Get the current system time formatted by the "defaultTimeFormat" setting varible.
		-gu   Get the current system time formatted as a UNIX timestampt.
		-gf   Get the current system time with single-use custom formatting.

	Examples:

		root> time -g
		28/06/2020 22:42:26 (Sun)

		root> time -gu
		1593376947.722174

		root> time -gf "%H-%m %A"
		22-06 Sunday
	"""

	argCount = 0
	for arg in args:
		argCount += 1

		if arg == "-g":
			return strftime(mdc.settings["defaultTimeFormat"])
		if arg == "-gu":
			return str(time())
		if arg == "-gf":
			try:
				print(strftime(args[argCount]))
			except Exception:
				return "No format provided"
