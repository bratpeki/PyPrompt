from psutil import process_iter, virtual_memory, cpu_percent, Process  # NOT STDLIB

import source.pyprompt_common_func as pyprompt_common_func


def _append_(All, pID, CTime, UsedCPU, UsedMem, UsedMemPer, i):

	A_, p_, ct_, uC_, uM_, uMP_ = 0, 0, 0, 0, 0, 0
	if i.pid != 0:
		All.append(i.name())
		A_ = pyprompt_common_func.getLongestWord(All)

		pID.append(str(i.pid))
		p_ = pyprompt_common_func.getLongestWord(pID)

		CTime.append(pyprompt_common_func.formatTime(i.create_time()))
		ct_ = pyprompt_common_func.getLongestWord(CTime)

		UsedCPU.append(str(i.cpu_percent()))
		uC_ = pyprompt_common_func.getLongestWord(UsedCPU)

		UsedMem.append(str(i.memory_info().rss))
		uM_ = pyprompt_common_func.getLongestWord(UsedMem)

		UsedMemPer.append(
			str(round(i.memory_info().rss / virtual_memory().total * 100, 4))
		)
		uMP_ = pyprompt_common_func.getLongestWord(UsedMemPer)

	return A_, p_, ct_, uC_, uM_, uMP_


def getMemInfo():
	"""
	Get information about the use of active memory on the level of the entire system

	Examples:

		root> meminfo
		ACTIVE MEMORY: Used/Available: 5451214848(32.426745%)/11359645696(67.573255%) (Total: 16810860544)
	"""

	VM = virtual_memory()
	pcAllMem, pcUsedMem, pcAvaMem = VM.total, VM.used, VM.available
	print(
		"ACTIVE MEMORY: Used/Available: %i(%f%%)/%i(%f%%) (Total: %i)"
		% (
			pcUsedMem,
			pcUsedMem / pcAllMem * 100,
			pcAvaMem,
			pcAvaMem / pcAllMem * 100,
			pcAllMem,
		)
	)


def getCPUInfo():
	"""
	Get information about the use of the CPU on the level of the entire system

	Examples:

		root> cpuinfo
		CPU: Used/Available: 34.400000/65.600000
	"""

	CPUUsed = cpu_percent()
	CPUAva = 100 - CPUUsed
	print("CPU: Used/Available: %f/%f" % (CPUUsed, CPUAva))


def getActiveProc(args):
	"""
	Iterate over all running processes

	Arguments:

		-s	Search through all running processes
		-e	Specify if the search argument must be explicit
		-t	Return only the process table, without the additional processes

	Examples:

		root> proc -s host.exe -e -t
		Name			| pID   | Time Created		| CPU | Memory   | Memory %
		svchost.exeg	| 240   | 2020-06-26 16:30:01 | 0.0 | 7868416  | 0.0468
		svchost.exeg	| 428   | 2020-06-24 08:18:17 | 0.0 | 12623872 | 0.0751
		svchost.exeg	| 868   | 2020-06-24 08:18:17 | 0.0 | 4444160  | 0.0264
		svchost.exeg	| 964   | 2020-06-24 08:18:16 | 0.0 | 991232   | 0.0059
		fontdrvhost.exe | 984   | 2020-06-24 08:18:16 | 0.0 | 380928   | 0.0023
	"""

	finding_name = []

	IsExplicit = False
	IsOnlyTable = False

	argCount = 0
	for arg in args:
		argCount += 1

		if arg.lower() == "-s":
			try:
				finding_name.append(args[argCount])
			except Exception:
				return "Argument corresponding to -s not specified"

		if arg.lower() == "-e":
			IsExplicit = True
		if arg.lower() == "-t":
			IsOnlyTable = True

	if not IsOnlyTable:
		getMemInfo()
		getCPUInfo()

	All, pID, CTime, UsedCPU, UsedMem, UsedMemPer = (
		["Name"],
		["pID"],
		["Time Created"],
		["CPU"],
		["Memory"],
		["Memory %"],
	)

	out = ""

	try:
		for i in process_iter():
			IsOkay = True
			if len(finding_name) > 0:
				for N in finding_name:
					if N not in i.name() and IsExplicit:
						IsOkay = False
					if N.lower() not in i.name().lower() and not IsExplicit:
						IsOkay = False
				if IsOkay:
					A_, p_, ct_, uC_, uM_, uMP_ = _append_(
						All, pID, CTime, UsedCPU, UsedMem, UsedMemPer, i
					)
			else:
				A_, p_, ct_, uC_, uM_, uMP_ = _append_(
					All, pID, CTime, UsedCPU, UsedMem, UsedMemPer, i
				)

		if len(All) != 1:
			for i in range(len(All)):
				out += (
					f"%-{A_}s | %-{p_}s | %-{ct_}s | %-{uC_}s | %-{uM_}s | %-{uMP_}s\n"
					% (All[i], pID[i], CTime[i], UsedCPU[i], UsedMem[i], UsedMemPer[i])
				)

	except Exception:
		out = "Could not get running processes"

	return out


def killProcess(args):
	"""
	Kill a process or list of processes by their PID or name
	Inserting an integer searches for process PID's
	Inserting a non-integer type searches for the process name

	Arguments:

		-e	Specify if the command argument must be explicit

	Options:

		Y	  Yes
		N	  No
		YA	 Yes All
		NA	 No All

	Examples:

		root> kill python
		8 processes found.
		python.exe, 4036
		python.exe, 4604
		python.exe, 11112
		python.exe, 13836
		python.exe, 15324
		python.exe, 17196
		python.exe, 27328
		python.exe, 27700
		Do you wish to kill python.exe (PID: 4036)? [Y/N/YA/NA]
		...

		root> kill 7412
		7412 corresponds to python.exe. Do you wish to kill this process? [Y/N]
	"""

	IsExplicit = False

	argCount = 0
	for arg in args:
		argCount += 1

		if arg.lower() == "-e":
			IsExplicit = True
			args.remove(arg)

	for proc in args:

		procList = []
		try:
			proc = int(proc)
			try:
				p = Process(proc)
				if (
					input(
						"%i corresponds to %s. Do you wish to kill this process? [Y/N] "
						% (proc, p.name())
					)
					.lower()
					.strip()
					== "y"
				):
					try:
						p.kill()
						print("Successfully ended the given process")
					except Exception:
						print("Could not kill process")
			except Exception:
				print("Could not find a process corresponding to the PID %i" % proc)
		except Exception:
			for i in process_iter():
				if proc.lower() in i.name().lower() and not IsExplicit:
					procList.append([i.name(), i.pid])
				if proc in i.name() and IsExplicit:
					procList.append([i.name(), i.pid])

		if len(procList) > 0:

			print("%i processes found." % len(procList))
			for i in procList:
				print(f"{i[0]}, {i[1]}")

			while len(procList):
				i = procList[0]
				inp = (
					input(
						"Do you wish to kill %s (PID: %i)? [Y/N/YA/NA] " % (i[0], i[1])
					)
					.lower()
					.strip()
				)

				if inp == "y":
					try:
						Process(i[1]).kill()
						print("Successfully ended the given process")
					except Exception:
						print("Could not kill process")
				elif inp == "n":
					print("Skipping current process")
				elif inp == "ya":
					for j in procList:
						try:
							Process(j[1]).kill()
							print("Successfully ended: %s (%i)" % (j[0], j[1]))
						except Exception:
							print("Could not end %s (%i)" % (j[0], j[1]))
					return
				elif inp == "na":
					return "Stopping..."
				else:
					continue

				procList = procList[1:]

		else:
			print("No processes correspoding to: %s" % proc)
