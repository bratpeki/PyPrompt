import source.pyprompt_mdc as pyprompt_mdc

from json import dump


def aliasMgmt(args):

	"""
	Manage your aliases
	Aliases represent single keywords that stand in place of other keywords

	Aliases are called using the prefix '%'. Without it, strings are interpreted as literals.

	Arguments:

		-n  Add a new alias
		-d  Delete an existing alias
		-l  List all available aliases

	Examples:

		root> alias -n hw "Hello World"
		Successfully added alias 'hw' ('Hello World')
		root> echo %hw!!!
		Hello World!!!

		root> alias -d hw
		Successfully deleted alias 'hw'
		root> echo %hw!!!
		%hw!!!
	"""

	delAlias = []
	newAlias = []
	lstAlias = False

	argCount = 0
	for arg in args:
		argCount += 1

		try:
			if arg.lower() == "-d":
				delAlias.append(args[argCount])
			if arg.lower() == "-n":
				newAlias.append([args[argCount], args[argCount + 1]])
			if arg.lower() == "-l":
				lstAlias = True
		except Exception:
			return "Missing argument(s) for %s\n" % arg

	if len(delAlias) > 0:
		out = ""
		for delInstance in delAlias:
			try:
				del pyprompt_mdc.alias[delInstance]
				dump(
					pyprompt_mdc.alias,
					open(pyprompt_mdc.base + "\\alias\\alias.json", "w"),
				)
				out += "Successfully deleted alias '%s'\n" % delInstance
			except Exception:
				out += "Couldn't delete alias '%s'\n" % (delInstance)
		print(out[:-1])

	if len(newAlias) > 0:
		for newIn in newAlias:
			print("\"" + newIn[1] + "\"")
			try:
				if newIn[0] in pyprompt_mdc.alias:
					if (
						input(
							"Alias '%s' already points to '%s'. Replace it with '%s'? [Y/N] "
							% (newIn[0], pyprompt_mdc.alias[newIn[0]], newIn[1])
						)
						.lower()
						.strip()
						!= "y"
					):
						continue
				pyprompt_mdc.alias[newIn[0]] = newIn[1]
				dump(
					pyprompt_mdc.alias,
					open(pyprompt_mdc.base + "\\alias\\alias.json", "w"),
				)
				print("Successfully added alias '%s' ('%s')" % (newIn[0], newIn[1]))
			except Exception:
				print("Couldn't add alias '%s' ('%s')" % (newIn[0], newIn[1]))

	if lstAlias:
		out = "Found %i aliases...\n" % len(pyprompt_mdc.alias)
		for i in pyprompt_mdc.alias:
			out += "%s: %s\n" % (i, pyprompt_mdc.alias[i])
		print(out[:-1])
