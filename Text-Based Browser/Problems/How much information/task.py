from lxml import etree

xml_string = input()
root = etree.fromstring(xml_string)
x = len(root)
y = len(root.keys())
print(x, y)
