1. Installiere lxml
-----------------------------------------------------------------------------------

from lxml import etree

2. Wir verwneden vorerst zwei klassen:
    - Element: repräsentiert ein Element im XML Dokument. Speichert alle Informationen
                über Tag Namen, Attribute und Verweise auf untergeordnete Elemente
    - ElementTree: repräsentiert das gesamte XML Dokument. Es enthält einige allgemeine
                Informationen zum XML Dokument wie Codierung, XML Version, sowie einen 
                Verweis auf das Stammelement des Dokuments

3. Vom Text zum XML
-------------------------------------------------------------------------------------
    - Analysen von xml geht entweder von einem Dokument oder von einer Zeichenfolge

3.1 Zeichenfolge analysieren:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    - mit fromstring()
        #Beispiel
        xml_string = xml_string = "<a><b>hello</b></a>"
        root = etree.fromstring(xml_string)
        print(type(root)) # <class 'lxml.etree._Element'>

3.2 XML aus Datei analysieren
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    - mit parse()
        # Beispiel
        xml_path = 'xml_file.xml'

        tree = etree.parse(xml_path)
        print(type(tree))  # <class 'lxml.etree._ElementTree'>

        root = tree.getroot()
        print(type(root))  # <class 'lxml.etree._Element'>

3.3 Drucken des XML Dokuments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    - mit dump()
    - nimmt ein Element und druckt es sauber formatiert aus
        # Beispiel
        xml_string = "<a><b>hello</b></a>"
        root = etree.fromstring(xml_string)
        
        etree.dump(root)
        # <a>
        #   <b>hello</b>
        # </a>  

4. Durchlaufen des XML tree
-------------------------------------------------------------------------------------
        # Beispieldokument
        xml_file = "xml_file.xml"
        root = etree.parse(xml_file).getroot()
        etree.dump(root)
        
        # <country>
        #   <name>United Stated of America</name>
        #   <capital>Washington</capital>
        #   <states>
        #     <state>California</state>
        #     <state>Texas</state>
        #     <state>Florida</state>
        #     <state>Hawaii</state>
        #   </states>
        # </country>



