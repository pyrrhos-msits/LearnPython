#  Posted from EduTools plugin
#a = 'First ladies rule the State and state the rule: ladies first'.split()
a = input().split()
w_list = []
for word in a:
    if word.endswith('s'):
        w_list.append(word)
        w_list.append('_')

# l = len(w_list) - 1
# w_list.pop(l)
# print(''.join(w_list))
if len(w_list) > 1:
    w_list.pop(len(w_list)-1)
    print(''.join(w_list))
