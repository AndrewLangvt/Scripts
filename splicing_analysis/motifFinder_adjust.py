#! /usr/bin/env python3 

# motifFinder_adjust.py
# Andrew S. Lang
# Created: 24JUL2018
# Last Modified: 24JUL2018

# This script simply re-inputs the meta data from whippet output into a MotifFinder output file. 
# inputs include 1) Whippet diff.gz file
#                2) MotifFinder spreadsheet file

import sys
from collections import defaultdict

def gen_dict(whippetF):                                          # Generate id of chrom:start (exon) IDs and metadata (sex, tissue, treatment)
    whippet = open(whippetF, 'r')
    meta_dict = defaultdict(list)

    for line in whippet:
        sample = line.split('\t')[0]
        exon = line.split('\t')[3]
        chrom = exon.split(":")[0]
        loc = exon.split(":")[1]
        start = int(loc.split("-")[0])
        exonID = str.join(':',(chrom, str(start)))
        meta_dict[exonID].append(sample)
    return meta_dict

#    for key,value in meta_dict.items():
#        print(key +'\t'+ str(value))

def add_meta(whippetF, motifF):                                  # Parse through motif file and insert metadata
    sample_meta = gen_dict(whippetF)
    motifs = open(motifF, 'r')    
    newfile = ""

    for line in motifs:
        if line.startswith("Query"):
            first = "Sample"
            second = line.split('\t')[0].strip()                 # Removing the extra whitespace on either end as it was throwing off the 
            third = line.split('\t')[1].strip()                  # generation of a TSV file
            fourth = "Pfam ID"
            fifth = line.split('\t')[3].strip()
            newfile += '{}\t{}\t{}\t{}\t{}\n'.format(first, second, third, fourth, fifth)
        else:
            motifID = line.split('\t')[0].strip()
            name = line.split('\t')[1].strip()
            info = line.split('\t')[3].replace('"','').strip()
            pfamID = info.split(',')[0].strip()
            description = info.split(',')[1].strip()

            for sample in sample_meta[motifID]:
#                print(sample)
                newfile += '{}\t{}\t{}\t{}\t{}\n'.format(sample, motifID, name, pfamID, description)
    new = motifF.replace('spreadsheet.tsv', 'sheet_adjust.tsv')

    outfile = open(motifF.replace('spreadsheet.tsv', 'sheet_adjust.tsv'), 'w')
    outfile.write(newfile)
    outfile.close()

#    print(newfile)
if __name__ == '__main__':
    whippetFile = sys.argv[1]
    motifFile = sys.argv[2]
    add_meta(whippetFile, motifFile)
