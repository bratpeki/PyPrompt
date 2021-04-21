
from platform import uname
from getpass import getuser

import source.pyprompt_version as pyprompt_version

keys = {
	"$user": [getuser(), "Returns the system's username"],
	"$system": [uname()[0], "Returns the system name"],
	"$node": [uname()[1], "Returns the computer’s network name"],
	"$release": [uname()[2], "Returns the system's release"],
	"$build": [uname()[3], "Returns the system's build release"],
	"$machine": [uname()[4], "Returns the machine type"],
	"$processor": [uname()[5], "Returns the (real) processor name"],

	"$version": [pyprompt_version.getVersion(), "Returns the current version of PyPrompt"]
}
