# raspi 搭建一个可以随时看离线视频的网站

### 前言

手里的树莓派闲置好长时间了，正好某宝买了50的资源，下了点资源，废物利用一下。

提示：一切以能用为主，不搞那些花里胡哨的。

## 效果展示

- 树莓派连接

<video style="height:400px;width:600px" src="C:\Users\jiujue\Downloads\设备展示.mp4"></video>

- 手机端演示

<video style="height:400px;width:600px" src="C:\Users\jiujue\Downloads\手机端演示.mp4"></video>

- 电脑端演示

  <video style="height:300px;width:500px" src="C:\Users\jiujue\Downloads\电脑端演示.mp4"></video>

## 想法

- 树莓派上搭建个后端程序提供文件浏览服务，将硬盘里的目录给映射出来
- 浏览器访问服务器获取文件列表，后端提供渲染服务
- nginx提供视频文件的托管

## 实现思路

- 采用python django 编写后端，采用前后端不分离的模式
- 树莓派无线网卡配置为热点，树莓派开机启动就会开放一个热点
- nginx 托管视频文件目录



## 具体操作步骤

### 用到的物理材料

- 必须品
  - 树莓派（版本无所谓主要要有无线功能的）
  - 硬盘（放视频文件）
  
- 非必须
  - 网线、免驱无线网卡（方便后续配置树莓派）
  - 屏幕一块（我这款是3.5寸，某宝可以买到，最便宜40左右）

### 程序编写

- 自己随便写的，以实现为主，前端模板用bootstrap实现响应式布局，不同设备访问都能有较好的体验。
- 后端代码就是 django

### raspi zero usb 以太网连接

 参考：[树莓派 Zero USB/以太网方式连接配置教程 | 树莓派实验室 (nxez.com)](https://shumeipai.nxez.com/2018/02/20/raspberry-pi-zero-usb-ethernet-gadget-tutorial.html)

### apt 源更换国内源

参考：https://blog.csdn.net/zifengzwz/article/details/107922635

### 视频浏览网站的编写

- https://github.com/jiujue/raspi_videohome            - github addr
- https://gitee.com/jiujueismmp/raspi_videohome  -  gitee addr

### raspi 无线热点配置

参考：[从零开始：树莓派共享 WiFi 秒变无线热点（树莓派路由器 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/102598741)

### 树莓派程序开机自启动方法总结

参考：[(3条消息) 树莓派程序开机自启动方法总结_老野的成长之路-CSDN博客_树莓派开机自启](https://blog.csdn.net/feixuedongji/article/details/79891735?utm_medium=distribute.wap_relevant.none-task-blog-2~default~BlogCommendFromMachineLearnPai2~default-1.wap_blog_relevant_pic&depth_1-utm_source=distribute.wap_relevant.none-task-blog-2~default~BlogCommendFromMachineLearnPai2~default-1.wap_blog_relevant_pic)

### nginx 静态文件服务配置

参考： [树莓派3B+搭建Nginx流媒体服务器 - 夏天雨后的吉他有点风 - 博客园 (cnblogs.com)](https://www.cnblogs.com/qiantuo1234/p/6611845.html)



### webmin安装配置 *可选项

参考：[ 用 webmin 在线管理树莓派系统 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/107091773)

### 时间同步 *可选项

参考：[树莓派系统时间同步 - HH番茄 - 博客园 (cnblogs.com)](https://www.cnblogs.com/imfanqi/p/4396292.html)

### linux 命令行链接wifi  *可选项

参考[linux下如何使用命令连接wifi_小马的博客-CSDN博客_linux连接wifi](https://blog.csdn.net/xiao_jj_jj/article/details/84322593)

