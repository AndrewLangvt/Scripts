# This script was used to generate the sequencing names from my metadata library prep sheets. 
# i.e. it takes in dividual columns containng sample, tissue, sex, and treatment, and combines
# them with an underscore as the delimter

import csv
import sys

def csv_reader(filename):
    with open(filename, 'rU') as csvfile:
        file = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for line in file:
            line_str = ', '.join(line)
            elements = line_str.rstrip().split(",")
            elements[3] = elements[3].replace("/", "-")
            elements[3] = elements[3].replace("(", "")
            elements[3] = elements[3].replace(")", "")
            elements[3] = elements[3].lower()
            print(elements[3] + "_" + elements[6] + "_" + elements[5] + "_" + elements[7])

if __name__ == '__main__':
    file = sys.argv[1]
    csv_reader(file)
