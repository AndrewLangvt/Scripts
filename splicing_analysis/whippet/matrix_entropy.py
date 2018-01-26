import sys
import gzip


def count_genes(sample_file):
    with gzip.open(sample_file, 'rt') as sampleIDs:

        tot_events = []
        for line in sampleIDs.readlines()[1:]:
            column = line.rstrip().split('\t')
            tot_events.append(column[0])
        gene_count = len(set(tot_events))
    return gene_count


def gen_matrix(matrix_list, sample_file, name, gene_count):
    with open(matrix_list, 'r') as matrixIDs, gzip.open(sample_file, 'rt') as sampleIDs:

        out_line = ""
        sample_dict = {}
        
        identifiers = str(sample_file).replace('.psi.gz', '').split('_')
        sex = identifiers[1]
        tissue = identifiers[2]
        treatment = identifiers[3]

        out_line += str(name) + '\n' + identifiers[1] + '\n' + identifiers[2] + '\n' + identifiers[3] + '\n'
        for line in sampleIDs.readlines()[1:]:
            column = line.rstrip().split('\t')

            if column[10] == 'NA':
                ent_val = 0.0
            else:
                ent_val = str(column[10])

            if column[6] == 'NA':
                sample_dict[column[2]] = 0.0
            elif float(column[6]) <= 0.3:
                sample_dict[column[2]] = float(ent_val)/float(gene_count)
            elif float(column[6]) > 0.3:
                sample_dict[column[2]] = 0.0
            
        for line in matrixIDs:
            id = line.rstrip()
            if id in sample_dict.keys():
                out_line += str(sample_dict[id]) + '\n'
            else:
                out_line += '0.0\n'
#        return out_line
        final_line = out_line.rstrip()	
        print(final_line)

if __name__ == '__main__':
    matrix_file = sys.argv[1]
    sample_file = sys.argv[2]
    name = str(sys.argv[3])
    gene_count = count_genes(sample_file)

gen_matrix(matrix_file, sample_file, name, gene_count)
        
