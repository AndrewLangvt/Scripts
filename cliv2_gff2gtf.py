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
           gbank = re.search("ID=(.*?)-mRNA-", column[8])
           trans = re.search("ID=(.*?):", column[8])
           if gbank:
               gen_id = gbank.group(1)
               trans_id = trans.group(1)
           else:          
               continue                  

        # Formatting gene_id and transcript_id

           last_col = 'gene_id ' + '"' + gen_id + '"' + "; " + 'transcript_id ' + '"' + trans_id + '"' + ';'
          
           attribute = column[0] + "\t" + column[1] + "\t" + column[2] + "\t" + column[3] + "\t" + column[4] + "\t" + column[5] + "\t" + column[6] + "\t" + column[7] + "\t" + last_col + "\n"
          
           gtf += attribute

        else:
            continue   

    outfile.write(gtf)
        
if __name__ == '__main__':
    file = sys.argv[1]
    read_gff(file)
