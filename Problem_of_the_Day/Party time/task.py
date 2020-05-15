guestlist = []
name = ''
while name != '.':
    name = input()
    if name != '.':
        guestlist.append(name)
if len(guestlist) > 0:
    print(guestlist)
    print(len(guestlist))