import re

try:
    file = open("A141481" , "r")
except IOError:
    print("*** ERROR: Could not open file for reading #A141481 number sequence values ***")
    raise SystemExit

input_val = 347991
input_line = None
term = None

while True:
    input_line = file.readline()
    term = re.findall("\d+" , input_line)
    if (int(term[1]) > input_val):
        print(term[1])
        break
