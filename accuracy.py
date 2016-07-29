import numpy as np
from sklearn.metrics import accuracy_score

y = open("a.txt", "r")
y_pred = y.read().split(',')

x = open ("b.txt", 'r')
x_true=  x.read().split(',')


f=accuracy_score(x_true, y_pred)
print f
