#  Posted from EduTools plugin
students_score = int(input())
max_score = int(input())

x = (students_score / max_score)*100


# if x in range(90,100):
#     print('A')
# if x in range(80,89.9):
#     print('B')
# if x in range(70,79.9):
#     print('C')
# if x in range(60,69.9):
#     print('D')
# if x < 60:
#     print('F')

if x < 60:
    print('F')
elif x < 70:
    print('D')
elif x < 80:
    print('C')
elif x < 90:
    print('B')
elif x <= 100:
    print('A')
