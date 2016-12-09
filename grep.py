import sys

for s in sys.stdin:
	if s.find(sys.argv[1])!=-1:
		print(s[:s.find(sys.argv[1])],'\033[32m',sys.argv[1],'\033[0m',s[s.find(sys.argv[1])+len(sys.argv[1]):])