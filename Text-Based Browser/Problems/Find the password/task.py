from lxml import etree

#xml_string = '<profile><account login="login" password="secret"/></profile>'
#xml_string = '<result><webpage link="hyperskill.com"></webpage><users><!-- Random comment --><user id="239" password="qwerty"><info email="a@a.a"/></user></users></result>'

def find_password(xml_string):
    root = etree.fromstring(xml_string)
    for el in root:
        return el.get('password')


