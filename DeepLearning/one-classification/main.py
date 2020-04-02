from model import *
from data_preprocessing import *
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc

np.random.seed(1)

train_x, train_y, test_x, test_y, classes = data_preprocessing()

layers_dims = [12288, 20, 7, 5, 1]

parameters = model(train_x, train_y, layers_dims, lamd=0.7, num_iterations=2000)

pred_train, p = predict(train_x, train_y, parameters)
pred_test, p = predict(test_x, test_y, parameters)



y_test = test_y.flatten()
y_score = pred_test.flatten()

fpr, tpr, threshold = roc_curve(y_test, y_score)
roc_auc = auc(fpr, tpr)

plt.figure()
lw = 2
plt.figure(figsize=(10, 10))
plt.plot(fpr, tpr, color='darkorange',
         lw=lw, label='ROC curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic example')
plt.legend(loc="lower right")
plt.show()


p = p.flatten()
for i in range(1, 50):
    if y_test[i] != p[i]:
        plt.imshow(test_x[:,i].reshape(64, 64, 3))
        plt.show()
