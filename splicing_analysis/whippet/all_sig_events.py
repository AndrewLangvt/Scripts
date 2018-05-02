# all_sig_events.py                                                                                                                                                                                                                                                           
# Andrew S. Lang                                                                                                                                                                                                                                                              
# Created: 02MAY2018                                                                                                                                                                                                                                                          
# Last Modified: 02MAY018                                                                                                                                                                                                                                                     
# This script will take an input diff.gz file from whippet, and spit out all of the genes in which significant                                                                                                                                                                
# splicing events (prob > 0.95 and abs(PSI) > 0.1) occur                                                                                                                                                                                                                      

import re
import sys
import gzip


def sig_ev(fname):
    name_trimmed = re.sub(r'.*/', '', str(fname)).replace("_comparison.diff.gz","")
    outfile_name = "all_sig_spliced_genes-" + name_trimmed + ".tsv"
    outfile = open(outfile_name, "w")
    with gzip.open(fname, 'rt') as file2 :
        header = file2.readline()
        file = file2.readlines()[1:]
        spliced_genes = name_trimmed

        for line in file:
            column = line.rstrip().split("\t")

            prob = float(column[8])
            abs_psi = abs(float(column[7]))

            if prob >= float(0.95) :
                if abs_psi >= 0.1:
                    spliced_genes+= '\t' + line
                else:
                    continue
            else:
                continue

    outfile.write(spliced_genes)
    outfile.close()

if __name__ == '__main__':
    filename = sys.argv[1]
    sig_ev(filename)
