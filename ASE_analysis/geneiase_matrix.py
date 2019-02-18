#! /usr/bin/env python3 

# geneiase_matrix.py
# Andrew S. Lang
# Created: 14FEB2019
# Last Modified: 17FEB2019

import sys
import re
import argparse
from argparse import RawDescriptionHelpFormatter
import os
import csv

parser = argparse.ArgumentParser(
    epilog='''Provide this script with the location containing your TSV files output by GeneiASE, 
and it will generate a TSV matrix. Rownames will be sampleIDs, column names geneIDs, 
and each cell the Benjamini-Hochberg corrected p-value.''', formatter_class= RawDescriptionHelpFormatter)

parser._action_groups.pop()
required = parser.add_argument_group('Required Arguments')    
required.add_argument('-l', '--location', help='Directory containing GeneiASE TSV files', required=True)
optional = parser.add_argument_group('Optional Arugments')    
optional.add_argument('-o', '--output', help='Output file name (Default = GeneiASE_matrix.tsv)', default='GeneiASE_matrix.tsv')


def gen_matrix(dir_location, outfile_name):
    master_dict= {}
    genes = []
    print('- - - - Processing Files - - - -')
    print('')
    for entry in os.scandir(dir_location):
        if entry.is_file() and entry.name.endswith('.tsv'):
            print('Now processing {}'.format(entry.name))
            filename = str(entry.name)
            sample = re.sub('.geneiASE_processed.tsv', '', filename)
            master_dict[sample] = []
            file_open = open(entry, 'r')
            file = file_open.readlines()[1:]
            for line in file:                                     # Adding the entrezID and FDR as tuple to master_dict
                column = line.rstrip().split('\t')
                geneID = column[0]
                fdr = column[8]
                if geneID == 'absent_entrezID':                   # Some of the geneiASE output files have absent_entrezID. Not
                    continue                                      # including them in the matrix file
                master_dict[sample].append((geneID, fdr))
                genes.append(geneID)
                master_dict[sample] = sorted(master_dict[sample]) # Sorting master_dict to ensure entrezIDs are in order
            file_open.close()
    total_genes = sorted(list(set(genes)))                        # Making genes a set, and then a list to get a complete 
                                                                  # list of all genes present in all files of the directory
    pval_dict = {}

    print('')
    print('- - - - Now writing output - - - -')
    for sample in master_dict.keys():                             # Iterating over every sample previously found in the directory
        pval_dict[sample] = []                                    # pval_dict will contain a list of pvalues for each sample
        GenePval_list = master_dict[sample]
        genes_in_sample = {}
        print('Writing output for ' + sample)
        for gene_pval in GenePval_list:                           # Generating a dictionary with key entries of all genes found
            sample_gene = int(gene_pval[0])                       # in the file currently being processed
            genes_in_sample[sample_gene] = []
        for entrezID in total_genes:                              # Iterating over my master list of genes found in all files
            entrez = int(entrezID)
            for gene_fdr in GenePval_list:                        # Separating each tuple into EntrezID and P-value
                samp_geneID = int(gene_fdr[0])
                unfil_fdr = float(gene_fdr[1])
                if entrez not in genes_in_sample.keys():          # For those genes not in this current sample, Pvalue will be 1
                    fdr = 1
                    break
                elif samp_geneID < entrez:                        # Series of booleans to locate the geneID that matches the current
                    continue                                      # EntrezID and assign the Pvalue as the corresponding pvalue for that 
                                                                  # gene in my sample
                elif samp_geneID == entrez:
                    fdr = unfil_fdr
                    break
#                    if unfil_fdr < 0.05:                          # This allows me to generate a "binary" matrix to potentially 
#                        fdr = 0                                   # generate a heatmap of genes showing ASE
#                    else:
#                        fdr = 1
                elif samp_geneID > entrez :
                    break
                else:
                    fdr = 'ERROR'
                    print('Error in parsing for Pvalues. Search output matrix for "ERROR".') 
					
            pval_dict[sample].append(str(fdr))
	
    with open(outfile_name, 'w') as outfile:                      # Writing to file, named according to -o flag
        tsv_writer = csv.writer(outfile, delimiter='\t', lineterminator = '\n')
        first_col = ['SampleID']
        header = first_col + total_genes
        tsv_writer.writerow(header)
        for sample in pval_dict.keys():
            pvals = pval_dict[sample]
            samp_name = [sample]
            entry = samp_name + pvals
            tsv_writer.writerow(entry)
        outfile.close()		
	
args = parser.parse_args()

print()
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('geneiase_matrix.py is running')
print()
print('Program Parameters')
print('LOCATION OF FILES   = {}'.format(args.location))
print('OUTPUT FILE NAME    = {}'.format(args.output))
print()
print('Processing Files and writing to matrix file.')
gen_matrix(args.location, args.output)
print('geneiase_matrix.py processing is complete.')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print()		
