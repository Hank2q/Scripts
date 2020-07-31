import PyPDF2
pdf_file = open(r'pdf\meetingminutes.pdf', 'rb')
reader = PyPDF2.PdfFileReader(pdf_file)
reader.decrypt('Fuck_u')
pages = reader.numPages
writer = PyPDF2.PdfFileWriter()
for page in range(pages):
    pageObj = reader.getPage(page)
    writer.addPage(pageObj)
writer.encrypt('Fuck_u')
with open('pdf/combinedminutes.pdf', 'wb') as pdf:
    writer.write(pdf)

# pdfFile = open('pdf/encrypted.pdf', 'rb')
# reader = PyPDF2.PdfFileReader(pdfFile)
# reader.decrypt('rosebud')
# print(reader.getPage(1).extractText())
