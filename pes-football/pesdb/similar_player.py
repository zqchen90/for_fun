#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-26 20:04:41
# @Author  : zhaoqun.czq
# Find similar players

import sys
import json
import string
import numpy as np
from constants import *
from utils import normalize, vectorDistance, findName
import warnings
warnings.filterwarnings('ignore')

from sklearn.decomposition import PCA

n = 6

def pca(data):
  pca = PCA(n_components=n)
  newData = pca.fit_transform(data)
  print(pca.components_)  
  #print(pca.explained_variance_ratio_)  
  return newData

def loadPlayerAbilities(dataPath):
  with open(dataPath, 'r') as fin:
    playerAbilities = json.loads(fin.read())
  return playerAbilities

def getAbility(playerAbilities, name, level):
  abilities = []
  idx = findName(map(lambda x:x['name'], playerAbilities), name)

  if idx >= 0:
    player = playerAbilities[idx]
    name = player['name']
    if level > player['maxlevel']:
      level = player['maxlevel']
    for i, abilityName in enumerate(ABILITY_NAMES):
      abilities.append(player['abilityList'][i][level - 1])

  return name, level, abilities

def processAbility(ability):
  abilityArray = np.array(ability, dtype=np.float64)
  maxAbility = np.max(abilityArray)
  return abilityArray / maxAbility

def findSimilarPlayer(playerAbilities, name):
  DEFAULE_LEVEL = 30
  name, level, currentAbility = getAbility(playerAbilities, name, DEFAULE_LEVEL)

  print('-' * 20 + name + '-' * 20)
  simiList = []
  for otherIdx, player in enumerate(playerAbilities):
    if name == player['name']:
      continue
    otherAbility = []
    for i, abilityName in enumerate(ABILITY_NAMES):
      otherAbility.append(player['abilityList'][i][DEFAULE_LEVEL - 1])
    currentVector = processAbility(currentAbility)
    otherVector = processAbility(otherAbility)
    simi = vectorDistance(currentVector, otherVector)
    # if 'NEYMAR' ==player['name']:
    #   print(currentVector)
    #   print(otherVector)
    #   print(simi)
    simiList.append([otherIdx, simi])
    
  sortSimiList = sorted(simiList, key = lambda x: x[1], reverse = True)
  for i in range(10):
    print('%2d %4.4f  %s' %(i+1, sortSimiList[i][1], playerAbilities[sortSimiList[i][0]]['name']))

def main():
  playerAbilities = loadPlayerAbilities('./data/abilities.txt')
  print('load %d players' %(len(playerAbilities)))

  if len(sys.argv) == 2:
    name = sys.argv[1]
  else:
    name = 'messi'
  findSimilarPlayer(playerAbilities, name)
  

if __name__ == '__main__':
  main()

  
