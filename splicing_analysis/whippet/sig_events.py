"""This script will identify all significant events (PSI>0.1 & p>0.95) occuring in the diff.gz output files from Whippet."""

import re
import sys
import gzip

def sig_ev(fname):
    with gzip.open(fname, 'rt') as file2 :
        file = file2.readlines()[1:]
        tot=0
        ce=0
       	aa=0
       	ad=0
       	ri=0
       	ts=0
       	te=0
       	af=0
       	al=0
       	bs=0
        entp=0
        vhentp=0
        Sentp=0
        Svhentp=0
        sig=0
       	Sce=0
        Saa=0
        Sad=0
        Sri=0
        Sts=0
        Ste=0
        Saf=0
        Sal=0
        Sbs=0

        for line in file:
            tot+=1
            column = line.rstrip().split("\t")

            prob = float(column[8])
            psi = float(column[7])
            event = str(column[4])
            entropy = float(column[10])

            if event == "CE":
                ce+=1
            elif event == "AA":
                aa+=1
       	    elif event == "AD":
       	       	ad+=1
       	    elif event == "RI":
       	       	ri+=1
       	    elif event == "TS":
       	       	ts+=1
       	    elif event == "TE":
       	       	te+=1
            elif event == "AF":
                af+=1
            elif event == "AL":
                al+=1
            elif event == "BS":
                bs+=1
 
            if float(1.0) <= entropy  < float(2.0):
                entp+=1
            if entropy >= float(2.0):
                vhentp+=1
            if prob >= float(0.95) :
                if psi >= float(0.1) :
                    sig+=1
                    if float(1.0) <= entropy < float(2.0):
                        Sentp+=1
                    if entropy >= float(2.0):
                        Svhentp+=1
                    if event == "CE":
                        Sce+=1
                    elif event == "AA":
                        Saa+=1
                    elif event == "AD":
                        Sad+=1
                    elif event == "RI":
                        Sri+=1
                    elif event == "TS":
                        Sts+=1
                    elif event == "TE":
                        Ste+=1
                    elif event == "AF":
                        Saf+=1
                    elif event == "AL":
                        Sal+=1
                    elif event == "BS":
                        Sbs+=1
                else:
                    continue
            else:
                continue

        name_trimmed = re.sub(r'.*/', '', str(fname))
        print("")
        print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
        print(name_trimmed)
        print("EVENTS BY TYPE                           " + "\t" + "Total" + "\t" + "Significant" + "           ")
        print("======================================================================")
        print("All Events                               " + "\t" + str(tot) + "\t" + str(sig) + "           ")
        print("Core Exon                                " + "\t" + str(ce) + "\t" + str(Sce) + "           ")
       	print("Alternative Acceptor                     " + "\t" + str(aa) + "\t" + str(Saa) + "           ")
        print("Alternative Donor                        " + "\t" + str(ad) + "\t" + str(Sad) + "           ")
        print("Retained Intron                          " + "\t" + str(ri) + "\t" + str(Sri) + "           ")
        print("Tandem Transcription Start Site          " + "\t" + str(ts) + "\t" + str(Sts) + "           ")
        print("Tandem Alternative Polyadenylation Site  " + "\t" + str(te) + "\t" + str(Ste) + "           ")
        print("Alternative First Exon                   " + "\t" + str(af) + "\t" + str(Saf) + "           ")
        print("Alternative Last Exon                    " + "\t" + str(al) + "\t" + str(Sal) + "           ")
        print("Circular Back-splicing                   " + "\t" + str(bs) + "\t" + str(Sbs) + "           ")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("High Entropy                             " + "\t" + str(entp) + "\t" + str(Sentp) + "           ")
        print("V. High Entropy                          " + "\t" + str(vhentp) + "\t" + str(Svhentp) + "           ")
        print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
        print("")

if __name__ == '__main__':
    filename = sys.argv[1]
    sig_ev(filename)
