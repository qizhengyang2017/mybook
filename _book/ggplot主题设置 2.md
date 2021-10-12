```R
plotAnnoBar(peakAnnoList) + theme(panel.grid.major = element_blank()) + scale_y_continuous(expand = c(0,0))+ 
theme(panel.border = element_rect(fill=NA,color="black", size=1.5, linetype="solid"),
      axis.ticks =element_line(color='black',size=1.5),
      axis.text = element_text(size=16,color = 'black'),
      axis.title=element_text(size=16,face="plain",color="black"),
      plot.title = element_text(size=16,colour = "black", color = "black"),
      legend.title=element_text(size=16,face="plain",color="black"),
      legend.text =element_text(size=14),
      legend.key.size=unit(0.2,'in')
     )
```