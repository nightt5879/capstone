
简体中文 | [English](README_EN.md)

- [capstone设计作业](#capstone设计作业)
  - [1. 项目介绍](#1-项目介绍)
    - [1.1 项目概括](#11-项目概括)
    - [1.2 使用硬件](#12-使用硬件)
    - [1.3 硬件接线](#13-硬件接线)
  - [2. 代码使用](#2-代码使用)
    - [2.1 使用前准备](#21-使用前准备)
    - [2.2 使用方法](#22-使用方法)
    - [2.3 保存的execl表格](#23-保存的execl表格)
  - [3. 注意事项](#3-注意事项)

# capstone设计作业
## 1. 项目介绍
### 1.1 项目概括
本项目是从地磅远距离通信读取重量数据，可以实现 **按键选择** 将当前的数据记录为 **皮重、毛重** 并自动计算出净重，这三项数据均可以保存至execl表格中于程序自动结束后自动生成. 
### 1.2 使用硬件
使用的地磅为 [xk3190](xk3190.pdf)
<br>远程通信模块为 [E32-DTU](E32-DTU(433L30)-V8_UserManual_CN_v1.0.pdf)（使用了上面的RS485 DB9通信）
<br>USB转E型（9脚）DB9标准接口

### 1.3 硬件接线
电脑端：使用USB转E型（9脚）DB9标准接口，插入USB接口，波特率9600，直接接收字节字符串（byte string）数据
<br>xk3190端：将15芯的+IN，+OUT**短接**接入通信模块的RS485 A端，-IN,-OUT**短接**接入通信模块的RS48 B端。最后将GND相连使模块与地磅共地。

## 2. 代码使用
### 2.1 使用前准备
在连线完成后请修改代码行的端口号，如下所示（65行）：
```python
ser = serial.Serial("COM10", 9600)  # 打开COM10，将波特率配置为115200，其余参数使用默认值
```
将其中的COM10修改成本电脑的端口号，如COM1，COM2等。
### 2.2 使用方法
在修改完端口号后，直接运行代码。在输出区会打印数据格式如下：
```python
目前重量，皮重，毛重，净重
```
此时根据需求进行按键操作，按键操作如下所示
```python
a-将当前重量保存为皮重
b-将当前重量保存为毛重
s-将当前重量数据保存至execl表格中
Esc-退出程序
```
### 2.3 保存的execl表格
excel命名为**2023-05-26_22_34_02_数据记录.xlsx**
<br>其中2023-05-26_22_34_02为程序运行时的时间（年月日，小时分钟秒钟），数据记录为固定的字符串。
<br>表格自动保存在同级目录下

## 3. 注意事项
本代码为一个简单课程设计的作业，代码质量不高，仅供参考。
<br>如有疑问欢迎通过邮件或者b站私信联系我
<br>邮箱：
<br>1469259223@qq.com
<br>scnuyyj@gmail.com
<br>bilibili:
<BR>[这里是啊J](https://space.bilibili.com/23620249?spm_id_from=333.1007.0.0)