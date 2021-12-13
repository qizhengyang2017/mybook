---
title: Flexible statistical methods for estimating and testing effects in genomic studies with multiple conditions
authors: Sarah M. Urbut, Gao Wang, Peter Carbonetto, Matthew Stephens
year: 2018
---

 

## UrLs
**重要的链接**

Multivariate adaptive shrinkage (mash) software, https://github. com/stephenslab/mashr; code and data resources for GTEx analysis, https://github.com/stephenslab/gtexresults, https://doi.org/10.5281/zenodo.1296399; GTEx project, http://gtexportal.org; adaptive shrinkage (ash) software, https://github.com/stephens999/ ashr; Sparse Factor Analysis (SFA) software, http://stephenslab.uchi- cago.edu/software.html; Extreme Deconvolution software, https:// github.com/jobovy/extreme-deconvolution; METASOFT software, http://genetics.cs.ucla.edu/meta; Matrix eQTL software, http:// www.bios.unc.edu/research/genomic_software/Matrix_eQTL.




## mashr针对的问题

Genomic studies often involve ==estimating and comparing many effects across multiple conditions== or outcomes. For example, these studies can include changes in expression of many genes under multiple treatments1, differences in histone methylation at many genomic locations in multiple cell lines2, effects of many genetic variants on risk of multiple diseases3, and effects of expression quantitative trait loci (eQTLs) in multiple cell types or tissues4,5,6. Analyses often aim to identify ‘significant’ nonzero effects, and to identify differences in effects among conditions (for example, tissue-specific effects), which may yield biological insights.

A common analysis strategy for such studies is to separately analyze each condition in turn and then compare the significant results among conditions. Although appealingly simple, this condition-by-condition approach is unsatisfactory in several ways: it under-represents sharing of effects among conditions because shared effects will be insignificant in some conditions by chance, and it misses the power gains that come from sharing information across conditions5.
-   此类研究的常见分析策略是依次单独分析每个条件，然后比较条件之间的显着结果。
-   尽管很简单，但这种逐个条件的方法在几个方面并不令人满意：它低估了条件之间的效果共享，因为共享效应在某些条件下偶然是不显著的，并且它失去了来自跨条件共享信息的功率增益

We introduce more flexible statistical methods that combine the most attractive features of existing approaches while overcoming their major limitations. The methods, which we refer to as multivariate adaptive shrinkage (mash), build on recent approaches16 for testing and estimating effects in a single condition, extending these approaches to multiple conditions. Key features of mash include: (1) it is flexible, allowing for both shared and condition-specific effects, and arbitrary patterns of correlation among conditions; (2) it is computationally tractable for hundreds of thousands of tests in dozens of conditions, or more; (3) it provides not only measures of significance, but also estimates of effect sizes, together with measures of uncertainty; (4) it is adaptive, meaning that ==its behavior adapts to patterns present in the data==; and (5) it is generic, requiring only a matrix containing the observed effects in each condition and a matrix of the corresponding standard errors. (Alternatively, mash can be supplied with just a matrix of Z scores, although this reduces the ability to estimate effect sizes.) Together, these features make mash a flexible and widely applicable method for estimating and testing multiple effects in multiple conditions.
-   我们引入了更灵活的统计方法，这些方法结合了现有方法最吸引人的特点，同时克服了它们的主要局限性。
-   我们将这些方法称为多元自适应收缩 (mash)，它建立在最近用于测试和估计单一条件下效果的方法的基础上，将这些方法扩展到多种条件。
-   mash 的主要特点包括： (1) 它是灵活的，允许共享和特定条件的影响，以及条件之间的任意关联模式；
-   (2) 在数十种或更多条件下的数十万次测试在计算上易于处理；
-   (3) 它不仅提供显着性的度量，而且提供效应大小的估计以及不确定性的度量；
-   (4) 它是自适应的，意味着它的行为适应数据中存在的模式；
-   (5) 它是通用的，只需要一个包含每个条件下观察到的效果的矩阵和一个相应标准误差的矩阵。
-   （或者，mash 可以只提供一个 Z 分数矩阵，尽管这会降低估计效果大小的能力。）这些功能一起使 mash 成为一种灵活且广泛适用的方法，用于在多种条件下估计和测试多种效果。

To demonstrate the potential for mash to provide new insights, we applied it to analyze cis eQTL effects in 16,069 genes across 44 human tissues. ==Focusing on the strongest cis eQTLs==, we found that although most eQTLs are shared by many tissues, effect sizes can still vary considerably. Our results suggest that when assessing effects that are tissue specific versus tissue consistent, careful attention should be paid to the sizes of effects, and not only to tests for significance. #引用

他这篇文章只关注效应最强的那个cis eQTL。