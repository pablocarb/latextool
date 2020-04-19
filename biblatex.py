#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 14:20:42 2020

@author: Pablo Carbonell

Extract doi and generate bibtex file.
"""
from doi2bib.crossref import get_bib_from_doi
import argparse
import re

def arguments():
    parser = argparse.ArgumentParser(description='Generate bib file from a LaTeX document using doi citations. Pablo Carbonell, Universitat Politecnica de Valencia, 2020')
    parser.add_argument('tex',
                        help='Latex input file.')
    parser.add_argument('bib',
                        help='Bibtex output file.')
    return parser

if __name__ == '__main__':
    parser = arguments()
    args = parser.parse_args()
    f = args.tex
    dois = set()
    with open(f) as h:
        for line in h:
            for x in re.findall('{doi:([^}]*)}',line):
                for y in x.split(','):
                    y = re.sub(' ','',y)
                    if not y.startswith('doi:'):
                        y = 'doi:'+y
                    dois.add(y)
    with open(args.bib, 'w') as upv:
        for y in dois:
            out = get_bib_from_doi(y)
            if out[0]:
                x = out[1].split(',')
                x[0] = re.sub('{[^,]*','{'+y,x[0])
                bib = ','.join(x)
                try:
                    upv.write(bib.encode('UTF-8')+'\n')
                except:
                    import pdb; pdb.set_trace()
