import sys

def check_high(line):
    return line.strip() == "HIGH"

print("hlol")
with open('out.txt', 'r') as f:
    for line in f.readlines():
        if check_high(line):
            print("High Vulnerability Found, Blocked")
            sys.exit(2)
        else:
            sys.exit(0)
