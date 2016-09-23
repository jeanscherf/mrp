# MatchReportParser
It creates an XML file from a PDF file (March Report) and parses it to one chosen file type.
The possible file types are csv, JSON and YAML.

BeautifulSoup search and filtering capabilities are used to extract the _Zeit, Spielzeit, Spielstand, Aktion_ fields from the MatchReport for the table 3.
BeautifulSoup requires an xml parser and they recommend *lxml*.

## Prerequisites
#### Python 3
#### BeautifulSoup 4 and lxml parser
On Debian/Ubuntu:
`$ apt-get install python-bs4 python-lxml`

On Arch Linux:
`$ pacman -S python-beautifulsoup4 python-lxml`

Using pip:
`$ pip install beautifulsoup4 lxml`

#### pdftohtml from poppler
Normally installed in several Linux distros

On Debian/Ubuntu:
`$ apt-get install poppler-utils`

On Arch Linux:
`$ pacman install poppler`

Usage:
`python parser_xml.py <PDF file> [optional: file type]`

## TODO
* It parses just to csv. JSON and YAML yet to come functional.
* Table 1 comes next
* Skip the xml creation. Maybe pipe from stdout.
