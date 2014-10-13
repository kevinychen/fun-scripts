#!/bin/python

from subprocess import call
from os import listdir

# Convert Word documents to pdf
for f in listdir('.'):
    if f.endswith('.doc') or f.endswith('.docx'):
        call(['soffice', '--headless', '--convert-to', 'pdf', f])

# Print all pdfs
for f in listdir('.'):
    if f.endswith('.pdf'):
        call(['lpr', '-o', 'sides=two-sided-long-edge', f])
        print 'printing', f

