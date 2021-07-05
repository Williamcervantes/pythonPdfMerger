import os, PyPDF2

#Ask user where the PDFs are
userpdflocation='C:\\Users\\Dev\\Desktop\\new'

#Sets the scripts working directory to the location of the PDFs
os.chdir(userpdflocation)

#Ask user for the name to save the file as
userfilename=input('What should I call the file?')

#Get all the PDF filenames
pdf2merge = []
userpdflocation

for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdf2merge.append(filename)

pdf2merge = list(reversed(pdf2merge))

pdfWriter = PyPDF2.PdfFileWriter()

#loop through all PDFs
for file in pdf2merge:
    pdfFileObj = open(file,'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    for pageNum in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
    
#save PDF to file, wb for write binary
pdfOutput = open(userfilename+'.pdf', 'wb')
#Outputting the PDF
pdfWriter.write(pdfOutput)
#Closing the PDF writer
pdfOutput.close()
print(pdf2merge)
