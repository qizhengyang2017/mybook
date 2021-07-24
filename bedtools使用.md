
module load BEDTools/2.27

bedtools intersect -a introg_1based.bed -b Ghirsutum_gene_model_Ghir_number_1based_tab.bed -wa -wb|bedtools groupby -i - -g 1-3 -c 7 -o collapse 

bedtools intersect -a introg_1based.bed -b Ghirsutum_gene_model_Ghir_number_1based_tab.bed -wa -wb|bedtools groupby  -c 7 -o collapse > introg_gene_within.txt

