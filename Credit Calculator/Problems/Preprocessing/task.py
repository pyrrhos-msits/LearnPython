txt = input()
# txt1 = txt.replace(',', '')
# txt2 = txt1.replace('.', '')
# txt3 = txt2.replace('?','')
# txt4 = txt3.replace('!','')
# print(txt4.lower())

# print(txt.lower().replace(',','').replace('.','').replace('!','').replace('?',''))
els = [',', '.', '!', '?']
for el in els:
    if el in txt:
        txt = txt.replace(el, '')
print(txt.lower())
