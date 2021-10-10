~/cotton_fiber/locus_plot
```
使用gtex环境

1. gff2转成gtf用的是python包。bioinfokit。
>>> from bioinfokit.analys import gff
>>> gff.gff_to_gtf(file="Athaliana_167_TAIR10.gene_chr1.gff3")

2. 用的当前目录下的annotation脚本

3. 标准化后的表达量去掉了不在染色体上的基因
```


![[Pasted image 20210910213042.png]]

