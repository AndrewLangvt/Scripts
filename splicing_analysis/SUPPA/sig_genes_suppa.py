# sig_genes_suppa.py
# Andrew S. Lang
# Created: 24MAR2018
# Last Modified: 26MAR2018

# This script will take an input SAMPLE.dpsi file from SUPPA, and spit out all of the genes in which significant 
# splicing events (p_val < 0.05) occur

import re
import sys


def sig_ev(fname):
    name_trimmed = re.sub(r'.*/', '', str(fname)).replace("_diffsplice.dpsi","")
    outfile_name = "spliced_genes-SUPPA-" + name_trimmed + ".tsv"
    outfile = open(outfile_name, "w")
    file = open(fname, "r")
    
    spliced_genes = ""
    spliced_genes_list = []
    next(file)
    
    for line in file:
        column = line.rstrip().split("\t")
        geneID = re.sub(r'_locus[0-9]', '', re.sub(r';.*', '', str(column[0])))           # removing locus numbers and everything following gene ID                                
        pval = float(column[2])
        psi = abs(float(column[1]))
      
        if pval <= float(0.05) :
#        if pval <= float(0.05) and psi >= 0.1 :
            if "_and_" in geneID:
                mult_IDs = geneID.rstrip().split("_and_")                                 # some of the output from SUPPA contains gene1_and_gene2, splitting them                 
                for singleID in mult_IDs:
                    if geneID not in spliced_genes_list:
                        spliced_genes_list.append(singleID)
                    elif geneID not in spliced_genes_list:
                        spliced_genes_list.append(geneID)
            else:
                if geneID not in spliced_genes_list:
                    spliced_genes_list.append(geneID)
        else:
            continue

        for gene in spliced_genes_list:
        spliced_genes += gene + "\n"

    outfile.write("Analysis:SUPPA " + name_trimmed + "\n" + spliced_genes)
    outfile.close()
            
            
if __name__ == '__main__':
    filename = sys.argv[1]
    sig_ev(filename)
