import re

string = 'Backslash is your best friend, right?'
string = re.escape(string)
print(string)