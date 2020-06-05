import re


def matched(template, string):
    match = re.match(template, string)
    if match == None:
        print(False)
    else:
        print(True)


matched('Fra', 'Frank')
