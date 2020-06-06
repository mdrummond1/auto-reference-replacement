import xml.etree.ElementTree as ET

esv = ET.parse('bibles/ESV')
sql = open("bibleQueries.sql", 'w')
bible = esv.getroot()


userChoice = ''

while (userChoice != 'n'):
    userBook = input("enter book\n")

    userChapter = input("enter chapter\n")

    userVerse = input("enter verse\n")
    for book in bible:
        #sql.write(book.attrib['n'])
        if book.attrib['n'] == userBook:
        
            for chapter in book:
                #sql.write("\n\t\tChapter " + chapter.attrib['n'])
                if chapter.attrib['n'] == userChapter:
                
                    for verse in chapter:
                        #sql.write("\t\t\t" + str(verse.attrib['n']) + " " + str(verse.text) + "\n")
                        #print("\t\t\t" + str(verse.attrib['n']) + " " + str(verse.text) + "\n")
                        if verse.attrib['n'] == userVerse:
                            print(book.attrib['n'] + " " + chapter.attrib['n'] + ":" + verse.attrib['n'] + "-" + verse.text)
                            break

    userChoice = input("Search Again? (y/n)\n")
                        

