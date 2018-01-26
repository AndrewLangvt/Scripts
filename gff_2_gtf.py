""" This python script will take a GFF as 1st cmd line arg and spit out a GTF with the same name as input GFF. """
import sys
import re

def read_gff(filename):
    outfile_name = str(filename).replace("gff", "gtf")
    outfile = open(outfile_name, "w")
    file = open(filename, "r")
    gtf = ""

    for line in file:
        column = line.rstrip().split("\t")

	#two booleans to determine if line contains actual features for gtf
	#or details specific to GFF3

        if bool(re.search("#.*", line)):
            continue
        elif bool(re.search("region", column[2])):
            continue
 
        #only extract lines where the attribute is an exon
        #search for "Genbank" and "transcript_id" in attributes, bordered 
	#with a ";". If found, assign as "gen_id" "trans_id", respectively.

        attribute = str(column[2])
        if attribute == "exon" : 
           gbank = re.search(".*GeneID:(.*?),", column[8])
           if gbank:
               gen_id = gbank.group(1)
           else:
               gbank2 = re.search(".*GeneID:(.*)", column[8])
               if gbank2:
                   gen_id = gbank2.group(1)
               else:
                   continue
#                   gen_id = ""

           trans = re.search(".*transcript_id=(.*?);", column[8])
           if trans:
               trans_id = trans.group(1)
           else:
               trans2 = re.search(".*transcript_id=(.*)", column[8])
               if trans2: 
                   trans_id = trans2.group(1)
               else:
                   continue   
#              	   trans_id = ""
            

	#formatting gene_id and transcript_id

           last_col = 'gene_id ' + '"' + gen_id + '"' + "; " + 'transcript_id ' + '"' + trans_id + '"' + ';'
          
           attribute = column[0] + "\t" + column[1] + "\t" + column[2] + "\t" + column[3] + "\t" + column[4] + "\t" + column[5] + "\t" + column[6] + "\t" + column[7] + "\t" + last_col + "\n"
          
           gtf += attribute

        else:
            continue   

    outfile.write(gtf)
	
if __name__ == '__main__':
    file = sys.argv[1]
    read_gff(file)
