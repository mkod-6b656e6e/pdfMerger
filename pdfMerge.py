#!/usr/bin/python

from PyPDF2 import PdfFileMerger

pdfs = ['c1.pdf', 'c2.pdf', 'c3.pdf', 'c4.pdf', 'c5.pdf', 'c6.pdf', 'c7.pdf', 'c8.pdf', 'c10.pdf']

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(open(pdf, 'rb'))

with open('complete.pdf', 'wb') as fout:
    merger.write(fout)

print "Done."