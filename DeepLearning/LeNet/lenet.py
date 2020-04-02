import torch.nn as nn
import torch


class LeNet(nn.Module):
    def __init__(self):
        super(LeNet, self).__init__()
        self.cnn1 = nn.Sequential(
            nn.Conv2d(in_channels=1, out_channels=6, kernel_size=5, padding=3),
            nn.ReLU(inplace=False),

            nn.AvgPool2d(kernel_size=2),
            nn.ReLU(inplace=False),

            nn.Conv2d(in_channels=6, out_channels=16, kernel_size=5),
            nn.ReLU(inplace=False),

            nn.AvgPool2d(kernel_size=2),
            nn.ReLU(inplace=False),

            nn.Conv2d(in_channels=16, out_channels=120, kernel_size=5),
            nn.ReLU(inplace=False),
        )

        self.fc1 = nn.Sequential(
            nn.Linear(120, 84),
            nn.ReLU(inplace=False),
            nn.Linear(84, 10),
            nn.ReLU(inplace=False)
        )

    def exp1(self, output):

        output = torch.exp(output)
        output_exp = torch.sum(output, 1)
        output_exp = output_exp.reshape(output_exp.shape[0], 1)
        #print(output_exp.shape)
        #print(output.shape)

        output = output / output_exp

        return output

    def forward(self, x):
        output = self.cnn1(x)
        #print(output)
        output = output.view(output.size()[0], -1)
        #print(output.shape)
        output = self.fc1(output)
        #print(output)
        output = self.exp1(output)

        return output


class SoftMaxLoss(nn.Module):
    def __init__(self, margin = 2.0):
        super(SoftMaxLoss, self).__init__()
        self.margin = margin

    def forward(self, output, label):
        #print(output.shape)
        #print(label.shape)
        ''' torch.autograd.set_detect_anomaly(True)
        a = output
        for i in range(0, 32):
            for j in range(0, 10):
                a[i][j] = torch.exp(output[i][j])
        output_exp = torch.sum(output, 1)
        #print(output_exp.shape)
        #print(type(output_exp))
        for i in range(0, 64):
            for j in range(0, 10):
                #print(type(output[i][j]))
                a[i][j] = output[i][j] / output_exp[i]

'''
        #print(type(output))
        s = 0
        for i in range(0, output.shape[0]):
            #print(label[i].cpu().numpy())
            if torch.log(output[i][label[i].cpu().numpy()]) != 0.0000:
                s = s - (torch.log(output[i][label[i].cpu().numpy()]))
            else:
                s = s - torch.log(torch.tensor(0.000001).cuda())
        loss = s / output.shape[0]
        #print(type(loss))
        #print(loss)
        return loss


