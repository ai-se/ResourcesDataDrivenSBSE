

import bibtexparser

with open('bib.bib') as bibtex_file:
    bibtex_str = bibtex_file.read()

bib_database = bibtexparser.loads(bibtex_str)
d = bib_database.get_entry_dict()



# Checking for duplicates
t = []
for key in d.keys():
    if key not in t:
        t.append(d[key]['title'].replace('\n', ' ').strip().lower())
    else:
        print key


# Cleaning the bib and create a new bib
new = []
for key in d.keys():
    t = {}
    try:
        t['ID'] = d[key]['ID']
        t['ENTRYTYPE'] = d[key]['ENTRYTYPE']
        t['title'] = d[key]['title'].replace('\n', ' ').strip()
        t['author'] = d[key]['author'].replace('\n', ' ').strip()
        if d[key]['ENTRYTYPE'] != 'book':
            if 'journal' in d[key].keys():
                t['journal'] = d[key]['journal']
            elif 'booktitle' in d[key].keys():
                t['booktitle'] = d[key]['booktitle']
            else:
                print '>> ', d[key]
        else:
            t['publisher'] = d[key]['publisher']

        t['year'] = d[key]['year']

    except:
        print key, d[key]


    new.append(t)

from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase

db = BibDatabase()
db.entries = new
writer = BibTexWriter()
writer.indent = '    '
with open('new_bib.bib', 'w') as bibfile:
    bibfile.write(writer.write(db))