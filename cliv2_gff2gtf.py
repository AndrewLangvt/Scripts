import sys
import re

def read_gff(filename):
    outfile_name = str(filename).replace("gff", "gtf")
    outfile = open(outfile_name, "w")
    file = open(filename, "r")
    gtf = ""

    for line in file:
        column = line.rstrip().split("\t")

        # a boolean to determine if line contains actual features for gtf
        # or details specific to GFF3

        if bool(re.search("#.*|contig|match|match_part", line)):
            continue
            
        # only extract lines where the attribute is an exon
        # search for "Genbank" and "transcript_id" in attributes, bordered 
        # with a ";". If found, assign as "gen_id" "trans_id", respectively.

        attribute = str(column[2])
        if attribute == "exon" : 
            gbank = re.search("gene_id=(.*?);", column[8])
            trans = re.search("transcript_id=(.*?);", column[8])
            gene = re.search("geneName=(.*?);", column[8])
            old_id = re.search("ID=(.*?);", column[8])
           
            if gbank:
                gen_id = gbank.group(1)
                trans_id = trans.group(1)
                gname = gene.group(1)
                locusID = old_id.group(1)
            else:          
                continue                  

            # Formatting gene_id and transcript_id

            first_cols = "\t".join(column[0:8])
            last_col = 'gene_id "' + gen_id + '"; ' + 'transcript_id "' + trans_id + '"; gene_abbrev=' + gname + '; gnomeID=' + locusID 
          
            gtf += first_cols + "\t" + last_col + '\n'

        else:
            continue   

    outfile.write(gtf)
        
if __name__ == '__main__':
    file = sys.argv[1]
    read_gff(file)
