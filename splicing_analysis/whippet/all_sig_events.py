# all_sig_events.py                                                                                                                                                                
# Andrew S. Lang                                                                                                                                                                   
# Created: 04APR2018                                                                                                                                                               
# Last Modified: 04APR018                                                                                                                                                          
# This script will take an input diff.gz file from whippet, and spit out all of the genes in which significant                                                                     
# splicing events (prob > 0.95) occur                                                                                                                                              

import re
import sys
import gzip


def sig_ev(fname):
    name_trimmed = re.sub(r'.*/', '', str(fname)).replace("_comparison.diff.gz","")
    outfile_name = "all_spliced_genes-" + name_trimmed + ".tsv"
    outfile = open(outfile_name, "w")
    with gzip.open(fname, 'rt') as file2 :
        header = file2.readline()
        file = file2.readlines()[1:]
        spliced_genes = ""

        for line in file:
            column = line.rstrip().split("\t")

            geneID = str(column[0])
            prob = float(column[8])
            psi = float(column[7])
            event = str(column[2])

            if prob >= float(0.95) :
                spliced_genes+= name_trimmed + '\t' + line
            else:
                continue

    outfile.write('Diff_File\t' + header + spliced_genes)
    outfile.close()

if __name__ == '__main__':
    filename = sys.argv[1]
    sig_ev(filename)
