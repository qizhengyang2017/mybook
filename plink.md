有两个网站，不知道它们之间的关系。harvard这个倾向于解释软件的逻辑。cog详细解释各种参数

https://zzz.bwh.harvard.edu/plink/dataman.shtml#recode

https://www.cog-genomics.org/plink/1.9/input#vcf

各种参数
https://www.cog-genomics.org/plink/1.9/index



The [--make-bed](https://zzz.bwh.harvard.edu/plink/data.shtml#bed) option does the same as --recode but creates binary files; these can also be filtered, etc, as described below.

```shell
module load plink
plink --vcf filter2_Q1000_SNPs_joint_376_MAF0.05.vcf.gz  --out filter2_Q1000_SNPs_joint_376_MAF0.05 --allow-no-sex --allow-extra-chr --make-bed
```

plink 使用说明
- plink 一旦用了`--make-bed` minor就在前面了（A1）
- vcf转plink的时候，不加`--make-bed`，ref当成A2 #plink 

```shell
# 不加--make-bed感觉不太好，因为后面在用plink做分析的话，都还是得加--make-bed之类的，否则可能没有输出
plink --vcf filter2_Q600_SNPs_joint_216_addID.vcf.gz --out filter2_Q600_SNPs_joint_216_addID --allow-no-sex --allow-extra-chr
```
https://www.cog-genomics.org/plink/1.9/input#vcf

> VCF reference alleles are set to [A2](https://www.cog-genomics.org/plink/1.9/data#ax_allele) by the autoconverter even when they appear to be minor. However, to maintain backwards compatibility with PLINK 1.07, PLINK 1.9 normally forces major alleles to A2 during its loading sequence. One workaround is permanently keeping the .bim file generated during initial conversion, for use as [--a2-allele](https://www.cog-genomics.org/plink/1.9/data#ax_allele) input whenever the reference sequence needs to be recovered. (If you use this method, note that, when your initial conversion step invokes --make-bed instead of [just --out](https://www.cog-genomics.org/plink/1.9/input#keep_autoconv), you also need [--keep-allele-order](https://www.cog-genomics.org/plink/1.9/data#ax_allele) to avoid losing track of reference alleles before the very first write, because --make-bed triggers the regular loading sequence.)



有些时候想要输出必须加 --make-bed 或者 --recode。否则就报错
/data/cotton/zyqi/gwas_419/twas/LDREF
```shell
plink --bfile fHBAU_Q1000_SNP001 --out fHBAU_Q1000_SNP001.1 --allow-no-sex --allow-extra-chr --chr 1 --make-bed
```
  
  
  