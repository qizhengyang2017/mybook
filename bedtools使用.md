
module load BEDTools/2.27

bedtools intersect -a introg_1based.bed -b Ghirsutum_gene_model_Ghir_number_1based_tab.bed -wa -wb|bedtools groupby -i - -g 1-3 -c 7 -o collapse 

bedtools intersect -a introg_1based.bed -b Ghirsutum_gene_model_Ghir_number_1based_tab.bed -wa -wb|bedtools groupby  -c 7 -o collapse > introg_gene_within.txt



bedtools intersect -a gene_rank.txt -b introg.txt -wa -wb|bedtools groupby -c 4 -o count




---
bedtools intersect -h

 `bedtools intersect -nonamecheck -a QTL_pos_range.bed -b change.Chr_genome_final_gene_deleteConfig.bed -wa -wb|bedtools groupby -i - -g 1-4 -c 8 -o collapse |les`
 
 
```
Chr01	7665162	9665164	FL
Chr02	7725282	9725284	FL
Chr05	84535943	86535945	FL
Chr06	99083472	101083474	FL
Chr07	85119545	87119547	FL
Chr03	132446703	134446705	FU
```



?? 这是什么warning?
如何report一个没有用的warning
https://github.com/arq5x/bedtools2/issues/248

***** WARNING: File change.Chr_genome_final_gene_deleteConfig.bed has a record where naming convention (leading zero) is inconsistent with other files:
Chr10   24508   28504   Garb_10G000010  .       -       EVM     gene    .       ID=Garb_10G000010


---
bedtools groupby -h

~/ga/hotspot/hot_scan_newCis/hotspot_all/tracks_c/bedtools_intersect

```
bedtools intersect -a 4D_hotspot.bed -b 4D_all.bed -wa -wb |bedtools groupby -g 1-5 -c 9,11 -o collapse|head
```

按第1-5列分组，9，11列summarize


---
hotspot和位点取交集
- [ ] 位点的LDblock区域




---
- [x] locus plot 更改图片大小
~/ga/ecaviar/locus_plot/new_locus_0929



