## Andrew S. Lang
## 19FEB2018

# This script will take the following inputs (in this order)
# 1. GFF file to adjust
# 2. A conversion file from NCBI containing gene & accession IDs
# 3. BLAST results from blasting the transcriptome sequences

# For every "exon" entry in the input gff, mRNA transcript identifiers are converted to RefSeq RNA accession
# numbers, and Entrez gene ID information is stored with gene abbreviation data.  This additional information
# is then written back into the gff file, and a new GFF is saved with a "convertedIDs.gff."

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
        entrezID = column[1]						# Entrez ID from conversion file
        rnaID = column[3]						# RNA accession ID from conversion file
        gene_name = column[15]						# Gene abbrevision ID from conversion file
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
        MAKERmRNAid = column[0]						# Transcript ID from blast file, as seen in 
									# the blasted transcriptome
        rnaID = column[1]						# RNA accession number from blast file

        blast_dict[MAKERmRNAid] = rnaID

    blast_file.close()
    return blast_dict

def gff_add_annotation(old_gff, ID_conversion_file, BLAST_file):
        # gff_add_annotation is the "main function" of this script.  It will call upon the two other functions
        # to generate dictionaries and convert RNA IDs to RNA Accession numbers, Entrez Gene IDs, and gene 
        # abbreviations, ultimately generating a new, updated GFF. 
    outfile_name = str(old_gff).replace("gff", "convertedIDs.gff")
    outfile = open(outfile_name, "w")
    gff_file = open(old_gff, "r")
    gff = ""

    RNA_ENTREZ_dict = convert_RNA_ENTREZ(ID_conversion_file)
    BLAST_dict = blast_convert_ID_RNA(BLAST_file)

    for line in gff_file:
	
        # a boolean to determine if line contains actual features for gtf or details specific to GFF3
        if bool(re.search("#.*|contig|match|match_part", line)):
            gff += line							# Bypassing any lines that do not contain
            continue							# pertinent info

        column = line.rstrip().split("\t")
        attribute = str(column[2])					# attribute type from gff

        if attribute == "exon" :
            first_cols = "\t".join(column[0:8])
            mRNAid_match = re.search("ID=(.*?-mRNA-.*):", column[8])	# searching for mRNA ID in gff
            if mRNAid_match:
                mRNAid = mRNAid_match.group(1)
                if mRNAid in BLAST_dict.keys():
                    rna_accession = BLAST_dict[mRNAid]			# Converting mRNA ID to RNA accession
                    RNA_ENTREZ = RNA_ENTREZ_dict[rna_accession].split(" ")	
                    entrezID = RNA_ENTREZ[0]				# Splitting values (entrezID & gene abb.)
                    gene = RNA_ENTREZ[1]				# from the conversion dictionary
                else:
                    rna_accession = "absent_transcriptID"
                    entrezID = "absent_entrezID"
                    gene = "absent_geneID"
                feature_line = "gene_id=" + entrezID + ";transcript_id=" + rna_accession + ";geneName=" + gene + ";" + column[8] + "\n"
            else:
                feature_line = column[8] + "\n"
            gff += first_cols + "\t" + feature_line

        else:
            gff += line
            continue

    outfile.write(gff)
    outfile.close()
    gff_file.close()

if __name__ == '__main__':
    gff_file = sys.argv[1]
    ID_conversion = sys.argv[2]
    BLAST = sys.argv[3]
    
    gff_add_annotation(gff_file, ID_conversion, BLAST)
