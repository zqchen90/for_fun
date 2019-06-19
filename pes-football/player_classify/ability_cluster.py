#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Date    : 2018-10-06 16:33:57
# @Author  : zhaoqun.czq
# Use PCA to reduce dimensions of players' ability vectors
# Cluster players by K-means
# Parameters including no. of PCA dimensions, noting as pcaN and no. of clusters, noting as clusterN
# can be assigned
# Traversing to find the best parameters combinations is also supported 
# using Calinski Harabaz Score as the metric

import numpy as np
from dataLoader import loadData
from utils import vectorDistance, normalize, pca
import sys
import string

from sklearn.cluster import KMeans
from sklearn import metrics
import matplotlib.pyplot as plt

def plot(label, data, dim, clusterN):
  colorList = ["r", "b", "g", "k", "y", "c", "m"]
  if 2 != dim:
    print "INVALID dim to plot"
  else:
    fig = plt.figure()
    ax = fig.add_subplot(111)
    color = []
    for l in label:
      color.append(colorList[l])
    ax.scatter(data[:, 0], data[:, 1], color = color, alpha=0.5)
    plt.savefig('./plots/ability_cluster.png')

def abilityCluster(attributes, abilities, pcaN, clusterN):
  reduceDimAbilities = pca(abilities, pcaN)
  predicts = KMeans(n_clusters = clusterN).fit_predict(reduceDimAbilities)
  playersInCluster = {}
  for i in range(clusterN):
    playersInCluster.update({i : []})

  for idx, att in enumerate(attributes):
    cluster = predicts[idx]
    playersInCluster[cluster].append('%d %s' %(int(att[4].encode('utf8')), att[0]))

  MAX_PLAYER_PRINT = 20
  for i in range(clusterN):
    print('\ncluster %d' %(i))
    playerInfos = sorted(playersInCluster[i], reverse=True)
    for j in range(MAX_PLAYER_PRINT):
      print(playerInfos[j])

  return reduceDimAbilities, predicts

def findBestCluster(attributes, abilities):
  print('Now find best parameters for clustering...')
  for pcaN in range(2, 18):
    reduceDimAbilities = pca(abilities, pcaN)
    maxScoreClusterN = -1
    maxScore = 0
    for clusterN in range(2, 20):
      predicts = KMeans(n_clusters = clusterN).fit_predict(reduceDimAbilities)
      clusterScore = metrics.calinski_harabaz_score(reduceDimAbilities, predicts)
      if clusterScore > maxScore:
        maxScore = clusterScore
        maxScoreClusterN = clusterN
    print('pcaN = %d, best clusterN = %d, score = %4.2f' %(pcaN, maxScoreClusterN, maxScore))

def preprocess(abilities):
  data = normalize(abilities)
  return data

def printUsage():
  print('Usage:\n\n\t1. Find best cluster parameters: python ability_cluster.py\n\t2. Run clustering: python ability_cluster.py 2 4')

if __name__ == '__main__':
  # format of attributes:
  # name, position, standard_position, simple_position, all_rating
  attributes, abilities = loadData()
  data = preprocess(abilities)

  if len(sys.argv) == 3:
    pcaN = string.atoi(sys.argv[1])
    clusterN = string.atoi(sys.argv[2])
    reduceDimAbilities, predicts = abilityCluster(attributes, data, pcaN, clusterN)
    plot(predicts, reduceDimAbilities, pcaN, clusterN)
  else:
    printUsage()
    # Best pcaN = 2, best clusterN = 4, score = 801.87
    findBestCluster(attributes, data)

  