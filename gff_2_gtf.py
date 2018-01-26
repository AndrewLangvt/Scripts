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
 
        feature_line = ""
        attribute = str(column[2])



        if attribute == "region" :
           reg = re.search("ID=(.*?);", column[8])
           if reg:
               feature_line += 'ID "' + str(reg.group(1)) + '"; '

           nam = re.search(".*Name=(.*?);", column[8])
       	   if nam:
               feature_line += 'Name "' + str(nam.group(1)) + '"; '

           chrom = re.search(".*chromosome=(.*?);", column[8])
       	   if chrom:
               feature_line += 'Chromosome "' +	str(chrom.group(1)) + '"; '



        elif attribute == "mRNA" :
           mrna = re.search("ID=(.*?);", column[8])
           if mrna:
               feature_line += 'ID "' + str(mrna.group(1)) + '"; '

           gbank = re.search(".*GeneID:(.*?),", column[8])
           if gbank:
               feature_line += 'gene_id "' + str(gbank.group(1)) + '"; '

           nam = re.search(".*gene=(.*?);", column[8])
           if nam:
               feature_line += 'gene_name "' + str(nam.group(1)) + '"; '

           trans = re.search(".*transcript_id=(.*?);", column[8])
           if trans:
               feature_line += 'transcript_id "' + str(trans.group(1)) + '"; '
           else:
               trans2 = re.search(".*transcript_id=(.*)", column[8])
               if trans2:
                   feature_line += 'transcript_id "' + str(trans2.group(1)) + '"; '
               else:
                   continue



        elif attribute == "exon" :
           gbank = re.search(".*GeneID:(.*?),", column[8])
           if gbank:
               feature_line += 'gene_id "' + str(gbank.group(1)) + '"; '
           else:
               gbank2 = re.search(".*GeneID:(.*)", column[8])
               if gbank2:
                   feature_line += 'gene_id "' + str(gbank2.group(1)) + '"; '
               else:
                   continue

           trans = re.search(".*transcript_id=(.*?);", column[8])
           if trans:
               feature_line += 'transcript_id "' + str(trans.group(1)) + '"; '
           else:
               trans2 = re.search(".*transcript_id=(.*)", column[8])
               if trans2: 
                   feature_line += 'transcript_id "' + str(trans2.group(1)) + '"; '
               else:
                   continue   



        elif attribute == "CDS" :
           seq = re.search("ID=(.*?);", column[8])
           if seq:
               feature_line += 'ID "' + str(seq.group(1)) + '"; '
           
           parent = re.search(".*Parent=(.*?);", column[8])
           if parent:
               feature_line += 'ID "' + str(parent.group(1)) + '"; '

           gbank = re.search(".*GeneID:(.*?),", column[8])
           if gbank:
               feature_line += 'gene_id "' + str(gbank.group(1)) + '"; '

           prot = re.search(".*protein_id=(.*?);", column[8])
           if prot:
               feature_line += 'protein_id "' + str(prot.group(1)) + '"; '
           else:
               prot2 = re.search(".*protein_id=(.*)", column[8])
               if prot2:
                   feature_line += 'protein_id "' + str(prot2.group(1)) + '"; '
               else:
                   continue

        else:
            continue
            

	#formatting gene_id and transcript_id

        attribute = column[0] + "\t" + column[1] + "\t" + column[2] + "\t" + column[3] + "\t" + column[4] + "\t" + column[5] + "\t" + column[6] + "\t" + column[7] + "\t" + feature_line + "\n"
        gtf += attribute


    outfile.write(gtf)
	
if __name__ == '__main__':
    file = sys.argv[1]
    read_gff(file)

