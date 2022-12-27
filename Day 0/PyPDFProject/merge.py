import PyPDF2

merger = PyPDF2.PdfMerger()
file_names = ["first.pdf", "second.pdf"] # example of hardcoding. .pdf merged in memory, needs to be written
for file_name in file_names:
    merger.append(file_name)
merger.write("combined.pdf")  # merger accepts File object

