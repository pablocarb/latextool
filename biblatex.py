#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 14:20:42 2020

@author: pablo

Extract doi and generate bibtex file.
"""
from doi2bib.crossref import get_bib_from_doi
import re

f = 'upvchapter.tex'
dois = set()
with open(f) as h:
    for line in h:
        for x in re.findall('{doi:([^}]*)}',line):
            for y in x.split(','):
                y = re.sub(' ','',y)
                if not y.startswith('doi:'):
                    y = 'doi:'+y
                dois.add(y)
with open('upv.bib', 'w') as upv:                
    for y in dois:
        out = get_bib_from_doi(y)
        if out[0]:
            x = out[1].split(',')
            x[0] = re.sub('{[^,]*','{'+y,x[0])
            bib = ','.join(x)
            print(bib)
            upv.write(bib+'\n')