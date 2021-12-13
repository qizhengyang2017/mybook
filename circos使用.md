## 2021年10月17日
如何快速上手circos:
注意几个配置文件
先配置象形
~/work/ga/hotspot_all/hotspot_result_new

---
## 2021年07月16日
如何使A01和D13左右对齐?

染色体间距是0.005r
0.05*360/2=9
-90+9=-81

但是这个间距不对，不知道原因。差不多就行了吧。微调到-82.3，大概距离中心线150像素。

[spacing breaks](http://circos.ca/documentation/tutorials/ideograms/variable_radius/)


Circos doesn't yet draw color legends. You can get a list of the color encoding by using `-debug_group legend`. (http://circos.ca/documentation/tutorials/2d_tracks/heat_maps/)

`circos -conf ... -debug_group legend`



我不知道怎么搞。但是我有颜色值。怎么生成热图的图例呢？
svg画热图图例

可以自己画
```xml
<svg width='120' height='40'>
<rect x='10' y='5' width='30' height='30' style='fill:#7a65d4'/>
<rect x='40' y='5' width='30' height='30' style='fill:#e74815'/>
<rect x='70' y='5' width='30' height='30' style='fill:#1c7bf3'/>
</svg>
```
如果用rgb，`<rect width="300" height="100" style="fill:rgb(0,0,255);stroke-width:3;stroke:rgb(0,0,0)" />`

参考(https://mp.weixin.qq.com/s/4G0R1tSK6UvxowM6YTxorw)

circos颜色(http://www.circos.ca/documentation/tutorials/2d_tracks/heat_maps/)
