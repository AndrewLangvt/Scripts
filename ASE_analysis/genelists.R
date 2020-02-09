# from many files to two. indicator and unique genes
library(tidyverse)
library(cowplot)

# formatting and color
stagelevels <- c("control", "bldg", "lay", "inc-d3", "inc-d9", "inc-d17",
                "hatch", "n5", "n9")

stagelevelsnohiphen <- c("control", "bldg", "lay", 
                  "incd3", "incd9", "incd17",
                 "hatch", "n5", "n9")

tissuelevels <- c("hyp", "pit", "gon")
sexlevels <- c("female", "male")


colorsstage <- c("control" = "#cc4c02", "bldg"= "#fe9929", "lay"= "#fed98e", 
                    "incd3"= "#78c679", "incd9"= "#31a354", "incd17"= "#006837", 
                    "hatch"= "#08519c","n5"= "#3182bd", "n9"= "#6baed6")

colorstissue <- c("hyp" = "#d95f02",
                  "pit" = "#1b9e77",
                  "gon" =  "#7570b3")

colorssex <- c("female" = "#969696", "male" = "#525252")

colorsall <- c(colorstissue, colorssex, colorsstage)


## indicator genes

data_path <- "./GeneLists/indicators/"   # path to the data
files <- dir(data_path, pattern = "*.txt") # get file names
filesdf <- as.data.frame(files)

indicatorsgenes <- files %>%
    set_names() %>%
  map_df(~ read.table(file.path(data_path, .),  sep = "\t", 
                      row.names = NULL,  fill=TRUE), .id = "source")  %>% 
  mutate_at(.vars = "source",  .funs = gsub,
            pattern = ".txt", replacement = "") %>%
  dplyr::rename("group" = "source", "geneid" = "V1") %>%
  dplyr::filter(!geneid %in% group)  %>%
   mutate_at(.vars = "group",  .funs = gsub,
            pattern = "_df", replacement = "") 
head(indicatorsgenes)

# this nex summary confirms data fromfigure 7
indsum <- indicatorsgenes %>% group_by(group) %>% 
  summarize(ASEcount = n()) %>% arrange(desc(ASEcount)) %>%
  dplyr::mutate(level = sapply(strsplit(as.character(group),'\\_'), "[", 2),
                group = sapply(strsplit(as.character(group),'\\_'), "[", 1)) 


indsum$group <- factor(indsum$group,
                                levels = c(
                                  sexlevels, tissuelevels,
                                  stagelevelsnohiphen) 
)



themeASEcount <- function () { 
  theme_classic(base_size = 10) +
    theme(
      panel.grid.major  = element_blank(),  
      panel.grid.minor  = element_blank(),
      legend.position = "none") 
}

a <- indsum %>%
  filter(level != "time") %>%
  ggplot(aes(x = group, y = ASEcount,
                   fill = group, label = ASEcount)) +
  geom_bar(stat = "identity")  +
  geom_text(vjust = -0.5, size = 3) +
  themeASEcount() +
  scale_fill_manual(values = colorsall) +
  labs(x = "Sex, Tissue", y = "Allele-Specific Expression Gene Count") 

b <- indsum %>%
  filter(level == "time") %>%
  ggplot(aes(x = group, y = ASEcount,
                   fill = group, label = ASEcount)) +
  geom_bar(stat = "identity") +
  geom_text(vjust = -0.5, size = 3) +
  themeASEcount() + 
  scale_fill_manual(values = colorsall) +
  labs(x = "Parental Stage", y = NULL)

plot_grid(a,b, rel_widths = c(0.45, 0.55))

## unique genes

data_path <- "./GeneLists/uniq_lists/"   # path to the data
files <- dir(data_path, pattern = "*.txt") # get file names
filesdf <- as.data.frame(files)

uniqgenes <- files %>%
    set_names() %>%
  map_df(~ read_delim(file.path(data_path, .),  delim = "\t"), .id = "source")  %>% 
  mutate_at(.vars = "source",  .funs = gsub,
            pattern = "_uniq.txt", replacement = "") %>%
   dplyr::select(source, To) %>%
  dplyr::rename("comparison" = "source", "gene" = "To")  %>%
  group_by(comparison) %>%
    summarize(genes = str_c(gene, collapse = " ")) %>%
  dplyr::mutate(sex = sapply(strsplit(comparison,'\\_'), "[", 1),
                tissue = sapply(strsplit(comparison,'\\_'), "[", 2),
                stage = sapply(strsplit(comparison,'\\_'), "[", 3)) %>%
  select(sex, tissue, stage, genes) %>%
  pivot_wider(names_from = tissue, values_from = genes)  %>%
  select(sex, stage, hypothalamus, pituitary, gonad)

uniqgenes$stage <- factor(uniqgenes$stage, levels = stagelevels)

uniqgenes <- uniqgenes %>% dplyr::arrange(sex, stage)
head(uniqgenes)

write_csv(indicatorsgenes, "./GeneLists/indicators/indicatorsgenes.csv")
write_csv(uniqgenes, "./GeneLists/uniq_lists/uniqgenes.csv")