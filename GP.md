## KAML
https://github.com/YinLiLin/KAML

集群目录
~/cotton_fiber/GP/KAML

本地目录
~/work_new/KAML



module load R/microsoft-r-open-MRO-3.5.1


```R
.libPaths("/public/home/zyqi/R/MRO_lib")
install.packages("devtools") #安装失败
```

本地源码包安装，成功！
```shell
module load R/microsoft-r-open-MRO-3.5.1
export R_LIBS_USER=/public/home/zyqi/R/MRO_lib
git clone https://github.com/YinLiLin/KAML
R CMD INSTALL KAML
```



使用模型，评估模型。plink文件如何转换。我需要去看源代码才行





## 注意
_**Note again:**_ _**`KAML`**_ has no function for adjusting the order of individuals. So please make sure the same order of individuals between phenotype and genotype.



~/cotton_fiber/gwas/trait_blup_376_filter_ranLineRep_EMMAX #EMMAX
比较了加不加cov，应该没有什么区别








## 贝叶斯方法
install.packages('BGLR')



## 其他
GS使用BLUE