import sys

for s in sys.stdin:
	if s.find(sys.argv[1])!=-1:
		print(s)