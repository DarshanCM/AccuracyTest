import numpy as np
from sklearn.metrics import accuracy_score

y = open("test.txt", "r")
y_pred = y.read().split(',')

x = open ("foraccuracy.txt", 'r')
x_true=  x.read().split(',')


f=accuracy_score(x_true, y_pred)
print f
