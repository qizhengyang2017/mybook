BioProject submission: SUB10794242
https://submit.ncbi.nlm.nih.gov/subs/bioproject/SUB10794242/target



Public description
Provide a description (a paragraph) of the study goals and relevance.


In order to  study the  regulatory variants that  are responsible for the formation of variable fiber quality, we performed whole genome sequencing of 216 G. arboreum accessions and RNA sequencing of 1,005 fiber samples of these accessions at five developmental stages.


所有一起传，在biosample attributes这一步需要发邮件人工审核
## SRA
SRA




```
cat sample_name_noJ104.txt|while read i;do ln -s /data/cotton/MaojunWang/Raw_Data/DiploidCotton_Resequencing/rawdata/${i}_R1.fq.gz upload/;ln -s /data/cotton/MaojunWang/Raw_Data/DiploidCotton_Resequencing/rawdata/${i}_R2.fq.gz upload/;done
```


      

PRJNA788322

  

Gossypium arboreum 
module load aspera-connect/3.9.9.177872
/public/home/zyqi/ga/raw_data/aspera.openssh



师兄说可以一个时期建一个号

J104上传成功
![[Pasted image 20211213194934.png]]

其他的改完本地上传，计算节点似乎连不上外网
nohup sh upload.sh &> upload_ncbi.log &

