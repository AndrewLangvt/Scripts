# exon_extract.py
# Andrew S. Lang
# Created: 16JUL2018
# Last Modified: 16JUL2018

### This script takes the following input:
#        1) Genome fasta file
#        2) GFF 
#        3) File containing loci of exons to extract where ID is listed as ChromID:start-stop
#        4) Prefix for naming the output files

# Outputs from this script include 1) a fasta-style output of translated exonic sequences and 
# 2) a table with counts of Exons, CDS, 5UTR, and 3UTRs.
 
import re
import sys
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna
#from recordtype import recordtype

class G_info:
    def __init__(self):
        self.sampleType = "none"
        self.chromStart = "none"
        self.is_exon = 0
        self.is_cds = 0
        self.is_5UTR = 0
        self.is_3UTR = 0
        self.strand = "none"
        self.phase = "none"
        self.seq = "none"
        self.inframe_seq = "none"
        self.trans = "none"

def genome_dict(genomeFile):                                 # Generates a ditionary with ChromID as key, and nuc seq as the value
    Genome = SeqIO.parse(genomeFile, "fasta")                # using SeqIO to parse the fastafile
    genDict = {}
    for record in Genome:                              
        chrom = record.id.split(" ")[0]
        seq = record.seq
        genDict[chrom] = seq
    return genDict

def excise_exons(genomeFile, exonF):                         # Excises the exonic sequences from genome, based upon input exon loci file
    gen_dict = genome_dict(genomeFile)
    exon_dict = {}
    exons = open(exonF, "r")
    for line in exons:
        sample = line.split('\t')[0]
        exon = line.split('\t')[3]
        chrom = exon.split(":")[0]
        loc = exon.split(":")[1]
        start = int(loc.split("-")[0])
        stop = int(loc.split("-")[1])
        exon_seq = str(gen_dict[chrom][start-1:stop:])       # Due to pythonic indexing, subtracting 1 from start index to capture that base
        exonID = str.join(':',(chrom, str(start)))
        exon_dict[exonID] = (exon_seq, sample)
#        print('{}\t{}\t{}\t{}\t{}'.format(exonID, start, stop, exon_seq, sample))
#    for key,value in exon_dict.items():
#        print('{}\t{}\t{}'.format(key, value[0], value[1]))
    return exon_dict

def gff_read(genomeGFF):                                     # Reads a GFF and generates a dictionary where ChromID:start is the key and 
    file = open(genomeGFF, "r")                              # an instance of the G_info class is the value
    gff_dict = {}
    for line in file:
        column = line.rstrip().split("\t")

        if bool(re.search("#.*|contig|match|match_part", line)):  # Skipping all lines not pertinent to this analysis
            continue
        chrom = str(column[0])
        attribute = str(column[2])
        start = str(column[3])
        strand = str(column[6])
        phase = str(column[7])
        keyrecord = str.join(':',(chrom, str(start)))

        if keyrecord not in gff_dict.keys():
            gff_dict[keyrecord]= G_info()
            gff_dict[keyrecord].chromStart = keyrecord

        if attribute == "exon" :                             # This block is counting number of exon, CDS, 5UTR, and 3UTR in the spliced exons
            gff_dict[keyrecord].is_exon += 1
        elif attribute == "CDS" : 
            gff_dict[keyrecord].is_cds += 1
            gff_dict[keyrecord].strand = strand
            gff_dict[keyrecord].phase = phase
        elif attribute == "five_prime_UTR" :
            gff_dict[keyrecord].is_5UTR += 1
        elif attribute == "three_prime_UTR" :
            gff_dict[keyrecord].is_3UTR += 1
        else:
            continue
    return gff_dict

def translate_exons(genomeFile, genomeGFF, exonF, outfile):           # Translating the excised nucleotide sequences in-frame and from the proper strand
    exon_seqs = excise_exons(genomeFile, exonF)
    exon_info = gff_read(genomeGFF)
    trans_fasta = []
    fastafile_name = outfile + ".fasta"
    spreadsheet_name = outfile + "_exon_sheet.tsv"
    fastafile = open(fastafile_name, "w")
    spreadsheet = open(spreadsheet_name, "w")
    fasta_str = ""
    spreadsheet_str = "Exon ID\tExon\tCDS\t5UTR\t3UTR\tSeq Length\n"

    for exon in exon_seqs.keys():

        exon_info[exon].sampleType = exon_seqs[exon][1]

        if exon_info[exon].strand == "+":                    # Identifying which strand to translate
            exon_info[exon].seq = Seq(exon_seqs[exon][0], generic_dna)  
        elif exon_info[exon].strand == "-":
            exon_info[exon].seq = Seq(exon_seqs[exon][0], generic_dna).reverse_complement()
        elif exon_info[exon].strand == "none":               # Some exons are exclusively in UTR regions, and thus have no strand or phase for translation purposes
            exon_info[exon].inframe_seq = "UTR REGION"
            exon_info[exon].trans = "UTR REGION"

        if exon_info[exon].inframe_seq != "UTR REGION":
            if exon_info[exon].phase == "0":                     # Determining phase (frame) for reading nuc seq
                exon_info[exon].inframe_seq = exon_info[exon].seq 
            elif exon_info[exon].phase == "1":
                exon_info[exon].inframe_seq = exon_info[exon].seq[1:len(exon_info[exon].seq)-2]
            elif exon_info[exon].phase == "2":
                exon_info[exon].inframe_seq = exon_info[exon].seq[2:len(exon_info[exon].seq)-1]
            exon_info[exon].trans = exon_info[exon].inframe_seq.translate(to_stop=True)
            fasta_str += ">{}\n{}\n".format(exon, exon_info[exon].trans)

        spreadsheet_str += "{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(exon_info[exon].sampleType, exon_info[exon].chromStart, exon_info[exon].is_exon, exon_info[exon].is_cds, exon_info[exon].is_5UTR, exon_info[exon].is_3UTR, len(exon_info[exon].inframe_seq))

#        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(exon_info[exon].sampleType, exon_info[exon].chromStart, exon_info[exon].is_exon, exon_info[exon].is_cds, exon_info[exon].is_5UTR, exon_info[exon].is_3UTR, len(exon_info[exon].inframe_seq), exon_info[exon].trans))
#    print(fasta_str)
#    print("\n")
#    print(spreadsheet_str)

    fastafile.write(fasta_str)
    fastafile.close()
    spreadsheet.write(spreadsheet_str)
    spreadsheet.close()


if __name__ == '__main__':
    gnomFasta = sys.argv[1]
    gnomGFF = sys.argv[2]
    exonFile = sys.argv[3]
    outfile_name = sys.argv[4]
    translate_exons(gnomFasta, gnomGFF, exonFile, outfile_name)
