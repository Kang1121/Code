from torch import optim
from torch.autograd import Variable
from preprocessing import *
from lenet import *

import torch
from torch.autograd import Variable
import os
import random
import linecache
import numpy as np
import torchvision
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms
from PIL import Image
import PIL.ImageOps
import matplotlib.pyplot as plt


'''
net = LeNet().cuda()
criterion = SoftMaxLoss()
optimizer = optim.Adam(net.parameters(), lr=0.0003)
counter = []
loss_history = []
iteration_number = 0

for epoch in range(0, 10):
    for i in range(0, 60000):
        img = torch.tensor(train_images[i][:][:])

        label = torch.tensor(train_labels[i])
        img, label = Variable(img).cuda(), Variable(label).cuda()
        output = net(img)
        optimizer.zero_grad()
        loss_contrastive = criterion(output, label)
        loss_contrastive.backward()
        optimizer.step()

        if i % 1000 == 0:
            print("Epoch:{},  Current loss {}\n".format(epoch, loss_contrastive.item()))
            iteration_number += 10
            counter.append(iteration_number)
            loss_history.append(loss_contrastive.item())
plt.plot(counter, loss_history)
plt.show()
'''


from PIL import Image
import torch


class MyDataset(torch.utils.data.Dataset):  # 创建自己的类：MyDataset,这个类是继承的torch.utils.data.Dataset
    def __init__(self, root, datatxt, transform=None, target_transform=None):  # 初始化一些需要传入的参数
        #print(root)
        super(MyDataset, self).__init__()
        fh = open(root + datatxt, 'r')  # 按照传入的路径和txt文本参数，打开这个文本，并读取内容
        imgs = [] # 创建一个名为img的空列表，一会儿用来装东西
        for line in fh:  # 按行循环txt文本中的内容
            line = line.rstrip() # 删除 本行string 字符串末尾的指定字符，这个方法的详细介绍自己查询python
            words = line.split()  # 通过指定分隔符对字符串进行切片，默认为所有的空字符，包括空格、换行、制表符等
            imgs.append((words[0], int(words[1])))  # 把txt里的内容读入imgs列表保存，具体是words几要看txt内容而定

 # 很显然，根据我刚才截图所示txt的内容，words[0]是图片信息，words[1]是lable
        self.imgs = imgs
        self.transform = transform
        self.target_transform = target_transform


    def __getitem__(self, index):
        # 这个方法是必须要有的，用于按照索引读取每个元素的具体内容
        fn, label = self.imgs[index]  # fn是图片path #fn和label分别获得imgs[index]也即是刚才每行中word[0]和word[1]的信息
        #print(root + fn)

        img = Image.open(fn)  # 按照path读入图片from PIL import Image # 按照路径读取图片

        if self.transform is not None:
            img = self.transform(img)  # 是否进行transform
        return img, label # return很关键，return回哪些内容，那么我们在训练时循环读取每个batch时，就能获得哪些内容

    def __len__(self):  # 这个函数也必须要写，它返回的是数据集的长度，也就是多少张图片，要和loader的长度作区分
        return len(self.imgs)


# 根据自己定义的那个勒MyDataset来创建数据集！注意是数据集！而不是loader迭代器
train_data = MyDataset('./', 'datatrain.txt', transform=transforms.ToTensor())
test_data = MyDataset('./', 'datatest.txt', transform=transforms.ToTensor())

train_loader = DataLoader(dataset=train_data, batch_size=512, shuffle=True)
test_loader = DataLoader(dataset=test_data, batch_size=512)

net = LeNet().cuda()
criterion = SoftMaxLoss()
optimizer = optim.Adam(net.parameters(), lr=0.0003)

counter = []
loss_history = []
iteration_number = 0


for epoch in range(0, 40):
    #print(len(train_dataloader))
    for i, data in enumerate(train_loader, 0):
        img0, label = data
        #print((img0).shape)
        #print((label).shape)
        img0, label = Variable(img0).cuda(), Variable(label).cuda()
        #print(img0.shape)
        output = net(img0)
        optimizer.zero_grad()
        loss_contrastive = criterion(output, label)

        loss_contrastive.backward()
        optimizer.step()

        if i % 100 == 0:
            print("Epoch:{},  Current loss {}\n".format(epoch, loss_contrastive.item()))
            iteration_number = iteration_number + 100
            counter.append(iteration_number)
            loss_history.append(loss_contrastive.item())
plt.plot(counter, loss_history)
plt.show()








