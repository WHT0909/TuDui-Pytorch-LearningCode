# P5-Pytorch 加载数据初认识

## 1. Dataset 类

目的：提供一种方式去获取数据及其 label

包含的功能：
- 如何获取每一个数据及其 label
- 告诉我们一共有多少数据

Dataset 可以拼接：
```
dataset1 = MyDataset(root_dir="path1")
dataset2 = MyDataset(root_dir="path2")
dataset = dataset1 + dataset2
```