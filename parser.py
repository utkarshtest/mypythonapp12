def check_high(line):
    return line.strip() == "HIGH"


with open('out.txt', 'r') as f:
    for line in f.readlines():
        if check_high(line):
            print("High Vulnerability Found, Blocked")