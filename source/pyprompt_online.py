from webbrowser import open_new_tab as _op_
from urllib.request import urlopen


def connected(url="https://www.google.com/", timeout=1):
	try:
		urlopen(url, timeout=timeout)
		return True
	except Exception:
		return False


def GoToLink(link):
	if link != "":
		if connected():
			_op_(link)
			return "Opening link '%s' in default browser" % link
		else:
			return "Could not connect to The Internet"
	else:
		return "No link specified."


def DuckDuckGo(keyword):
	"""
	Open or search DuckDuckGo
	"""

	if connected():
		if keyword == "":
			_op_("https://duckduckgo.com/")
			return "Opening DuckDuckGo"
		else:
			_op_("https://duckduckgo.com/" + keyword)
			return "Searching up '%s' on DuckDuckGo" % keyword
	else:
		return "Could not connect to DuckDuckGo"


def Google(keyword):
	"""
	Open or search Google
	"""

	if connected():
		if keyword == "":
			_op_("https://www.google.com/")
			return "Opening Google"
		else:
			_op_("https://www.google.com/search?q=" + keyword)
			return "Searching up '%s' on Google" % keyword
	else:
		return "Could not connect to Google"


def Instagram(keyword):
	"""
	Open or search Instagram
	"""

	if connected():
		if keyword == "":
			_op_("https://instagram.com/")
			return "Opening Instagram"
		elif keyword[0] == "#":
			_op_("http://instagram.com/explore/tags/" + keyword[1:])
			return "Searching up '#%s' on Instagram" % keyword[1:]
		else:
			_op_("https://instagram.com/" + keyword)
			return "Searching up user '%s' on Instagram" % keyword
	else:
		return "Could not connect to The Internet"


def YouTube(keyword):
	"""
	Open or search YouTube
	"""

	if connected():
		if keyword == "":
			_op_("https://www.youtube.com/")
			return "Opening YouTube"
		else:
			_op_("https://www.youtube.com/search?q=" + keyword)
			return "Searching up '%s' on YouTube" % keyword
	else:
		return "Could not connect open Youtube"


def Twitter(keyword):
	"""
	Open or search Twitter
	"""

	if connected():
		if keyword == "":
			_op_("https://twitter.com/")
			return "Opening Twitter"
		else:
			_op_("https://twitter.com/search?q=" + keyword)
			return "Searching up '%s' on Twitter" % keyword
	else:
		return "Could not connect to The Internet"


def StackOverflow(keyword):
	"""
	Open or search StackOverflow
	"""

	if connected():
		if keyword == "":
			_op_("https://stackoverflow.com/")
			return "Opening StackOverflow"
		else:
			_op_("https://stackoverflow.com/search?q=" + keyword)
			return "Searching up '%s' on StackOverflow" % keyword
	else:
		return "Could not connect to StackOverflow"


def SoundCloud(keyword):
	"""
	Open or search SoundCloud
	"""

	if connected():
		if keyword == "":
			_op_("https://soundcloud.com/")
			return "Opening SoundCloud"
		else:
			_op_("https://soundcloud.com/search/people?q=" + keyword)
			return "Searching up '%s' on SoundCloud" % keyword
	else:
		return "Could not connect to SoundCloud"


def GitHub(args):
	"""
	Open or search GitHub

	Arguments:

		-any	   Search type: Any
		-code	  Search type: Code
		-commit	Search type: Commit
		-issue	 Search type: Issue
		-repo	  Search type: Repo
		-user	  Search type: User

	Examples:

		root> github -code "import os"
		root> github -any legacy
	"""

	if connected():
		if not bool(len(args)):
			_op_("https://github.com/")
			return "Opening GitHub"

		argCount = 0
		for arg in args:
			argCount += 1

			if arg.lower() == "-code":
				try:
					_op_("https://github.com/search?q=%s&type=Code" % args[argCount])
					return "Searching for '%s'..." % args[argCount]
				except Exception:
					return "Argument corresponding to -code not specified"
			elif arg.lower() == "-repo":
				try:
					_op_(
						"https://github.com/search?q=%s&type=Repositories"
						% args[argCount]
					)
					return "Searching for '%s'..." % args[argCount]
				except Exception:
					return "Argument corresponding to -repo not specified"
			elif arg.lower() == "-commit":
				try:
					_op_("https://github.com/search?q=%s&type=Commits" % args[argCount])
					return "Searching for '%s'..." % args[argCount]
				except Exception:
					return "Argument corresponding to -commit not specified"
			elif arg.lower() == "-issue":
				try:
					_op_("https://github.com/search?q=%s&type=Issues" % args[argCount])
					return "Searching for '%s'..." % args[argCount]
				except Exception:
					return "Argument corresponding to -issue not specified"
			elif arg.lower() == "-user":
				try:
					_op_("https://github.com/search?q=%s&type=Users" % args[argCount])
					return "Searching for '%s'..." % args[argCount]
				except Exception:
					return "Argument corresponding to -user not specified"
			elif arg.lower() == "-any":
				try:
					_op_("https://github.com/search?q=%s" % args[argCount])
					return "Searching for '%s'..." % args[argCount]
				except Exception:
					return "Argument corresponding to -any not specified"
	else:
		return "Could not connect to GitHub"
