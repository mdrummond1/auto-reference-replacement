import docx2txt as dt

doc = dt.process("Hello world.docx").split()
ref = ""
for word in doc:
    print(word)

print(doc)

