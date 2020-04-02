from functions import *
import matplotlib.pyplot as plt


def data_preprocessing():
    train_x_orig, train_y, test_x_orig, test_y, classes = load_data()

    m_train = train_x_orig.shape[0]
    num_px = train_x_orig.shape[1]
    m_test = test_x_orig.shape[0]

    #print("Number of training examples: " + str(m_train))
    # print("Number of testing examples: " + str(m_test))
    #print("Each image is of size: (" + str(num_px) + ", " + str(num_px) + ", 3)")
    #print("train_x_orig shape: " + str(train_x_orig.shape))
    #print("train_y shape: " + str(train_y.shape))
    #print("test_x_orig shape: " + str(test_x_orig.shape))
    #print("test_y shape: " + str(test_y.shape))

    train_x_flatten = train_x_orig.reshape(train_x_orig.shape[0],-1).T
    test_x_flatten = test_x_orig.reshape(test_x_orig.shape[0], -1).T

    train_x = train_x_flatten / 255.
    test_x = test_x_flatten / 255.

   # print("train_x's shape: " + str(train_x.shape))
   # print("test_x's shape: " + str(test_x.shape))
    return train_x, train_y, test_x, test_y, classes
