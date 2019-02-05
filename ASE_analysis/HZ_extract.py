#! /usr/bin/env python3 

# HZ_extract.py
# Andrew S. Lang
# Created: 05FEB2019
# Last Modified: 05FEB2019

import sys
import argparse
from argparse import RawDescriptionHelpFormatter
    
parser = argparse.ArgumentParser(
    description='''This script takes a VCF input and will output a VCF 
that is filtered to contain only heterozygous loci.''', formatter_class= RawDescriptionHelpFormatter)
parser._action_groups.pop()
required = parser.add_argument_group('Required Arguments')    
required.add_argument('-i', '--infile', help='Input File Name (VCF File)', required=True)    
optional = parser.add_argument_group('Optional Arugments')    
optional.add_argument('-o', '--output', help='Output file name (Default = Het_only.vcf)', default='Het_only.vcf')

def hzExtract(inputfile, outName):                     # Extracting HZ sites from VCF
    vcf = open(inputfile, 'r')
    vcf_str = ""

    for line in vcf:
        if line.startswith("#"):                       # Retaining all of the VCF informational lines
            vcf_str += line
        else:
            columns = line.rstrip().split('\t')
            geno_info = columns[9]
            genotype = geno_info.split(':')            # Isolating the allele genotypes
            alleles = genotype[0].split('/')
            allele1 = str(alleles[0])
            allele2 = str(alleles[1])
            if allele1 != "." and allele1 != allele2:  # Only retaining HZ genotypes
                vcf_str += line
            else:
                continue
    outfile = open(outName, 'w')
    outfile.write(vcf_str)
    vcf.close()
    outfile.close()

args = parser.parse_args()
inputfile = args.infile
output = args.output

print()
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('HZ_extract.py is running.')
print()
print('Program Parameters')
print('INPUT FILE      = {}'.format(args.infile))
print('OUTPUT FILE     = {}'.format(args.output))
print()
print('Extracting HZ sites from VCF')
hzExtract(args.infile, args.output)
print()
print('HZ_extract.py processing is complete.')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print()
