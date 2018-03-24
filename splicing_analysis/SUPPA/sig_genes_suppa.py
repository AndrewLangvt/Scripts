# sig_genes_suppa.py
# Andrew S. Lang
# Created: 24MAR2018
# Last Modified: 24MAR2018

# This script will take an input SAMPLE.dpsi file from SUPPA, and spit out all of the genes in which significant 
# splicing events (p_val < 0.05) occur

import re
import sys


def sig_ev(fname):
    name_trimmed = re.sub(r'.*/', '', str(fname)).replace("_diffsplice.dpsi","")
    outfile_name = "spliced_genes-SUPPA-" + name_trimmed + ".tsv"
    outfile = open(outfile_name, "w")
    file = open(fname)
    
    spliced_genes = ""
    
    for line in file:
        column = line.rstrip().split("\t")
        geneID = str(column[0])
        ppval = float(column[2])
        psi = abs(float(column[2]))
      
        if pval <= float(0.05) :
            if psi >= float(0.1) :
                if geneID not in spliced_genes_list:
                    spliced_genes_list.append(geneID)
            else:
                continue
        else:
            continue


        for gene in spliced_genes_list:
            spliced_genes += gene + "\n"

        outfile.write(name_trimmed + "\n" + spliced_genes)
        outfile.close()

if __name__ == '__main__':
    filename = sys.argv[1]
    sig_ev(filename)
