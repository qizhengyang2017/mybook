jupyter kernelspec list
- [ ] 怎么添加其他环境中的内核？

---
==jupyterlab的配置文件是不是更改了==

~/.jupyter/jupyter_notebook_config.py

我的配置文件的时间是 Jan  8  2021

![[Pasted image 20210828214615.png]]


```
<< output from stdout >>
2021/08/28 21:45:02 [W] [service.go:102] login to server failed: dial tcp 211.69.141.138:8899: connect: no route to host
dial tcp 211.69.141.138:8899: connect: no route to host

<< output from stderr >>
[I 2021-08-28 21:45:00.796 ServerApp] jupyterlab | extension was successfully linked.
[W 2021-08-28 21:45:00.805 NotebookApp] 'allow_remote_access' has moved from NotebookApp to ServerApp. This config will be passed to ServerApp. Be sure to update your config before our next release.
[W 2021-08-28 21:45:00.805 NotebookApp] 'password' has moved from NotebookApp to ServerApp. This config will be passed to ServerApp. Be sure to update your config before our next release.
[I 2021-08-28 21:45:01.298 ServerApp] nbclassic | extension was successfully linked.
[I 2021-08-28 21:45:01.417 ServerApp] nbclassic | extension was successfully loaded.
[I 2021-08-28 21:45:01.420 LabApp] JupyterLab extension loaded from /public/home/zyqi/anaconda3/envs/new1/lib/python3.9/site-packages/jupyterlab
[I 2021-08-28 21:45:01.420 LabApp] JupyterLab application directory is /public/home/zyqi/anaconda3/envs/new1/share/jupyter/lab
[I 2021-08-28 21:45:01.429 ServerApp] jupyterlab | extension was successfully loaded.
[I 2021-08-28 21:45:01.430 ServerApp] Serving notebooks from local directory: /public/home/zyqi
[I 2021-08-28 21:45:01.430 ServerApp] Jupyter Server 1.9.0 is running at:
[I 2021-08-28 21:45:01.430 ServerApp] http://localhost:8888/lab
[I 2021-08-28 21:45:01.431 ServerApp]  or http://127.0.0.1:8888/lab
[I 2021-08-28 21:45:01.431 ServerApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[W 2021-08-28 21:45:01.457 ServerApp] No web browser found: could not locate runnable browser
```