#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-26 16:37:56
# @Author  : zhaoqun.czq

import numpy as np
import math
import warnings
warnings.filterwarnings('ignore')

from sklearn.decomposition import PCA

def vectorDistance(vector1, vector2, type = 'cosine'):
  if type == 'cosine':
    return vector1.dot(vector2) / np.sqrt(vector1.dot(vector1) * vector2.dot(vector2))
  else:
    return 0

def normalize(data):
  rowMax = np.max(data, axis = 1)
  rowMaxT = np.reshape(rowMax, (len(rowMax), 1))
  normData = data / rowMaxT
  assert(data.shape == normData.shape)
  return normData


def pca(data, n = 2):
  pca = PCA(n_components=n)
  newData = pca.fit_transform(data) 
  return newData


if __name__ == '__main__':
  assert(0 == vectorDistance(np.array([1,0]), np.array([0,1])))
  assert(1 / np.sqrt(2) == vectorDistance(np.array([1,0]), np.array([1,1])))

