#!/usr/bin/python3
from bs4 import BeautifulSoup
import csv

page3 = []
row = []
top = 0
c = 0

writer = csv.writer(open("Lauterstein-Bretten.csv", "w"), delimiter=";")
with open('Lauterstein-Bretten.xml') as fd:
    soup = BeautifulSoup(fd.read(), 'xml')
    for page in soup.find_all('page', number='3'):
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

writer.writerows(page3)
