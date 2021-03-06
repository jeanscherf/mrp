#!/usr/bin/python3
from bs4 import BeautifulSoup
import csv
import json
import os
import sys
import subprocess

if len(sys.argv) < 2:
    print("Parser - version 0.1")
    print("")
    print("Usage: python "+sys.argv[0]+" <XML file> [optional: file type]")
    print("")
    quit()
else:
    ifile = sys.argv[1]
    xmlfile = os.path.splitext(ifile)[0]+".xml"
    pdffile = os.path.splitext(ifile)[0]+".pdf"
    csvfile = os.path.splitext(ifile)[0]+".csv"
    jsonfile = os.path.splitext(ifile)[0]+".json"
    yamlfile = os.path.splitext(ifile)[0]+".yaml"

print("file: "+sys.argv[1])


def XMLpage1():
    page1 = []
    row = []
    top = 0
    c = 0
    pagenumber = ['1']
    with open(xmlfile) as fd:
        soup = BeautifulSoup(fd.read(), 'xml')
        for page in soup.find_all('page', number=pagenumber):
            for text in page.find_all('text', font=2):
                old_top = top
                top = text['top']

                t = len(page.find_all('text', top=top))

                if top != old_top:
                    c = 1
                    page1.append(row)
                    row = [text.string]
                else:
                    c += 1
                    if (c == t & c == 3):
                        row.append('')
                    row.append(text.string)
    page1.append(row)
    return page1


def XMLpage34():
    page34 = []
    row = []
    top = 0
    c = 0
    pagenumber = ['3', '4']
    with open(xmlfile) as fd:
        soup = BeautifulSoup(fd.read(), 'xml')
        for page in soup.find_all('page', number=pagenumber):
            for text in page.find_all('text', font=2):
                old_top = top
                top = text['top']

                t = len(page.find_all('text', top=top))

                if top != old_top:
                    c = 1
                    page34.append(row)
                    row = [text.string]
                else:
                    c += 1
                    if (c == t & c == 3):
                        row.append('')
                    row.append(text.string)
    page34.append(row)
    return page34

# substitute os.system for subprocess and skipping xmlfile creation
xml = subprocess.run(['pdftohtml', '-s', '-i', '-xml', pdffile])

# os.system("pdftohtml -s -i -xml "+pdffile+" "+xmlfile)


if ((len(sys.argv) == 3 and sys.argv[2] == 'csv') or len(sys.argv) < 3):
    # writer = csv.writer(open(csvfile, "w"), delimiter=";")
    # with open(csvfile, "w") as writer:
    #    writer = csv.writer(writer, delimiter=";")
    #    writer.writerows(XMLpage34())
    # print(XMLpage34())

    outputfile = os.path.splitext(ifile)[0]+"_12.csv"

    with open(outputfile, "w") as writer:
        writer = csv.writer(writer, delimiter=";")
        writer.writerows(XMLpage1())

    outputfile = os.path.splitext(ifile)[0]+"_34.csv"

    with open(outputfile, "w") as writer:
        writer = csv.writer(writer, delimiter=";")
        writer.writerows(XMLpage34())

elif (sys.argv[2] == 'json'):
    print("Generating JSON...")
    # JSON structure not yet defined. Just some tests:
    outputfile = os.path.splitext(ifile)[0]+"_12.json"

    with open(outputfile, "w") as writer:
        json.dump(XMLpage1(), writer, ensure_ascii=False)

    outputfile = os.path.splitext(ifile)[0]+"_34.json"

    with open(outputfile, "w") as writer:
        json.dump(XMLpage34(), writer, ensure_ascii=False)

elif (sys.argv[2] == 'yaml'):
    print("Generating YAML...")

else:
    print("Oops... file type not recognized.")


print("Completed!")
