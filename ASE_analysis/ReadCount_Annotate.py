#! /usr/bin/env python3 

# ReadCounter_Annotate.py
# Andrew S. Lang
# Created: 04FEB2019
# Last Modified: 04FEB2019

import sys
import argparse
from argparse import RawDescriptionHelpFormatter

parser = argparse.ArgumentParser(
    epilog='''This script takes the following input:
    1) Output from GATKs ASEReadCounter
    2) TSV file containing Contig, Start, Stop, Gene

And will output a TSV file containing SNPs identified by 
ASEReadCounter with Annotation information formatted as:                                                                                                                                                                
    Contig    position    refCount    altCount    geneID
 ''', formatter_class= RawDescriptionHelpFormatter)
parser._action_groups.pop()
required = parser.add_argument_group('Required Arguments')    
required.add_argument('-i', '--infile', help='Input File Name (Output from GATKs ASEReadCounter)', required=True)    
required.add_argument('-a', '--AnnotationFile', help='Annotation File Name (Anotation file from annotation_file.py)', required=True)
optional = parser.add_argument_group('Optional Arugments')    
optional.add_argument('-o', '--output', help='Output file name (Default = for_geneiASE.tsv)', default='for_geneiASE.tsv')

def annotation_dict(Annotation_file):                    # Generating an annotation dictionary from annotation file
    anno = open(Annotation_file, 'r')
    anno_dict = {}
    for line in anno.readlines()[1:]:                    # Skipping header line 
        columns = line.rstrip().split('\t')
        contig = columns[0]
        gStart = int(columns[1])
        gEnd = int(columns[2])
        gName = columns[3]
        if contig not in anno_dict.keys():               # Generating new dictionary entry for contig if not already present,
            anno_dict[contig] = [(gStart, gEnd, gName)]  # otherwise it is appended to the existing list (dictionary value)
        else:
            anno_dict[contig].append((gStart, gEnd, gName))

        for key, value in anno_dict.items():             # Sorting dictionary to ensure loci are in sequential order
            anno_dict[key] = sorted(value)
    anno.close()
    return(anno_dict)

def Add_annotation(infile, AnnotationFile, outName):     # Processing count file and adding annotation
    annotation = annotation_dict(AnnotationFile)
    ASE_f = open(infile, 'r')
    outfile = open(outName, 'w')
    anno_str = 'Gene\tposition\tRefCount\tAltCount\n'

    for line in ASE_f.readlines()[1:]:                   # Skipping the headerline, iterating through remainder of file
        columns = line.split('\t')
        contig = columns[0]
        position = int(columns[1])
        refcount = columns[5]
        altcount = columns[6]
        tup_list = annotation[contig]             

        for gene in tup_list:                            # Iterating over all loci for given contig 
            GeneStart = int(gene[0])
            GeneEnd = int(gene[1])
            if position < GeneStart:                     # This breaks the loop if we move past the location of present SNP
                break
            elif GeneStart <= position and position <= GeneEnd:   # Confirms SNP is within gene
                GeneID = gene[2]
                anno_str += '{}\t{}\t{}\t{}\n'.format(GeneID, position, refcount, altcount)
            else:
                continue

    outfile.write(anno_str)
    ASE_f.close()
    outfile.close()

args = parser.parse_args()
infile = args.infile
AnnotationFile = args.AnnotationFile
output = args.output
print()
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('ReadCount_Annotate.py is running')
print()
print('Program Parameters')
print('INPUT FILE      = {}'.format(args.infile))
print('ANNOTATION FILE = {}'.format(args.AnnotationFile))
print('OUTPUT FILE     = {}'.format(args.output))
print()
print('Extracting counts from Input File and adding annotation.')
Add_annotation(args.infile, args.AnnotationFile, args.output)
print('ReadCount_Annotate.py processing is complete.')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print()
