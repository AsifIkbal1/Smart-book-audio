import pyttsx3
import PyPDF2
book=open('OOP.pdf','rb')
pdf=PyPDF2.PdfFileReader(book)
variable=pyttsx3.init()
for i in range(7,111):
    page=pdf.getPage(i)
    text=page.extractText()
    variable.say(text)
    variable.runAndWait()




