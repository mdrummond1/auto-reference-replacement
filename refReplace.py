import xml.etree.ElementTree as ET

esv = ET.parse('bibles/ESV')
bible = esv.getroot()
notes = open("test.txt")
count = 0
notes = notes.read().split()
print(notes)

ref = []

for word in notes:
    if word[0] == '~':
        ref.append(word)

print(ref)

'''for book in bible:
    
    for chapter in book:
                #sql.write("\n\t\tChapter " + chapter.attrib['n'])
  #              if chapter.attrib['n'] == userChapter:
                
        for verse in chapter:
                        #sql.write("\t\t\t" + str(verse.attrib['n']) + " " + str(verse.text) + "\n")
                        #print("\t\t\t" + str(verse.attrib['n']) + " " + str(verse.text) + "\n")
 #                       if verse.attrib['n'] == userVerse:
            print(book.attrib['n'] + " " + chapter.attrib['n'] + ":" + verse.attrib['n'] + "-" + verse.text)
            count = count + 1
            print("There are " + str(count) + " verses in the Bible")
#    userChoice = input("Search Again? (y/n)\n")
  '''                      

