#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Date    : 2018-10-06 14:45:27
# @Author  : zhaoqun.czq

import string
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from dataLoader import loadData

n = 2

def pca(data):
  pca = PCA(n_components=n)
  newData = pca.fit_transform(data)
  print(pca.components_)  
  #print(pca.explained_variance_ratio_)  
  return newData

def plot(label, data):
  colorMap = {u"中锋":"r",u"影锋":"r",u"右边锋":"m",u"左边锋":"m",
    u"左边卫":"b",u"右边卫":"b",u"前腰":"b",u"后腰":"c",u"中场":"g",
    u"左后卫":"y",u"右后卫":"y",u"门将":"k",u"中后卫":"k"}
  color = []
  for l in label:
    color.append(colorMap[l])
  fig = plt.figure()
  if 3 == n:
    ax = Axes3D(fig)
    ax.scatter(data[:, 0], data[:, 1], data[:, 2], color = color, alpha=0.5)
  elif 2 == n:
    ax = fig.add_subplot(111)
    ax.scatter(data[:, 0], data[:, 1], color = color, alpha=0.5)
  else:
    print "INVALID n"
  plt.savefig('./player_norm.png')
  #plt.show()

def findPoint(rawData, newData, xRange, yRange):
  for i in range(0, len(rawData)):
    if newData[i][0] >= xRange[0] and \
      newData[i][0] <= xRange[1] and \
      newData[i][1] >= yRange[0] and \
      newData[i][1] <= yRange[1]:
      print("%s %s %4.2f %4.2f" %(rawData[i][0], rawData[i][1], newData[i][0], newData[i][1]))

def normalize(data):
  rowMax = np.max(data, axis = 1)
  rowMaxT = np.reshape(rowMax, (len(rowMax), 1))
  normData = data / rowMaxT
  assert(data.shape == normData.shape)
  return normData

if __name__ == '__main__':
  # name, position, standard_position, attributes...
  attributes, abilities = loadData()
  label = attributes[:, 1]
  data = abilities
  data = normalize(data)
  newData = pca(data)
  #plot(label, newData)

  findPoint(attributes, newData, [0.2, 0.3], [0.1, 0.2])
