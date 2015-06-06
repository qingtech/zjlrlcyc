#! /usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn.linear_model as lm
import sklearn.datasets as ds

def multivar_linear_regression():
    clf = lm.LinearRegression()
    x = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5]]
    #x = np.array([[1], [2], [3], [4], [5]])
    y = np.array([4.83, 4.27, 3.59, 3.53, 3.46])
    print 'x:', len(x)
    print 'y:', len(y)
    clf.fit(x, y)
    for xx, yy in zip(x, y):
        print yy, clf.predict(xx)
    print 'x=[6, 6, 6], y =', clf.predict([6, 6, 6])
    return
    plt.scatter(x, y, color='blue')
    plt.plot(x, clf.predict(x), color='red', linewidth=4)
    plt.xticks(())
    plt.yticks(())
    plt.show()


if __name__ == '__main__':
    multivar_linear_regression()
