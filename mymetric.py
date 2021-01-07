# coding=utf-8
import numpy as np
from sklearn import metrics
y_true=np.array([1.1,3.3,5.5,7.7])
y_pred=np.array([1.0,3.0,5.0,7.0])

# MSE
def MSE(true, pred):
    return np.sum((true - pred)**2)
mse=metrics.mean_squared_error(y_true,y_pred)
# RMSE
rmse=np.sqrt(mse)
# MAE
def mae(true, pred):
    return np.sum(np.abs(true - pred))
mae=metrics.mean_absolute_error(y_true,y_pred)
# MAPE
mape=np.mean(np.abs(y_pred-y_true)/y_true)*100
#SMPAE
smape=np.mean(2*np.abs(y_pred-y_true)/(np.abs(y_pred)+np.abs(y_true)))*100
# R Squared
RS=metrics.r2_score(y_true,y_pred)
# huber loss
def huber(true, pred, delta):
    loss = np.where(np.abs(true-pred) < delta , 0.5*((true-pred)**2), delta*np.abs(true - pred) - 0.5*(delta**2))
    return np.sum(loss)

y_trues = [1,1,1,1,0,0,1,1,1,0,0]
y_preds = [1,1,1,0,1,1,0,1,1,1,0] 

# ACC准确率
acc=metrics.accuracy_score(y_trues,y_preds)
# Precision精准率
P=metrics.precision_score(y_trues,y_preds)
# Recall召回率
R=metrics.recall_score(y_trues,y_preds)
# F
F=metrics.fbeta_score(y_trues,y_preds,beta=1)