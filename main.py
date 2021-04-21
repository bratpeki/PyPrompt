
from sys import argv

if __name__ == "__main__":

	import source.pyprompt_command as pyprompt_command

	if len(argv) == 1:
		pyprompt_command.printStartUp()
		while True:
			for i in input(
				pyprompt_command.mdc.pyprompt_global.PS1()).split(
				pyprompt_command.mdc.settings["commandSpliter"]
			):
				pyprompt_command.checkCom(i)
	else:
		for arg in argv[1:]:
			for line in open(arg).readlines():
				pyprompt_command.checkCom(line[:-1])
