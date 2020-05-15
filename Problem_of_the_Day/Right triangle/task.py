class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2
        self.S = 0.5 * (leg_1 * leg_2)


hyp, leg_1, leg_2 = input().split()
hyp = int(hyp)
leg_1 = int(leg_1)
leg_2 = int(leg_2)

my_triangle = RightTriangle(hyp, leg_1, leg_2)

if my_triangle.c ** 2 == (my_triangle.a ** 2) + (my_triangle.b ** 2):
    print(my_triangle.S)
else:
    print('Not right')




