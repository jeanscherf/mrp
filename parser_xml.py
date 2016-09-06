#!/usr/bin/python3
from bs4 import BeautifulSoup
import csv

page3=[]
row=[]
top=0
writer = csv.writer(open("Lauterstein-Bretten.csv", "w"), delimiter = ";")
with open('Lauterstein-Bretten.xml') as fd:
  soup = BeautifulSoup(fd.read(), 'xml')
  for page in soup.find_all('page',number='3'):
    for text in page.find_all('text',font=2):
      old_top = top
      top = text['top']
      if top != old_top:
        page3.append(row)
        row = [text.string]
      else:
        row.append(text.string)
writer.writerows(page3)
