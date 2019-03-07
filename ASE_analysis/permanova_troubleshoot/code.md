```
column_list <- c("GeneID", "male_hypothalamus_control", "male_hypothalamus_bldg", "male_hypothalamus_lay", 
                 "male_hypothalamus_inc.d3", "male_hypothalamus_inc.d9", "male_hypothalamus_inc.d17", 
                 "male_hypothalamus_hatch", "male_hypothalamus_n5", "male_hypothalamus_n9", "male_pituitary_control", 
                 "male_pituitary_bldg", "male_pituitary_lay", "male_pituitary_inc.d3", "male_pituitary_inc.d9", 
                 "male_pituitary_inc.d17", "male_pituitary_hatch", "male_pituitary_n5", "male_pituitary_n9", 
                 "male_gonad_control", "male_gonad_bldg", "male_gonad_lay", "male_gonad_inc.d3", "male_gonad_inc.d9", 
                 "male_gonad_inc.d17", "male_gonad_hatch", "male_gonad_n5", "male_gonad_n9", 
                 "female_hypothalamus_control", "female_hypothalamus_bldg", "female_hypothalamus_lay", 
                 "female_hypothalamus_inc.d3", "female_hypothalamus_inc.d9", "female_hypothalamus_inc.d17", 
                 "female_hypothalamus_hatch", "female_hypothalamus_n5", "female_hypothalamus_n9", 
                 "female_pituitary_control", "female_pituitary_bldg", "female_pituitary_lay", 
                 "female_pituitary_inc.d3", "female_pituitary_inc.d9", "female_pituitary_inc.d17", 
                 "female_pituitary_hatch", "female_pituitary_n5", "female_pituitary_n9", "female_gonad_control", 
                 "female_gonad_bldg", "female_gonad_lay", "female_gonad_inc.d3", "female_gonad_inc.d9", 
                 "female_gonad_inc.d17", "female_gonad_hatch", "female_gonad_n5", "female_gonad_n9", "Location")

column_names <- c("GeneID", "male_hypothalamus_control", "male_hypothalamus_bldg", "male_hypothalamus_lay", 
                  "male_hypothalamus_inc-d3", "male_hypothalamus_inc-d9", "male_hypothalamus_inc-d17", 
                  "male_hypothalamus_hatch", "male_hypothalamus_n5", "male_hypothalamus_n9", "male_pituitary_control", 
                  "male_pituitary_bldg", "male_pituitary_lay", "male_pituitary_inc-d3", "male_pituitary_inc-d9", 
                  "male_pituitary_inc-d17", "male_pituitary_hatch", "male_pituitary_n5", "male_pituitary_n9", 
                  "male_gonad_control", "male_gonad_bldg", "male_gonad_lay", "male_gonad_inc-d3", "male_gonad_inc-d9", 
                  "male_gonad_inc-d17", "male_gonad_hatch", "male_gonad_n5", "male_gonad_n9", 
                  "female_hypothalamus_control", "female_hypothalamus_bldg", "female_hypothalamus_lay", 
                  "female_hypothalamus_inc-d3", "female_hypothalamus_inc-d9", "female_hypothalamus_inc-d17", 
                  "female_hypothalamus_hatch", "female_hypothalamus_n5", "female_hypothalamus_n9", 
                  "female_pituitary_control", "female_pituitary_bldg", "female_pituitary_lay", 
                  "female_pituitary_inc-d3", "female_pituitary_inc-d9", "female_pituitary_inc-d17", 
                  "female_pituitary_hatch", "female_pituitary_n5", "female_pituitary_n9", "female_gonad_control", 
                  "female_gonad_bldg", "female_gonad_lay", "female_gonad_inc-d3", "female_gonad_inc-d9", 
                  "female_gonad_inc-d17", "female_gonad_hatch", "female_gonad_n5", "female_gonad_n9", "Location")

columns <- c("male_hypothalamus_control", "male_hypothalamus_bldg", "male_hypothalamus_lay", 
             "male_hypothalamus_inc-d3", "male_hypothalamus_inc-d9", "male_hypothalamus_inc-d17", 
             "male_hypothalamus_hatch", "male_hypothalamus_n5", "male_hypothalamus_n9", "male_pituitary_control", 
             "male_pituitary_bldg", "male_pituitary_lay", "male_pituitary_inc-d3", "male_pituitary_inc-d9", 
             "male_pituitary_inc-d17", "male_pituitary_hatch", "male_pituitary_n5", "male_pituitary_n9", 
             "male_gonad_control", "male_gonad_bldg", "male_gonad_lay", "male_gonad_inc-d3", "male_gonad_inc-d9", 
             "male_gonad_inc-d17", "male_gonad_hatch", "male_gonad_n5", "male_gonad_n9", 
             "female_hypothalamus_control", "female_hypothalamus_bldg", "female_hypothalamus_lay", 
             "female_hypothalamus_inc-d3", "female_hypothalamus_inc-d9", "female_hypothalamus_inc-d17", 
             "female_hypothalamus_hatch", "female_hypothalamus_n5", "female_hypothalamus_n9", 
             "female_pituitary_control", "female_pituitary_bldg", "female_pituitary_lay", 
             "female_pituitary_inc-d3", "female_pituitary_inc-d9", "female_pituitary_inc-d17", 
             "female_pituitary_hatch", "female_pituitary_n5", "female_pituitary_n9", "female_gonad_control", 
             "female_gonad_bldg", "female_gonad_lay", "female_gonad_inc-d3", "female_gonad_inc-d9", 
             "female_gonad_inc-d17", "female_gonad_hatch", "female_gonad_n5", "female_gonad_n9")

all_chroms <- c('CM007525.1', 'CM007526.1', 'CM007527.1', 'CM007528.1', 'CM007529.1', 
                'CM007530.1', 'CM007531.1', 'CM007532.1', 'CM007533.1', 'CM007534.1', 
                'CM007535.1', 'CM007536.1', 'CM007537.1', 'CM007538.1', 'CM007539.1', 
                'CM007523.1', 'CM007540.1', 'CM007541.1', 'CM007542.1', 'CM007543.1', 
                'CM007544.1', 'CM007545.1', 'CM007546.1', 'CM007547.1', 'CM007548.1', 
                'CM007549.1', 'CM007550.1', 'CM007551.1', 'CM007524.1')

ASE_byChromLoc_all <- read.csv('~/Desktop/AlleleSpecificExpression/ASE_matrix/Location_of_GeneCounts_byChromosome_at_0.6.tsv', sep = '\t')
ALL_ASE_byChromLoc <- ASE_byChromLoc_all[,column_list]
colnames(ALL_ASE_byChromLoc) <- column_names
ALL_ASE_byChromLoc <- cbind(ALL_ASE_byChromLoc, count = rowSums(ALL_ASE_byChromLoc[,c(columns)]))
ALL_ASE_byChromLoc$chrom <- sapply(strsplit(as.character(ALL_ASE_byChromLoc$Location), '_'), `[`, 1)

ALL_ASE_byChromLoc$chrom <- factor(ALL_ASE_byChromLoc$chrom, levels = all_chroms)
ALL_ASE_byChromLoc <- dplyr::filter(.data = ALL_ASE_byChromLoc, !is.na(chrom))

ALL_ASE_byChromLoc$Location <- NULL
ALL_ASE_byChromLoc$count <- NULL
ALL_ASE_byChromLoc$chrom <- NULL
transp_ALL_ASE_byChromLoc <- as.data.frame(t(ALL_ASE_byChromLoc))
colnames(transp_ALL_ASE_byChromLoc) <- transp_ALL_ASE_byChromLoc[1,]
transp_ALL_ASE_byChromLoc <- transp_ALL_ASE_byChromLoc[-1,] 
geneIDs <- colnames(transp_ALL_ASE_byChromLoc)   # this will feed in as column names for the distance matrix below
transp_ALL_ASE_byChromLoc$Sex <- sapply(strsplit(as.character(rownames(transp_ALL_ASE_byChromLoc)), '_'), `[`, 1)
transp_ALL_ASE_byChromLoc$Tissue <- sapply(strsplit(as.character(rownames(transp_ALL_ASE_byChromLoc)), '_'), `[`, 2)
transp_ALL_ASE_byChromLoc$Time <- sapply(strsplit(as.character(rownames(transp_ALL_ASE_byChromLoc)), '_'), `[`, 3)

library(vegan)
# Identifies if significant differences by group
dist_mtrx <- vegdist(transp_ALL_ASE_byChromLoc[geneIDs], dist = 'binomial') # all columns except for the meta variables
```

## Questions with adonis2
1) Should I be including multiple permutations with adonis2?
2) This is probably a VERY easy answer... where is the p-value indicating a difference between my meta groups? (i.e. between sexes for the first one)
3) I'm wondering if I have the code right for the adonis2 comparing Sex-tissue-time groups (3rd one below), as some of the values come out as NAs...
```
veg_permanova_sex <- adonis2(dist_mtrx ~ Time, data = transp_ALL_ASE_byChromLoc)  # testing for differences between meta variable in ASE gene identity pres/abs
summary(veg_permanova_sex)
```
```
       Df           SumOfSqs           R2               F           Pr(>F)    
 Min.   : 8.00   Min.   :1.144   Min.   :0.2321   Min.   :1.7   Min.   :0.01  
 1st Qu.:26.50   1st Qu.:2.465   1st Qu.:0.5000   1st Qu.:1.7   1st Qu.:0.01  
 Median :45.00   Median :3.786   Median :0.7679   Median :1.7   Median :0.01  
 Mean   :35.33   Mean   :3.287   Mean   :0.6667   Mean   :1.7   Mean   :0.01  
 3rd Qu.:49.00   3rd Qu.:4.359   3rd Qu.:0.8840   3rd Qu.:1.7   3rd Qu.:0.01  
 Max.   :53.00   Max.   :4.931   Max.   :1.0000   Max.   :1.7   Max.   :0.01  
                                                  NA's   :2     NA's   :2  
```
```
veg_permanova_sex_tiss <- adonis2(dist_mtrx ~ Sex * Tissue, data = transp_ALL_ASE_byChromLoc) # testing for interactions between multiple meta variables
summary(veg_permanova_sex_tiss)
```
```       Df          SumOfSqs            R2                F              Pr(>F)     
 Min.   : 1.0   Min.   :0.2231   Min.   :0.04525   Min.   : 3.665   Min.   :0.001000  
 1st Qu.: 2.0   1st Qu.:0.4541   1st Qu.:0.09209   1st Qu.: 3.697   1st Qu.:0.001000  
 Median : 2.0   Median :1.3314   Median :0.27002   Median : 3.729   Median :0.001000  
 Mean   :21.2   Mean   :1.9723   Mean   :0.40000   Mean   : 6.110   Mean   :0.002667  
 3rd Qu.:48.0   3rd Qu.:2.9222   3rd Qu.:0.59265   3rd Qu.: 7.332   3rd Qu.:0.003500  
 Max.   :53.0   Max.   :4.9307   Max.   :1.00000   Max.   :10.935   Max.   :0.006000  
                                                   NA's   :2        NA's   :2 
```
```
veg_permanova_allMeta <- adonis2(dist_mtrx ~ Sex * Tissue * Time, data = transp_ALL_ASE_byChromLoc) # testing for interactions between multiple meta variables
summary(veg_permanova_allMeta)
```
```       Df           SumOfSqs           R2               F           Pr(>F)   
 Min.   : 0.00   Min.   :0.000   Min.   :0.0000   Min.   : NA   Min.   : NA  
 1st Qu.:26.50   1st Qu.:2.465   1st Qu.:0.5000   1st Qu.: NA   1st Qu.: NA  
 Median :53.00   Median :4.931   Median :1.0000   Median : NA   Median : NA  
 Mean   :35.33   Mean   :3.287   Mean   :0.6667   Mean   :NaN   Mean   :NaN  
 3rd Qu.:53.00   3rd Qu.:4.931   3rd Qu.:1.0000   3rd Qu.: NA   3rd Qu.: NA  
 Max.   :53.00   Max.   :4.931   Max.   :1.0000   Max.   : NA   Max.   : NA  
                                                  NA's   :3     NA's   :3  
 ```

#### Identifying the genes that are significantly different by group using the pairwise function for adonis
`pariwise.adonis(dist_mtrx, transp_ALL_ASE_byChromLoc$Sex) # use my distance matrix as I am in binary world (bray curtis is relative abundance, which is what he uses in this package)`
## Question: What package does this come from? All I have been able to find is some stand-alone pairwise.adonis function that someone wrote... 
###   https://www.researchgate.net/post/How_can_I_do_PerMANOVA_pairwise_contrasts_in_R

#### Using simper and kruskal to identify gene differences between groups
```
transp_ALL_ASE_byChromLoc$tissue_genes <- simper(transp_ALL_ASE_byChromLoc[geneIDs], transp_ALL_ASE_byChromLoc$Tissue, permutations=1)  #outputs a gene list for each of the tissues
##### let simper identify what is different between groups, use kruskal to confirm

transp_ALL_ASE_byChromLoc$bonf1 <- kruskal.test(transp_ALL_ASE_byChromLoc$tissue_genes ~ transp_ALL_ASE_byChromLoc$Tissue) # confirm what simper found
p.adjust(transp_ALL_ASE_byChromLoc$bonf1, method = 'bonferonni')
```
outputs the following error:
```
Error in model.frame.default(formula = transp_ALL_ASE_byChromLoc$tissue_genes ~  : 
  invalid type (list) for variable 'transp_ALL_ASE_byChromLoc$tissue_genes'
```

#### Running multipart to identify the "indicator genes" of each time point
(multipart apparently needs a "A matrix with same number of rows as in y, columns coding the levels of sampling hierarchy")

```
hierarchy <- transp_ALL_ASE_byChromLoc[,c('Time', 'Tissue', 'Sex')]
hierarchy$Sex <- factor(hierarchy$Sex, levels = c('male', 'female'))
hierarchy$Tissue <- factor(hierarchy$Tissue, levels = c('hypothalamus', 'pituitary' , 'gonad'))
hierarchy$Treatment <- factor(hierarchy$Time, levels = c('control', 'bldg', 'lay', 'inc-d3', 'inc-d9', 'inc-d17', 'hatch', 'n5', 'n9'))
sex_most_sig <- multipart(dist_mtrx, hierarchy)
```
## outputs the following error:
```
Error in multipart.default(dist_mtrx, hierarchy) : 
  levels are not perfectly nested
  ```
