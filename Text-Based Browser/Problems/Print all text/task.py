from lxml import etree

root = etree.fromstring(input())
for el in root:
    print(el.text)
