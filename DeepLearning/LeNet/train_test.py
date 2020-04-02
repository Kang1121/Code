import torch
from main import *

sum1 = 0
sum0 = 0

for epoch in range(0, 40):
    #print(len(train_dataloader))
    for i, data in enumerate(train_loader, 0):
        img0, label = data

        img0, label = Variable(img0).cuda(), Variable(label).cuda()

        output = net(img0)
        k = output.size()
        # print(k[0])
        # print(k[1])
        for j in range(0, k[0]):
            t = torch.max(output, 1)[0].data.cpu().numpy()
            # sss = t.size()
            # print(sss[0])
            # print(sss[1])


            #print(t)

            sum0 = sum0 + 1
            if (output[j][label[j]]) == t[j]:
                sum1 = sum1 +1


print("train accuracy", sum1 / sum0)


sum1 = 0
sum0 = 0

for epoch in range(0, 40):
    #print(len(train_dataloader))
    for i, data in enumerate(test_loader, 0):
        img0, label = data

        img0, label = Variable(img0).cuda(), Variable(label).cuda()

        output = net(img0)
        k = output.size()
        # print(k[0])
        # print(k[1])
        for j in range(0, k[0]):
            t = torch.max(output, 1)[0].data.cpu().numpy()
            # sss = t.size()
            # print(sss[0])
            # print(sss[1])


            #print(t)

            sum0 = sum0 + 1
            if (output[j][label[j]]) == t[j]:
                sum1 = sum1 +1


print("test accuracy", sum1 / sum0)


