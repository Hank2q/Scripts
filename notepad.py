import sys

file = sys.argv[1]
with open(file) as f:
    print(f.read())
