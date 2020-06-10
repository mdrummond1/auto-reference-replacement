import xml.etree.ElementTree as ET
from itertools import cycle

esv = ET.parse('bibles/ESV')
""" kjv = ET.parse('bibles/KJV.xmm')
nasb = ET.parse('bibles/NASB.xmm')
nkjv = ET.parse('bibles/NKJV.xmm') """

bible = esv.getroot()
notes = open("test.txt")
count = 0
notes = notes.read().split()

#print(notes)


for word in notes:
    if word[0] == '~':
        if (notes.index(word) + 1 != len(notes)):
            book = word[1:]
            chapter = int(notes[notes.index(word)+1].split(':')[0]) - 1
            print(notes[notes.index(word)+1].split(':'))
            verse = int(notes[notes.index(word)+1].split(':')[1]) - 1
            print("{} {}:{} - ".format(book, chapter + 1, verse + 1))
            for bookNDX in bible:
                
                if bookNDX.attrib['n'].lower() == book.lower():
                    print(bookNDX[chapter][verse].text)




       

                      

