~/cotton_fiber/fusion/TWAS_result/FS


--coloc_P
--PANELN


wgtlist = read.table(opt$weights,head=T,as.is=T)

```
WGT	ID	CHR	P0	P1
weights_4DPA/Garb_01G000040.wgt.RDat	Garb_01G000040	1	26653	32316
weights_4DPA/Garb_01G000280.wgt.RDat	Garb_01G000280	1	180533	186895
weights_4DPA/Garb_01G000460.wgt.RDat	Garb_01G000460	1	345710	347608
weights_4DPA/Garb_01G000800.wgt.RDat	Garb_01G000800	1	731695	734582
weights_4DPA/Garb_01G000830.wgt.RDat	Garb_01G000830	1	789436	791215
weights_4DPA/Garb_01G000880.wgt.RDat	Garb_01G000880	1	878352	881703
weights_4DPA/Garb_01G000900.wgt.RDat	Garb_01G000900	1	886434	890081
weights_4DPA/Garb_01G001270.wgt.RDat	Garb_01G001270	1	1258115	1262871
weights_4DPA/Garb_01G001280.wgt.RDat	Garb_01G001280	1	1287785	1289662
```


```
paneln = read.table(opt$PANELN,as.is=T,head=T,sep='\t')

m = match( wgtlist$PANEL , paneln$PANEL )

wgtlist$N = paneln$N[ m ]
```