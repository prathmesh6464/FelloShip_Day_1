from sys import argv
cmdargv=int(argv[1])
if 0<=cmdargv<31:
	for i in range(cmdargv+1):
		print(2**i)
	