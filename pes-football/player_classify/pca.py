#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Date    : 2018-10-06 14:45:27
# @Author  : zhaoqun.czq
# Use PCA to reduce dimensions of players' ability vectors to 2 or 3
# Each player is plotted as a point on 2D or 3D canvas
# The color of the point represents the player's position, such as Forward and Goalkeeper.

import string
import numpy as np
import warnings
warnings.filterwarnings('ignore')

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from dataLoader import loadData
from utils import vectorDistance, normalize, pca


def plot(label, data, dim):
  colorMap = {u"中锋":"r",u"影锋":"r",u"右边锋":"m",u"左边锋":"m",
    u"左边卫":"b",u"右边卫":"b",u"前腰":"b",u"后腰":"c",u"中场":"g",
    u"左后卫":"y",u"右后卫":"y",u"门将":"k",u"中后卫":"k"}
  color = []
  for l in label:
    color.append(colorMap[l])
  fig = plt.figure()
  if 3 == dim:
    ax = Axes3D(fig)
    ax.scatter(data[:, 0], data[:, 1], data[:, 2], color = color, alpha=0.5)
  elif 2 == dim:
    ax = fig.add_subplot(111)
    ax.scatter(data[:, 0], data[:, 1], color = color, alpha=0.5)
  else:
    print "INVALID dim"
  plt.savefig('./plots/player_norm.png')
  #plt.show()

def findPoint(rawData, newData, xRange, yRange):
  print('-' * 30)
  print('xRange [%4.2f, %4.2f]  yRange [%4.2f, %4.2f]' %(xRange[0], xRange[1], yRange[0], yRange[1]))
  for i in range(0, len(rawData)):
    if newData[i][0] >= xRange[0] and \
      newData[i][0] <= xRange[1] and \
      newData[i][1] >= yRange[0] and \
      newData[i][1] <= yRange[1]:
      print("[%4.2f, %4.2f]   %s %s" %(newData[i][0], newData[i][1], rawData[i][1], rawData[i][0]))
  print('-' * 30)

def preprocess(abilities, pcaN):
  #print(abilities[0])
  data = normalize(abilities)
  #print(data[0])
  data = pca(data, pcaN)
  #print(data[0])
  
  return data

if __name__ == '__main__':
  # format of attributes:
  # name, position, standard_position, simple_position, all_rating
  pcaN = 2
  attributes, abilities = loadData()
  label = attributes[:, 1]
  data = preprocess(abilities, pcaN)
  # plot(label, data, pcaN)
  
  findPoint(attributes, data, [-1, 1], [0.4, 1])
  findPoint(attributes, data, [-1, -0.5], [-1, 1])
  findPoint(attributes, data, [-1, 1], [-1, -0.3])
  findPoint(attributes, data, [0, 0.3], [0, 0.2])
  findPoint(attributes, data, [0.55, 1], [-1, 1])
