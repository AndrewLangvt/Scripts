# high_psi.py
# Andrew S. Lang
# Created: 26SEP2017
# Last Modified: 01NOV2017

# This script will take an input diff.gz file from whippet, and spit out all of the significant events (prob > 0.95)
# with a psi value >= the value given as the second command line argument. 

import re
import sys
import gzip

def sig_ev(fname, psi):
    with gzip.open(fname, 'rt') as file2 :
        file = file2.readlines()[1:]
        hENTevent = ""
        psi_min = float(psi)

        for line in file:
            column = line.rstrip().split("\t")

            prob = float(column[8])
            delpsi = float(column[7])
            entropy = float(column[10])
            gene = str(column[0])
            loc = str(column[2])
            event = str(column[4])
            psia = str(column[5])
            psib = str(column[6])

            if prob >= float(0.95) :
                if abs(delpsi) >= psi_min :
                    hENTevent += gene + '\t' + loc + '\t\t' + str(entropy) + '\t' + ' ' + event + '\t' + ' ' + str(delpsi) + '  \t' + str(prob) + '\t' + " A: " + psia + '\t' + "  B: " +  psib + '\n'
#                    if float(2.0) < entropy :
#                        hENTevent += gene + '\t' + loc + '\t \t' + str(entropy) + '\t' + event + '\t' + str(psi) + '\n'
#                    else:
#                        continue
                else:
                    continue
            else:
                continue

        name_trimmed = re.sub(r'.*/', '', str(fname))
        print("")
        print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
        print("")
        print(name_trimmed)
        print("Gene \t\t Location \t\t\t Entropy \t Event \t d-PSI \t\t Prob \t\t PSI-A \t\t PSI-B")
        print("======================================================================")
        print(hENTevent)
        print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
        print("")

if __name__ == '__main__':
    filename = sys.argv[1]
    psi = sys.argv[2]
    sig_ev(filename, psi)
