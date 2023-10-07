# S-DES
# TiMi小组关于S-DES加解密项目开发手册

1. **概述**

本项目可通过GUI界面实现对二进制、ASCII编码的数据进行加/解密，同时还可通过暴力破解获得多对明密文对相应的密钥以及一对明密文对可能存在的多个密钥。

1. **GUI**** 界面**

**2.1**  **相关代码**

GUI界面相关代码可参考代码项目中GUI.py相关文件。

**2.2**  **具体界面及操作解释**

用户可以通过运行GUI.py文件可得：

![](RackMultipart20231007-1-6w2w71_html_6b7a71a33eb7d852.png)

用户输入密钥以及明/密文，可进行加/解密：

![](RackMultipart20231007-1-6w2w71_html_1542e6d42a76274e.png)

![](RackMultipart20231007-1-6w2w71_html_866c0386e009e942.png)

若输入密钥或者明文的长度、格式不对（比如密钥长度不为10，二进制明文长度不为8，或者格式不为二进制），会有相关提醒：

![](RackMultipart20231007-1-6w2w71_html_3a528ec331f8d3c5.png)

![](RackMultipart20231007-1-6w2w71_html_21956e8971f983e7.png)

![](RackMultipart20231007-1-6w2w71_html_954e327a215fddef.png)

![](RackMultipart20231007-1-6w2w71_html_ccfa73131e399fe5.png)

暴力破解：

![](RackMultipart20231007-1-6w2w71_html_dd637cebba81b08e.png)

![](RackMultipart20231007-1-6w2w71_html_7e39adf42d7d0262.png)

![](RackMultipart20231007-1-6w2w71_html_5444129cca4fc6d7.png)

1. **项目代码部分相关介绍**

![](RackMultipart20231007-1-6w2w71_html_91769638933fe013.png)

其中GUI.py主要关于界面的设计；Function.py主要设计EP-Box，S-Box，SP-Box，IP，IP的逆，轮函数的设计；Key.py主要设计了提取子密钥；Encryption.py主要完成加密过程；Decryption.py主要完成解密过程；ASCII.py完成了对于ASCII编码的加/解密；BF.py完成了

多对明密文的密钥破解；BF2.py完成了破解一对明密文可能存在的多个不同密钥。

可运行文件为：GUI.py；BF.py；BF2.py

1. **项目背景介绍**

S-DES算法加/解密原理流程图如下：

![](RackMultipart20231007-1-6w2w71_html_6bec324f3747f0c6.jpg)

轮函数原理流程如下：

![](RackMultipart20231007-1-6w2w71_html_cdc339ecbc6dc975.jpg)

1. **使用步骤**

●运行GUI.py文件

●可选择"加密"或者"解密"选项

●输入相应的密钥，二进制明/密文（可选），ASCII编码的明/密文（可选），选择加/解密

●若进行暴力破解，可运行BF.py文件或者时BF2.py文件

1. **其他帮助**

TiMi小组是一个优秀、热情负责的团队。若您在使用过程中出现任何困惑不解，[可发送邮件至](mailto:%E5%8F%AF%E5%8F%91%E9%80%81%E9%82%AE%E4%BB%B6%E8%87%B3891073279@qq.com)[891073279@qq.com](mailto:%E5%8F%AF%E5%8F%91%E9%80%81%E9%82%AE%E4%BB%B6%E8%87%B3891073279@qq.com)或者3416924346@qq.com。
