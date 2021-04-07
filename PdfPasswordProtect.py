import PyPDF2
import os
def passProtect(_filename, password):
    filename, _ = os.path.splitext(_filename)
    try:
        pdfFile = open(filename+'.pdf', 'rb')
    except:
        return '''Could not open File.\nPlease make sure the file is in the same path\nOR\nEnter the file name correctly'''
    # Create reader and writer object
    if not len(password):
        return "Hey! You forgot to enter the Password!!!"
    try:
        pdfReader = PyPDF2.PdfFileReader(pdfFile)
        pdfWriter = PyPDF2.PdfFileWriter()
        # Add all pages to writer (accepted answer results into blank pages)
        for pageNum in range(pdfReader.numPages):
            pdfWriter.addPage(pdfReader.getPage(pageNum))
        # Encrypt with your password
        pdfWriter.encrypt(password)
        # Write it to an output file. (you can delete unencrypted version now)
        resultPdf = open(filename+'_encrypted.pdf', 'wb')
        pdfWriter.write(resultPdf)
        resultPdf.close()
        return "Success"
    except:
        return "Something's wrong! Failed to protect the file :'( "

if __name__ == "__main__":
    filename = input('Please Enter the file name (example.pdf): ')
    password = input('Please enter the password to encrypt your file: ')
    print(passProtect(filename,password))