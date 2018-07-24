#! /usr/bin/env python3 

# exon_extract.py
# get_GOs.py
# Andrew S. Lang
# Created: 01JUL2018
# Last Modified: 24JUL2018

# This script takes an output file from Whippet, and identifys parent GO terms corresponding to each alternatively spliced
# gene. The terms are then represented in tabular format with counts of each parent term output. 
# The execution of this script is as follows:
# ./get_GOs.py <filename> columnNumber level
#    columnNumber = column to reference for GO terms
#         10: MF-slim    11: BP-slim   12: CC-slim 
#         13: MF         14: BP        15: CC

import sys
import re
import subprocess 
from operator import itemgetter
from collections import defaultdict

def get_GOs(filename, colnum, level):
    file1 = open(filename, 'r', encoding='iso-8859-1')
    file = file1.readlines()[1:]
    ID_dict = {}
    ID_GO_out = []
    tot_genes = set()

    print('Generating Gene ID Dictionary')
    for line in file:                                       # ***---GENERATE DICTIONARY OF GENE ID AND GO IDS---***
        column = line.rstrip().split("\t")
        geneID = column[6]
        GO_column = column[int(colnum)]                     #       Grab desired column from file
        GO_list = ""
        tot_genes.add(geneID)                               #       For counting all genes, regarless of GO ID presence
        for match in re.findall("(GO:[0-9]*)", GO_column):  #       Search line for GO term
            GO_list += match + ","                          #       Add GO term to string, with comma
            if geneID in ID_dict:
                old_val = ID_dict[geneID] + ","      #       Assign value(GO term string) to key(geneID)
                ID_dict[geneID] = old_val + GO_list[:-1:]
            else:
                ID_dict[geneID] = GO_list[:-1:]                 #       Assign value(GO term string) to key(geneID)
    for key in ID_dict.keys():
        GO_terms = ID_dict[key].rstrip().split(",")         #       Split terms for a given gene ID
        for term in GO_terms:
            ID_GO_out.append([key, term])                   #       Append gene ID with each corresponding term

    print('Generating input for goAbstract.py')
    go_input = ""

    for term in ID_GO_out:                                  # ***---GENERATE INPUT OF JUST GO IDS FOR goAbstract.py---***
        if str(term[1]) != '':                              #       Only include values that contain a string 
            go_input += str(term[1]) + '\n'                 #       and not the portion following a split on ','
        else:
            continue
    go_input2 = go_input.rstrip('\n')
    GO_list = open('GO_list_input.txt', 'w')                #       Write this all to file, as goAbstract.py requires this
    GO_list.write(go_input2)
    GO_list.close()

    print('Running goAbstract.py')                          # ***---RUN GOABSTRACT.PY AND PARSE OUTPUT---***
    abstract = subprocess.run("/pylon5/mc3bg6p/al2025/isoform/whippet_analysis/diff_files/stress_study/GO_analysis/goAbstract_lang.py -i ./GO_list_input.txt -l {}".format(int(level)), shell=True, stdout=subprocess.PIPE)
    ab_temp = abstract.stdout.decode()
    abstracted_GOs = ab_temp.splitlines()[1::]              #       Skip the first element of stdout list 
    Parent_Dict= defaultdict(list)                                         #       ('GO_name \t Domain') from ./goAbstract.py
    Final_out = ""

    for term_parent in abstracted_GOs:                      #       Generate dictionary of GO_ID and parent term
        GOterm = term_parent.split('\t')[0]
        GOparent = term_parent.split('\t')[1]
        Parent_Dict[GOterm].append(GOparent)

    print('Generating list of Gene, GO ID, and parent term.')
    gene_parent = set()                                     #       Create three-column list of GeneID, GOID, and Parent term 
    for Gene in ID_dict.keys():
        if ID_dict[Gene] != '':
            for GO_ID in ID_dict[Gene].split(','):
                if GO_ID in Parent_Dict.keys():
#                    print(Parent_Dict[GO_ID])
                    for Parent in Parent_Dict[GO_ID]:
#                        print(Parent)
#                        Parent = Parent_Dict[GO_ID]
                        Final_out += '{}\t{}\t{}\n'.format(Gene, GO_ID, Parent)
                        gene_parent.add((Gene, Parent))
                else:
                    # Term = "NoGOterm"
                    Parent = "NoParent"
                    Final_out += '{}\t{}\t{}\n'.format(Gene, GO_ID, Parent)
                    gene_parent.add((Gene, Parent))
        else:
            GO_ID = "NoGOterm"
            Parent = "NoParent"
            gene_parent.add((Gene, Parent))
            Final_out += '{}\t{}\t{}\n'.format(Gene, GO_ID, Parent)

    GO_counts = {}
    not_inc = 0

    print('Counting instances of parent terms.')
    for parentIDs in Parent_Dict.values():                   #       Count the number of instances of each parent term
        for single_ID in parentIDs:
            GO_counts[single_ID] = 0
    for GP_pair in gene_parent:
        parent_term = GP_pair[1]
        if parent_term in GO_counts.keys():
            new_value = GO_counts[parent_term] + 1 
            GO_counts[parent_term] = new_value
        else:
#            print("ERROR...Parent term currently absent from your dictionary. \n Ensure your GO_IDs are primary IDs, and not alternat/secondary IDs.")
            not_inc += 1
    total_genes = len(tot_genes)
    print('Normalizing counts and sorting.')
    for term in GO_counts.keys():
        norm_val = GO_counts[term]/total_genes              #       Normalize the counts by total 
        GO_counts[term] = norm_val
                                                            #       Sort terms in one of two orders             
#    GO_counts_sorted = sorted(GO_counts.items(), key=itemgetter(1), reverse=True)#        1) ~~~~ sort by count, descending values 
    GO_counts_sorted = sorted(GO_counts.items(), key=itemgetter(0))  #                    2) ~~~~ sort by parent term, alphabetical order            
    counts_out = ""                                         
    for value in GO_counts_sorted:
        counts_out += "{}\t{}\n".format(value[0], value[1])

    if str(colnum) == "10":                                 #       Depending on column originally input, reflect in output
        goType = "MF-slim"
    if str(colnum) == "11":
        goType = "BP-slim"
    if str(colnum) == "12":
        goType = "CC-slim"
    if str(colnum) == "13":
        goType = "MF"
    if str(colnum) == "14":
        goType = "BP"
    if str(colnum) == "15":
        goType = "CC"

    extension = "GO_counts_{}_lvl{}.tsv".format(goType, level)
    count_fname = str(filename).replace("sheet.txt", extension)
    count_file = open(count_fname, "w")
    count_file.write(counts_out)
    count_file.close()

if __name__ == '__main__':
    file = sys.argv[1]
    colnum = sys.argv[2]
    level = sys.argv[3]
    get_GOs(file, colnum, level)
