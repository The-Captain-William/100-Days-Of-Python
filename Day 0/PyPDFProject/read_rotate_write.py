import PyPDF2
from pathlib import Path

pdf = Path("PDF Files/first.pdf")  # path object points to pdf
with open(pdf, "rb") as file:  # rb = read in binary; with statement for auto close; file is object
    reader = PyPDF2.PdfReader(file)  # reading file
    print(reader.numPages)  # returns pages in pdf
    page = reader.getPage(0)  # index of page
    page.rotateClockwise(90)  # parameter in degrees
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)  # .insert page does same but with index param; writing page
    with open("rotated.pdf", "wb") as output:  # write binary
        writer.write(output)
