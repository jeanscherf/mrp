



#!/usr/bin/python3
from bs4 import BeautifulSoup
import csv
import os
import sys
import subprocess

if len(sys.argv) < 2:
    print("Parser - version 0.1")
    print("")
    print("Usage: python "+sys.argv[0]+" <PDF file> [optional: file type]")
    print("")
    quit()
else :
    ifile = sys.argv[1]
    xmlfile = os.path.splitext(ifile)[0]+".xml"
    pdffile = os.path.splitext(ifile)[0]+".pdf"
    csvfile = os.path.splitext(ifile)[0]+".csv"
    jsonfile = os.path.splitext(ifile)[0]+".json"
    yamlfile = os.path.splitext(ifile)[0]+".yaml"

print("file: "+sys.argv[1])

print("Converting PDF to XML...")
# substitute os.system for subprocess
xml = subprocess.run(['pdftohtml', '-s', '-i', '-xml', pdffile])
#os.system("pdftohtml -s -i -xml "+pdffile+" "+xmlfile)

page3 = []
row = []
top = 0
c = 0
pagenumber = ['3', '4']

if ((len(sys.argv)==3 and sys.argv[2]=='csv')  or len(sys.argv) < 3) :
    print("Generating CSV...")
    writer = csv.writer(open(csvfile, "w"), delimiter=";")
    with open(xmlfile) as fd:
        soup = BeautifulSoup(fd.read(), 'xml')
        for page in soup.find_all('page', number=pagenumber):
            for text in page.find_all('text', font=2):
                old_top = top
                top = text['top']

                t = len(page.find_all('text', top=top))

                if top != old_top:
                    c = 1
                    page3.append(row)
                    row = [text.string]
                else:
                    c += 1
                    if (c == t & c == 3):
                        row.append('')
                    row.append(text.string)

    page3.append(row)
    writer.writerows(page3)

elif (sys.argv[2]=='json'):
    print("Generating JSON...")

elif (sys.argv[2]=='yaml'):
    print("Generating YAML...")

else :
    print("Oops... file type not recognized.")


print("Completed!")
