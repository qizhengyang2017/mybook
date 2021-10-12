
合并有表头的文件
`awk 'FNR==1 && NR!=1{next;}{print}' *.txt > final_merge_bin.txt`

In awk, `FNR` refers to the record number (typically the line number) in the current file and `NR` refers to the total record number. The operator `==` is a comparison operator, which returns true when the two surrounding operands are equal.



options(repr.plot.width=4, repr.plot.height=4)