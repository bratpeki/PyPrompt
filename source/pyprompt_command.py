import source.pyprompt_mdc as mdc

from subprocess import call


def printStartUp():
	print("PyPrompt v" + mdc.pyprompt_user.keys["$version"][0])
	print("=" * 10)
	print("User:", mdc.pyprompt_user.keys["$user"][0])
	print("System:", mdc.pyprompt_user.keys["$system"][0])
	print("Node:", mdc.pyprompt_user.keys["$node"][0])
	print("Release:", mdc.pyprompt_user.keys["$build"][0])
	print("Machine:", mdc.pyprompt_user.keys["$machine"][0])
	print("Processor:", mdc.pyprompt_user.keys["$processor"][0])
	print("=" * 10)


def getHelp(IsHelp, com, args=None):
	if IsHelp:
		return com.__doc__
	else:
		return com(args) if args is not None else com()


def checkCom(rawCom):

	InMarks, IsHelp = False, False
	word, words = "", []

	if rawCom != "":

		while rawCom.count('"') % 2 != 0:
			rawCom += input(mdc.pyprompt_global.PS2)

		# alias rendering
		for alIn in mdc.alias:
			rawCom = rawCom.replace(f"%{alIn}", f'{mdc.alias[alIn]}')

		for i in rawCom + " ":

			if i == '"':
				InMarks = not InMarks
			elif InMarks or (not InMarks and i != " "):
				word += i
			elif word.strip() != "":
				words.append(word.strip())
				word = ""

		if not len(words):
			return

		if words[0].lower() == "help":
			if len(words) == 1:
				print("You should choose which function you need help with. Check pyprompt_command.")
				return
			IsHelp = True
			words = words[1:]
		key = words[0].lower()

		# global
		if rawCom == "exit":
			for var in locals():
				del var
			exit()

		# pyprompt_alias
		if key == "alias":
			out = getHelp(IsHelp, mdc.pyprompt_alias.aliasMgmt, words[1:])

		# pyprompt_dir_file
		if key == "del":
			out = getHelp(IsHelp, mdc.pyprompt_dir_file.deleteDirFile, words[1:])
		if key == "mk":
			out = getHelp(IsHelp, mdc.pyprompt_dir_file.makeDirFile, words[1:])
		if key == "rn":
			out = getHelp(IsHelp, mdc.pyprompt_dir_file.renameDirFile, words[1:])

		# pyprompt_dir
		if key == "cd":
			out = getHelp(IsHelp, mdc.pyprompt_dir.changeDir, words[1:])
		if key == "dir":
			out = getHelp(IsHelp, mdc.pyprompt_dir.listDir, words[1:])

		# pyprompt_file
		if key == "read":
			out = getHelp(IsHelp, mdc.pyprompt_file.readFile, "".join(words[1:]))

		# pyprompt_mdc
		if key == "echo":
			out = getHelp(IsHelp, mdc.echo, "".join(words[1:]))

		# pyprompt_online
		if key == "duckduckgo":
			out = getHelp(IsHelp, mdc.pyprompt_online.DuckDuckGo, "".join(words[1:]))
		if key == "github":
			out = getHelp(IsHelp, mdc.pyprompt_online.GitHub, words[1:])
		if key == "google":
			out = getHelp(IsHelp, mdc.pyprompt_online.Google, "".join(words[1:]))
		if key == "instagram":
			out = getHelp(IsHelp, mdc.pyprompt_online.Instagram, "".join(words[1:]))
		if key == "link":
			out = getHelp(IsHelp, mdc.pyprompt_online.GoToLink, "".join(words[1:]))
		if key == "soundcloud":
			out = getHelp(IsHelp, mdc.pyprompt_online.SoundCloud, "".join(words[1:]))
		if key == "stackoverflow":
			out = getHelp(IsHelp, mdc.pyprompt_online.StackOverflow, "".join(words[1:]))
		if key == "twitter":
			out = getHelp(IsHelp, mdc.pyprompt_online.Twitter, "".join(words[1:]))
		if key == "youtube":
			out = getHelp(IsHelp, mdc.pyprompt_online.YouTube, "".join(words[1:]))

		# pyprompt_system
		if key == "cpuinfo":
			out = getHelp(IsHelp, mdc.pyprompt_system.getCPUInfo, None)
		if key == "kill":
			out = getHelp(IsHelp, mdc.pyprompt_system.killProcess, words[1:])
		if key == "meminfo":
			out = getHelp(IsHelp, mdc.pyprompt_system.getMemInfo, None)
		if key == "proc":
			out = getHelp(IsHelp, mdc.pyprompt_system.getActiveProc, words[1:])

		# pyprompt_time
		if key == "time":
			out = getHelp(IsHelp, mdc.pyprompt_time.getTime, words[1:])

		if "out" in locals():
			if out is not None:
				print(out)
		elif mdc.settings["runCommandIfNotFound"]:
			try:
				call(mdc.settings["runCommandIfNotFoundPrefix"] + rawCom, shell=True)
			except Exception:
				call(rawCom, shell=True)
