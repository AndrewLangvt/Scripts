# JunctionSeq Analysis
# Andrew S. Lang
# Created: 26OCT2017
# Last Modified: 31OCT2017

#JunctionSeq Install
source("http://hartleys.github.io/JunctionSeq/install/JS.install.R");
JS.install();

#Load JunctionSeq:
library("JunctionSeq"); 

#~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%
#~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~% JunctionSeq Analysis Pipeline %~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%
#~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%

JunctionFunction <- function(comparison, location, out_loc) {

  assign(paste0(comparison, "_decoder"),                                            # Generate decoder file
    read.table(paste0(location, comparison, "/", comparison, "_decoder_file.txt"),
    header=T,stringsAsFactors=F));
  
  dcdr_f = get(paste0(comparison, "_decoder"))                                        # Assigning variable as decoder object
  
  #The count files:
  assign(paste0(comparison, "_countFiles"), paste0(                                   # Assign count files to R objects
    paste0(location, comparison, "/"),
    dcdr_f$sample.ID,
    "/QC.spliceJunctionAndExonCounts.withNovel.forJunctionSeq.txt.gz"
  ));
  
  #Run the analysis:
  samp_files = get(paste0(comparison, "_countFiles"))                                 # Assign comparison_countFiles object to samp_files
  gff_file = paste0(location, comparison, "/withNovel.forJunctionSeq.gff.gz")         # Generating string name for gff with novel junctions
                   
  assign(paste0(comparison, "_jscs"), runJunctionSeqAnalyses(                         # Run the JunctionSeq analysis
    sample.files = samp_files,
    sample.names = dcdr_f$sample.ID,
    condition = dcdr_f$group.ID,
    flat.gff.file = gff_file,
    nCores = 2,
    verbose=TRUE,
    debug.mode = TRUE));
  
  jseq = get(paste0(comparison, "_jscs"))                                             # Assign analysis output object to jseq
  count_out = paste0(out_loc, comparison, "/")                                        # Assign string for location of count output
  dir.create(count_out)                                                               # Create directory for count output
                   
  writeCompleteResults(jseq,                                                          # Write all results from analysis run
    outfile.prefix= paste0(count_out, comparison, "_"),
    save.jscs = TRUE);
                   
  plot_out = paste0(count_out, "plots")                                               # Assign location for plots to be output
  dir.create(plot_out)                                                                # Create directory for plots to be output
                   
  buildAllPlots(                                                                      # Build plots for all significant events
    jscs=jseq,
    FDR.threshold = 0.01,
    outfile.prefix = plot_out,
    variance.plot = TRUE,
    ma.plot = TRUE,
    rawCounts.plot=TRUE,
    verbose = TRUE);
  
  plotDispEsts(jseq);                                                                 # Generate dispersion estimates plot
  plotMA(jseq, FDR.threshold=0.05);                                                   # Generate MA plot comparing two treatments
}


#~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%
# Provide list of Qorts output directory names as 'sample_list' and location of said directories
# This pipeline will then perform JunctionSeq analysis on all directories

sample_list = c(
  "femaleG_SvC",
  "femaleH_SvC",
  "femaleP_SvC",
  "maleG_SvC",
  "maleH_SvC",
  "maleP_SvC",
  "gonadC_MvF",
  "gonadS_MvF",
  "hypothalamusC_MvF",
  "hypothalamusS_MvF",
  "pituitaryC_MvF",
  "pituitaryS_MvF")

  print("")
  print("%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%")
  print(paste0("<><><><><><><><>< Now Running Analysis for ", sampleID, " ><><><><><><><><>"))
  print("%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%")
  print("")
  
  JunctionFunction(
    comparison = sampleID,
    location = "/Users/andrewlang/Desktop/junctionSeq_analysis/counts/",                 # For both location and out_loc, string must end with '/'
    out_loc = "/Users/andrewlang/Desktop/junctionSeq_analysis/output/")                  # and out_loc must already exist

  print("")
  print(paste0("<><><><><><><><><>< ", sampleID, " Analysis Complete ><><><><><><><><><><>"))
  print("%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%")
  print("")
  
#~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%
#~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~% NOTHING FOLLOWS %~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%
#~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%
