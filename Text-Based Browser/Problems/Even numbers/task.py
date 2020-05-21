n = int(input())


def even(num):
    ev = 0
    ct = 0
    while ct < num:
        yield ev
        ct += 1
        ev += 2

evenprt = even(n)
for _ in range(n):
    print(next(evenprt))
