#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-19 16:01:22
# @Author  : zhaoqun.czq
# Use PCA to reduce dimensions of players' ability vectors
# Calculate similarities by cosine
# Print top10 most similar players to each player

import string
import sys
import traceback
from dataLoader import loadData
from utils import vectorDistance, normalize, pca

def findSimilaryPlayer(attributes, abilities):
  cnt = 0
  for idx, att in enumerate(attributes):
    if att[4] < 85:
      continue
    print('-' * 20 + att[0] + '-' * 20)
    currentAbility = abilities[idx, :]
    simiList = []
    for otherIdx, otherAbility in enumerate(abilities):
      if idx == otherIdx:
        continue
      if string.atoi(attributes[otherIdx][4]) < 83:
        continue
      simi = vectorDistance(currentAbility, otherAbility)
      simiList.append([otherIdx, simi])
    
    sortSimiList = sorted(simiList, key = lambda x: x[1], reverse = True)
    for i in range(10):
      print('%2d %4.2f  %s' %(i+1, sortSimiList[i][1], attributes[sortSimiList[i][0], 0]))
    
    cnt = cnt + 1
    if cnt >= 100:
      break

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
  attributes, abilities = loadData()

  pcaN = 2
  try:
    if len(sys.argv) == 1:
      pcaN = 2
    elif len(sys.argv) == 2:
      pcaN = string.atoi(sys.argv[1])
    else:
      raise ValueError('invalid parameter')
    print('PCA N = %d' %(pcaN))
    data = preprocess(abilities, pcaN)
    #findSimilaryPlayer(attributes, data)
  except Exception, ex:
    print('Usage: python similar_player.py [number]')
    traceback.print_exc()

    
  