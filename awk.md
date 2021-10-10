 

**关联数组**跟数字数组不同之处在于它的索引值可以是任意文本字符串。你不需要用连续的数 字来标识数组中的数据元素。相反，关联数组用各种字符串来引用值。每个索引字符串都必须能 够唯一地标识出赋给它的数据元素。如果你熟悉其他编程语言的话，就知道这跟**散列表**和**字典**是同一个概念。[@2016]


cat test.txt | awk '{map[$2]++} END { for (a in map )print map[ a ]" " map[ a ]/NR*100 "% " a }'


```
aaa
bbb
aaa
bbb
ccc
bbb
```

输出

```
2 33.3333% aaa
1 16.6667% ccc
3 50% bbb
```

cat test.txt|awk '!x[$0]++'


awk 的基本执行流程是，对文件的每一行，做一个指定的逻辑判断，如果逻辑判断成立，则执行指定的命令；如果逻辑判断不成立，则直接跳过这一行。这里写的 awk 命令是!x[$0]++，意思是，首先创建一个 map 叫x，然后用当前行的全文$0作为 map 的 key，到 map 中查找相应的 value，如果没找到，则整个表达式的值为真，可以执行之后的语句；如果找到了，则表达式的值为假，跳过这一行。由于表达式之后有++，因此如果某个 key 找不到对应的 value，该++操作会先把对应的 value 设成 0，然后再自增成 1，这样下次再遇到重复的行的时候，对应的 key 就能找到一个非 0 的 value 了。


```
cat test.txt|awk '{x[$0]++}END{for(k in x){print k"\t"x[k]}}'
```


(mashr) 21:26 zyqi@login02:/data/cotton/zyqi/Ga_data/nominal
$cat run2.sh

```
for i in 4DPA 8DPA 12DPA 16DPA 20DPA
do
awk 'NR==FNR{a[$4]=$2;b[$4]=$1;if ($6=="+") c[$4]=$2; else c[$4]=$3;next}{p=a[$2]+$4+1;$3=b[$2]"_"p;$4=p-c[$2];print $2,$3,$4,$5,$6,$7,$8,$9,$10}' OFS='\t' change.Chr_genome_final_gene_1based.bed ${i}_fastQTL_nominal_AllChrs.txt > ${i}_nominal_addID_TSSdistance.txt

md5sum ${i}_nominal_addID_TSSdistance.txt > ${i}_nominal_addID_TSSdistance.txt.md
done
```


