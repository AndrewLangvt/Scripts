# annotation_file.py
# Andrew S Lang
# 06JAN2019

# This script takes an input GFF, gene to accesszion gzipped file (see below), and a BLAST results file from 
# blasting the Columba Livia transcriptome to the Gallus genome. 
# It will then generate a tab-separated file with four columns
# chromosome    gene.start    gene.end    gene.name

import sys
import io
import gzip
import re

def convert_RNA_ENTREZ(file1):
    # convert_RNA_ENTREZ takes an input gene to accession file found here
    # ftp://ftp.ncbi.nlm.nih.gov/gene/DATA/gene2accession.gz
    # It will then generate a dictionary where the RNA accession number is
    # the key, while the ENTREZ ID and gene abbreviation are the values

    convert_file = io.TextIOWrapper(io.BufferedReader(gzip.open(file1)))
    convert_dict = {}
    for line in convert_file:
        column = line.rstrip().split("\t")
        entrezID = column[1]					 # Entrez ID from conversion file
        rnaID = column[3]		    	    		 # RNA accession ID from conversion file
        gene_name = column[15]				  	 # Gene abbrevision ID from conversion file
        dict_val = str(entrezID + " " + gene_name)
        convert_dict[rnaID]=dict_val
    convert_file.close()    
    return convert_dict

def blast_convert_ID_RNA(file2):
    # blast_convert_ID_RNA is a function that takes a blast file as input
    # and parses through the blast hits, assigning the mRNA transcript IDs
    # as the keys, and corresponding RNA accession numbers as values
    
    blast_file = open(file2, "r")
    blast_dict = {}

    for line in blast_file:
        column = line.rstrip().split("\t")
        MAKERgeneID = column[0].rsplit("-mRNA")[0]		# Transcript ID from blast file, except with the
		      						# "-mRNA" extension removed

        rnaID = column[1]					# RNA accession number from blast file

        if MAKERgeneID not in blast_dict.keys():
            blast_dict[MAKERgeneID] = rnaID
        else:
            continue
	
    blast_file.close()
    return blast_dict

def gff_add_annotation(old_gff, ID_conversion_file, BLAST_file):
        # gff_add_annotation is the "main function" of this script.  It will call upon the two other functions
        # to generate dictionaries and convert RNA IDs to RNA Accession numbers, Entrez Gene IDs, and gene 
        # abbreviations, ultimately generating a new, updated GFF. 

    outfile_name = str(old_gff).replace("gff", "RPASE.tsv")
    outfile = open(outfile_name, "w")
    gff_file = open(old_gff, "r")
    gene_file = "chromosome\tgene.start\tgene.end\tgene.name\n"

    print("Building RNA to Entrez conversion dictionary")
    RNA_ENTREZ_dict = convert_RNA_ENTREZ(ID_conversion_file)
    print("RNA to Entrez dictionary complete")
    print("- - - - - - - - - - - - - - - - -")
    print("Building BLAST dictionary")
    BLAST_dict = blast_convert_ID_RNA(BLAST_file)
    print("BLAST dictionary complete")
    print("Beginning to process your GFF")
    for line in gff_file:
    
        # a boolean to determine if line contains actual features for RPASE TSV (only pulling out gene entries)
        if bool(re.search("#.*|contig|match|match_part", line)):
            continue	 		  	    	      	              # Bypassing any lines that do not contain pertinent info

        column = line.rstrip().split("\t")
        attribute = str(column[2])					      # attribute type from gff

        if attribute == "gene" :
            chrom = str(column[0])					      # chromosome ID
            start = str(column[3])					      # gene start location
            stop = str(column[4])				       	      # gene stop location

            gene_match = re.search("ID=(.*?);", column[8])
            if gene_match:
                geneID = gene_match.group(1)
                if geneID in BLAST_dict.keys():
                    rna_accession = BLAST_dict[geneID]                        # Assigning transcript ID to look up entrez ID in 
                    entrezID = RNA_ENTREZ_dict[rna_accession].split(" ")[0]   #      RNA_ENTREZ_dict dictionary
                    gene = RNA_ENTREZ_dict[rna_accession].split(" ")[1]       # Saving the gene abbreviation (e.g. GnRH) in case
                else:                                                         #      I want it for future reference
                    rna_accession = "absent_transcriptID"
                    entrezID = "absent_entrezID"
                    gene = "absent_geneID"
		
                feature_line = ("{}\t{}\t{}\t{}\n").format(chrom, start, stop, entrezID)

            else:
                feature_line = "UNFOUND ID FOR " + line
            gene_file += feature_line
        else:
            continue


    print("GFF processing complete! :-)")
    outfile.write(gene_file)
    outfile.close()
    gff_file.close()

if __name__ == '__main__':
    gff_file = sys.argv[1]
    ID_conversion = sys.argv[2]
    BLAST = sys.argv[3]
    
    gff_add_annotation(gff_file, ID_conversion, BLAST)
