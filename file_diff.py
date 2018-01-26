# Find File Difference

# AUTHOR = Andrew S. Lang
# DATE = 17APR2017

""" This script will parse through two files of sample/transcript IDs, and write a new file "transcript_difference.txt" containing all 
IDs that are uniqe to each file. """

import sys

def transcript_diff(filename1, filename2): #counting the number of words in a book
    file1 = open(filename1, "r")
    file2 = open(filename2, "r")
    output = open("transcript_difference.txt", "w")
    trans_dict = {}
    trans_dict2 = {}
    trans_diff = ""
    
    for line in file1:
        trans_dict[line] = ""
    
    for line in file2:
        trans_dict2[line] = ""

    for key in trans_dict.keys():
        if key not in trans_dict2.keys():
            trans_diff += key

    for	key2 in trans_dict2.keys():
        if key2 not in trans_dict.keys():
       	    trans_diff += key2
    
    output.write(trans_diff)
    file1.close()
    file2.close()
    output.close()

if __name__ == '__main__':
    filename1 = sys.argv[1]
    filename2 = sys.argv[2]

    transcript_diff(filename1, filename2)
