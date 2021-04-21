from time import ctime, strftime, gmtime


def getLongestWord(i):
	ret = 0
	for j in i:
		ret = len(j) if (len(j) > ret) else ret
	return str(ret)


def formatTime(i):
	return strftime("%Y-%m-%d %H:%M:%S", gmtime(i))
