# matrix_psi.py
# Andrew S. Lang
# Created 02NOV2017
# Last modified 02NOV2017

# This script will take an input list of event IDs, psi.gz file, and ID-name, and will output a column containing the ID, sex, tissue, treatment, 
# and psi values (normalized by total genes identified in the sample file). These columns then will be used to generate a matrix of psi events.  

import sys
import gzip

def count_genes(sample_file):
    with gzip.open(sample_file, 'rt') as sampleIDs:

        tot_events = []                                                                         # defining tot_events as list
        for line in sampleIDs.readlines()[1:]:                                                  # looping through the file containing all event IDs
            column = line.rstrip().split('\t')                                                  # splitting each line on the tab, assigning as tuple
            tot_events.append(column[0])                                                        # appending the event name to tot_events
        gene_count = len(set(tot_events))                                                       # counting the length of tot_events list
    return gene_count


def gen_matrix(matrix_list, sample_file, name, gene_count):
    with open(matrix_list, 'r') as matrixIDs, gzip.open(sample_file, 'rt') as sampleIDs:

        out_line = ""
        sample_dict = {}
        
        identifiers = str(sample_file).replace('.psi.gz', '').split('_')                        # Splitting the name of the sample file to generate sex, tissue, and
        sex = identifiers[1]                                                                    # treatment identifiers.
        tissue = identifiers[2]
        treatment = identifiers[3]

        out_line += str(name) + '\n' + sex + '\n' + tissue + '\n' + treatment + '\n'            # writting the first 4 lines of the column (Name, sex, tissue, treatment)
        for line in sampleIDs.readlines()[1:]:                                                  # looping through the file containing sample information
            column = line.rstrip().split('\t')                                                  # splitting each line on the tab, assigning as tuple

            if column[5] == 'NA':                                                               # checking if psi value is 'NA', assigning psi_val as 0 if true
                psi_val = 0.0                                                                   
            else:                                                                               # otherwise (psi != 'NA'), assigning psi_val as value refleted in file 
                psi_val = str(column[5])

            if column[6] == 'NA':                                                               # Checking the CI width, if 'NA', assigns the psi val corresponding to 
                sample_dict[column[2]] = 0.0                                                    # this event as 0.  If the CI width is an actual number, this checks 
            elif float(column[6]) <= 0.3:                                                       # to determine that it is narrower, or equal to, 0.3.  If this is true
                sample_dict[column[2]] = float(psi_val)/float(gene_count)                       # it will assign this (normalized by gene count for this sample) as the 
            elif float(column[6]) > 0.3:                                                        # value for the key (event) in the sample dictionary (sample_dict).
                sample_dict[column[2]] = 0.0
            
        for line in matrixIDs:
            id = line.rstrip()                                                                  # Iterates over the keys in my sample event dictionary, if said event
            if id in sample_dict.keys():                                                        # is found, appends the psi value to the output string.  If not present
                out_line += str(sample_dict[id]) + '\n'                                         # in the dictionary, it will assign '0.0' to the string.  This allows 
            else:                                                                               # me to check for all possible events, regardless if they were 
                out_line += '0.0\n'                                                             # identified in any given file. 
        final_line = out_line.rstrip()  
        print(final_line)

if __name__ == '__main__':
    matrix_file = sys.argv[1]
    sample_file = sys.argv[2]
    name = str(sys.argv[3])
    gene_count = count_genes(sample_file)

gen_matrix(matrix_file, sample_file, name, gene_count)
