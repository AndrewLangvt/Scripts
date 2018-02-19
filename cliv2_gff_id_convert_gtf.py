## Andrew S. Lang
## 19FEB2018

# This script will take the following inputs (in this order)
# 1. GFF file to adjust
# 2. A conversion file from NCBI containing gene & accession IDs
# 3. BLAST results from blasting the transcriptome sequences

import sys
import re

def convert_RNA_ENTREZ(file1):
    convert_file = open(file1, "r")
    convert_dict = {}
    for line in convert_file:
        column = line.rstrip().split("\t")
        entrezID = column[1]
        rnaID = column[3]
        gene_name = column[16]
        dict_val = str(entrezID + "_" + gene_name)
	
        convert_dict[rnaID]=entrezID
        
    return convert_dict

def blast_convert_ID_RNA(file2):
    blast_file = open(file2, "r")
    blast_dict = {}

    for line in blast_file:
        column = line.rstrip().split("\t")
        MAKERmRNAid = column[0]
        rnaID = column[1]

        blast_dict[MAKERmRNAid] = rnaID

    return blast_dict

def gff_add_annotation(old_gff, ID_conversion_file, BLAST_file):
    outfile_name = str(old_gff).replace("gff", "IDconvert.gff")
    outfile = open(outfile_name, "w")
    gff_file = open(old_gff, "r")
    gff = ""

    RNA_ENTREZ_dict = convert_RNA_ENTREZ(ID_conversion_file)
    BLAST_dict = blast_convert_ID_RNA(BLAST_file)

    for line in gff_file:
	
        # a boolean to determine if line contains actual features for gtf
        # or details specific to GFF3

        if bool(re.search("#.*|contig|match|match_part", line)):
            gff += line
            continue

        column = line.rstrip().split("\t")
        attribute = str(column[2])

        if attribute == "exon" :
            first_cols = "\t".join(column[0:8])
            mRNAid_match = re.search("ID=(.*?-mRNA-.*):", column[8])
            if mRNAid_match:
                mRNAid = mRNAid_match.group(1)
                rna_accession = BLAST_dict[mRNAid]
                entrezID = RNA_ENTREZ_dict[rna_accession]
                feature_line = "gene_id=" + entrezID + ";transcript_id=" + rna_accession + ";" + column[8] + "\n"
            else:
                feature_line = column[8] + "\n"
            gff += first_cols + "\t" + feature_line

        else:
            gff += line
            continue
	
if __name__ == '__main__':
    gff_file = sys.argv[1]
    ID_conversion = sys.argv[2]
    BLAST = sys.argv[3]
    
    gff_add_annotation(gff_file, ID_conversion, BLAST)
