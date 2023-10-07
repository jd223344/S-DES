# TiMi小组1-5关测试结果

成员：戴静、陈晓阳

## **第1关：基本测试**

本小组GUI主界面如下：



![image1](https://github.com/jd223344/S-DES/assets/145902946/75014e5b-c07b-46e3-b807-ae3fa3d99a02)
![image2](https://github.com/jd223344/S-DES/assets/145902946/aadeea5b-504f-40d2-93de-951ca7de69ab)

输入部分：加密选项卡输入10-bit的密钥、8-bit的明文（ASCII编码明文详见第3关）；

解密选项卡输入加密选项卡输入10-bit的密钥、8-bit的密文（和ASCII编码密文）。

输入错误结果展示：如果输入非10-bit的密钥或非8-bit的明\\密文，将会弹出错误弹窗提示。

![image3](https://github.com/jd223344/S-DES/assets/145902946/f63067f2-2a68-4c7f-82fa-1e3a7b9ae0d3)


![image4](https://github.com/jd223344/S-DES/assets/145902946/81b33997-d2fc-4c3b-b9c2-070656b9ca0e)


输出结果：加密选项卡输入密钥和明文后点击加密，文本框显示加密后的密文；解密选项卡输入密钥和密文后点击解密，文本框显示解密后的明文。

![image5](https://github.com/jd223344/S-DES/assets/145902946/904430c5-d076-4dc3-a51e-a2d0152d67fe)


![image6](https://github.com/jd223344/S-DES/assets/145902946/b1664262-9d05-4714-a2ca-0d791dd34382)


由上两图可见，加密前的明文和解密后的明文保持一致，说明加解密过程无误。第1关测试完成。

## **第2关：交叉测试**

本小组采用"不同小组使用相同的明文P和密钥K进行加密得到相同的密文C"的要求进行测试，并与窦一冉组、鲁梦瑶组、唐豪组进行交叉测试。

测试明文：10011010

测试密钥：1010000010

本组结果：

![image7](https://github.com/jd223344/S-DES/assets/145902946/acfbf760-2391-4b1d-87f9-441586b48db5)


窦一冉组结果：

![image8](https://github.com/jd223344/S-DES/assets/145902946/08776328-618e-4b6d-8335-d2c545be5800)


鲁梦瑶组结果：

![image9](https://github.com/jd223344/S-DES/assets/145902946/ed44bc9a-3975-408b-87de-33b15128d40e)


唐豪组结果：

![image10](https://github.com/jd223344/S-DES/assets/145902946/05dd5f3e-f5c8-4be1-991c-e1714dd3b2d5)


由上面四组加密结果截图可见，密文均为11101111，符合交叉测试的通过要求。第2关测试完成。

## **第3关：扩展功能**

考虑到向实用性扩展，加密算法的数据输入可以是ASII编码字符串(分组为1
Byte)，对应地输出也可以是ASCII字符串(很可能是乱码)。本组成功实现了该扩展功能，具体方法如下：将ASCII字符串转化为二进制字符串，并以1
Byte为一组对该二进制字符串进行循环加密，得到加密后的二进制字符串密文。随后将二进制字符串密文重新转化为ASCII字符串输出。解密同理。

输入部分：加密选项卡输入10-bit的密钥和ASCII编码明文；

解密选项卡输入加密选项卡输入10-bit的密钥和ASCII编码密文。

输出结果：加密选项卡输入密钥和ASCII明文后点击加密，文本框显示加密后的ASCII密文；解密选项卡输入密钥和ASCII密文后点击解密，文本框显示解密后的ASCII明文。

![image11](https://github.com/jd223344/S-DES/assets/145902946/5c9b2f3b-fc47-4dce-a292-eb27fcf11cf4)
![image12](https://github.com/jd223344/S-DES/assets/145902946/11a0fe41-d983-4055-b82f-7c79c30218cf)


由上两图可见，加密前的明文和解密后的明文保持一致，说明加解密过程无误。第3关测试完成。

**综合第1关和第3关，本组的GUI实现了普通8-bit二进制字符串和ASCII编码字符串的同时加\\解密，并可以同时显示加\\解密结果。效果如下：**

![image13](https://github.com/jd223344/S-DES/assets/145902946/3a0d417d-fed9-45b8-b099-cbf3899e2294)

![image14](https://github.com/jd223344/S-DES/assets/145902946/d87df8f0-8d8e-4700-ba43-5ca31a1bd8e8)


## **第4关：暴力破解**

本组编写了暴力破解程序，该程序会对一对或多对明密文对进行暴力破解，并统计每对明密文破解的时间，最后计算平均值。暴力破解的过程中，每一条破解过程中的密钥和密文都会被打印；在找到正确的密钥时会进一步打印尝试次数和破解时间。

下两张静态图展示了程序对3对使用相同密钥的明、密文对进行暴力破解输入完成的情形和破解完成后的结果。

![image15](https://github.com/jd223344/S-DES/assets/145902946/24bf7c8c-ed79-4cfe-a525-2fc435617e82)


![image16](https://github.com/jd223344/S-DES/assets/145902946/92746e94-d3c8-4c52-8182-e100f9901158)


完整破解视频见Github链接：[[https://github.com/jd223344/S-DES]{.underline}](https://github.com/jd223344/S-DES)

第4关测试完成。

## **第5关：封闭测试**

根据第4关的结果，我们发现三对使用相同密钥1001000110的明密文对，在暴力破解时可能找到不同的密钥（如第二对明密文对找到的密钥）。因此，本组编写了相似的新暴力破解程序：对于一组明密文对通过暴力破解的方法找出所有可能的密钥Key。

我们对第二组明密文对重新进行了暴力破解，结果如下：

![image17](https://github.com/jd223344/S-DES/assets/145902946/21ac3377-5d1e-4a20-955f-6f962fdc4f4f)


对于该密文对，我们找到了4个可能的密钥，且密钥3就是关卡4中3对明密文对原来使用的密钥。

综合第4关和第5关分析可知，对于随机选择的一个明密文对，可能存在一个或多个密钥Key。进一步扩展，对应明文空间任意给定的明文分组[Pn](#)，有可能会出现选择不同的密钥[Ki≠Kj](#)加密得到相同密文[Cn](#)的情况：只要这些密钥产生的子密钥k1和k2相同，就可以加密得到相同的密文。

第5关测试完成。



# TiMi小组关于S-DES加解密项目开发手册

## 1.  概述

本项目可通过GUI界面实现对二进制、ASCII编码的数据进行加/解密，同时还可通过暴力破解获得多对明密文对相应的密钥以及一对明密文对可能存在的多个密钥。

## 2.  GUI界面

### 2.1 相关代码

GUI界面相关代码可参考代码项目中GUI.py相关文件。

### 2.2 具体界面及操作解释

用户可以通过运行GUI.py文件可得：

<img width="302" alt="image18" src="https://github.com/jd223344/S-DES/assets/145902946/bcd23280-d75e-4a5c-aa0a-c2955b0e1a0b">


用户输入密钥以及明/密文，可进行加/解密：

<img width="298" alt="image19" src="https://github.com/jd223344/S-DES/assets/145902946/25557fda-2d40-46ad-bc48-f8c3d96dd834">


<img width="300" alt="image20" src="https://github.com/jd223344/S-DES/assets/145902946/64a10cea-aa95-4819-aa52-69576c6d97bd">


若输入密钥或者明文的长度、格式不对（比如密钥长度不为10，二进制明文长度不为8，或者格式不为二进制），会有相关提醒：

<img width="299" alt="image21" src="https://github.com/jd223344/S-DES/assets/145902946/cc462747-3d4c-4316-a00f-6153f463830c">


<img width="301" alt="image22" src="https://github.com/jd223344/S-DES/assets/145902946/32d79414-34cc-410f-8f99-f41694b6f36b">


<img width="303" alt="image23" src="https://github.com/jd223344/S-DES/assets/145902946/f66d90d4-c8e8-423d-9434-d29a12771373">


<img width="302" alt="image24" src="https://github.com/jd223344/S-DES/assets/145902946/971e1aa6-353d-4e9a-9a35-130fa887d55a">


暴力破解：

<img width="412" alt="image25" src="https://github.com/jd223344/S-DES/assets/145902946/89bebc72-df44-44b0-89b4-f2e4d58dc50f">


<img width="469" alt="image26" src="https://github.com/jd223344/S-DES/assets/145902946/a0368473-31f1-4d39-9151-38e98ac19e68">


<img width="496" alt="image27" src="https://github.com/jd223344/S-DES/assets/145902946/7320ddf6-8f88-4506-a34b-6002b866df46">


## 3.  项目代码部分相关介绍

<img width="158" alt="image28" src="https://github.com/jd223344/S-DES/assets/145902946/c16c1689-fb73-45a4-80d1-4bf3f29e5306">


其中GUI.py主要关于界面的设计；Function.py主要设计EP-Box，S-Box，SP-Box，IP，IP的逆，轮函数的设计；Key.py主要设计了提取子密钥；Encryption.py主要完成加密过程；Decryption.py主要完成解密过程；ASCII.py完成了对于ASCII编码的加/解密；BF.py完成了

多对明密文的密钥破解；BF2.py完成了破解一对明密文可能存在的多个不同密钥。

可运行文件为：GUI.py；BF.py；BF2.py

## 4.  项目背景介绍

S-DES算法加/解密原理流程图如下：

![image29](https://github.com/jd223344/S-DES/assets/145902946/dd2ce508-6268-404a-b487-bf11aa62fb04)


轮函数原理流程如下：

![image30](https://github.com/jd223344/S-DES/assets/145902946/3b0325d8-5741-401c-9e6a-451e727d71e7)


## 5.  使用步骤

●运行GUI.py文件

●可选择"加密"或者"解密"选项

●输入相应的密钥，二进制明/密文（可选），ASCII编码的明/密文（可选），选择加/解密

●若进行暴力破解，可运行BF.py文件或者时BF2.py文件

## 6.  其他帮助

TiMi小组是一个优秀、热情负责的团队。若您在使用过程中出现任何困惑不解，<可发送邮件至891073279@qq.com>或者3416924346@qq.com。
