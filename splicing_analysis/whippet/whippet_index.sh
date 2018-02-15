# Generates indices for desired genome. I generally have this in the job 
# submission file just preceeding the whippet-quant step

julia /opt/packages/whippet/Whippet.jl-0.8/bin/whippet-index.jl \
--fasta /pylon2/mc3bg6p/al2025/isoform/colLiv2_genome/Rockdove_cliv2.gtf
--gtf /pylon2/mc3bg6p/al2025/isoform/colLiv2_genome/Rockdove_cliv2.gtf
--index /pylon2/mc3bg6p/al2025/isoform/whippet_analysis/index/ColLiv_v2

