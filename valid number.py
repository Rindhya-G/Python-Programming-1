import re
def is_valid_number(s):
    pattern = re.compile(r'^[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?$') 
    match = pattern.match(s)
    print(bool(match))
is_valid_number("0")
