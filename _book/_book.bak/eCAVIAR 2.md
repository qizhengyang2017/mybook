2021年09月18日

path: ~/ga/expression/expression_data/ecaviar
conda activate mashr




每个基因的plink文件：
- 需要表达量数据bed文件，==做ecaviar并不需要==
~/ga/expression/expression_data/Ga_12DPA_AllSamples_199_FPKM_AllStages_deleteConfig.bed 



基因型文件
~/ga/tensorQTL/Genotypes/filter2_Q600_SNPs_joint_216_addID


eQTL
/data/cotton/zyqi/tensorQTL_nominal/nominal_allChr/4D.gz

GWAS
  /data/cotton/zyqi/Ga_GWAS/UHML_ID_out
  得到某个区间内的基因
 
 - [x] bedtools提取基因

~/ga/expression/expression_data/ecaviar

- [x] 提取基因表达量
- [x] 和egene取交集
- [x] extract locus 
- [x] get gwas Z eQTL Z

~/ga/expression/expression_data/ecaviar  
bss "Rscript get_ecaviar_input.r 8DPA UHML"
- [x] run ecaviar

bss "sh ecaviar_run.sh UHML 20DPA"



~/cotton_fiber/fusion/TWAS_log_bak

提交任务

bss "sh extract_locus.sh 20DPA"

gene
/data/cotton/zyqi/Ga_GWAS/QTL.pos.txt










