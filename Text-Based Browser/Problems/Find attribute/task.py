from lxml import etree

xml_string = input()
atr_name = input()
root = etree.fromstring(xml_string)
print(root.get(atr_name))
