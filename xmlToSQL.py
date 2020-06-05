import xml.etree.ElementTree as ET

tree = ET.parse('bibles/ESV')

root = tree.getroot()

for book in root:
    for chapter in book:
        print(chapter.attrib)
        for verse in chapter:
            print(verse.attrib)