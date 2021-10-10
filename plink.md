有两个网站，不知道它们之间的关系。harvard这个倾向于解释软件的逻辑。cog详细解释各种参数

https://zzz.bwh.harvard.edu/plink/dataman.shtml#recode

https://www.cog-genomics.org/plink/1.9/input#vcf

各种参数
https://www.cog-genomics.org/plink/1.9/index



The [--make-bed](https://zzz.bwh.harvard.edu/plink/data.shtml#bed) option does the same as --recode but creates binary files; these can also be filtered, etc, as described below.

module load plink

plink --vcf filter2_Q1000_SNPs_joint_376_MAF0.05.vcf.gz  --out filter2_Q1000_SNPs_joint_376_MAF0.05 --allow-no-sex --allow-extra-chr --make-bed