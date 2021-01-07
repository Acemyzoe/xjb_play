#!/usr/bin/env python
# -*- coding: utf8 -*-
# y_true: list, the true labels of input instances 
# y_pred: list, the probability when the predicted label of input instances equals to 1
import numpy as np
from sklearn.metrics import log_loss

def logloss(y_true, y_pred, eps=1e-15):

    # Prepare numpy array data
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    assert (len(y_true) and len(y_true) == len(y_pred))

    # Clip y_pred between eps and 1-eps
    p = np.clip(y_pred, eps, 1-eps)
    loss = np.sum(- y_true * np.log(p) - (1 - y_true) * np.log(1-p))

    return loss / len(y_true)

def cross_entropy(y_true, y_pred):
    """Cross-Entropy loss function.
    以向量化的方式实现交叉熵函数
    """
    y_true = np.float_(y_true)
    y_pred = np.float_(y_pred)
    return -np.sum(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred)) / len(y_true)

def unitest():
    y_true = [0, 0, 1, 1]
    y_pred = [0.1, 0.2, 0.7, 0.99]

    print("Use self-defined logloss() in binary classification, the result is {}".format(logloss(y_true, y_pred)))
    print("Use log_loss() in scikit-learn, the result is {} ".format(log_loss(y_true, y_pred)))
    print(cross_entropy(y_true,y_pred))
if __name__ == '__main__':
    unitest()