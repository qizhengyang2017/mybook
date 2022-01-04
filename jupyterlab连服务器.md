ssh 设置
j_8890.lsf这个脚本中指定的Ip不发挥作用
重新投递要等一会，看看<< output from stderr >>有没有输出
ssh -p 22333 -N -f -L 8890:c03n07:8890 zyqi@211.69.141.131
ip改成130或者142