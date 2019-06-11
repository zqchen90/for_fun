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

PCA_N_COMPONENTS = 6
DEFAULE_LEVEL = 30
NORM_FLAG = False
VECTOR_NORM_FLAG = False
DEBUG = False

def pca(data, n):
  pca = PCA(n_components=n)
  newData = pca.fit_transform(data)
  #print(pca.components_)  
  #print(pca.explained_variance_ratio_)  
  return newData

def loadPlayerAbilities(dataPath):
  with open(dataPath, 'r') as fin:
    playerAbilities = json.loads(fin.read())
  return playerAbilities

def processAbility(ability):
  abilityArray = np.array(ability, dtype=np.float64)
  if VECTOR_NORM_FLAG:
    maxAbility = np.max(abilityArray)
    return abilityArray / maxAbility
  else:
    return abilityArray

# Load players' abilities at certain level
# and converted to numpy array
def getAllAbilities(playerAbilities, level):
  overallRatings = []
  abilities = []
  for idx, player in enumerate(playerAbilities):
    otherAbility = []
    for i, abilityName in enumerate(ABILITY_NAMES):
      ability = player['abilityList'][i][level - 1]
      if 'Overall Rating' == abilityName:
        overallRatings.append(ability)
      else:
        otherAbility.append(ability)
    abilities.append(otherAbility)
  return np.array(overallRatings, dtype=np.float64), np.array(abilities, dtype=np.float64)

def findSimilarPlayer(playerAbilities, name):
  idx = findName(map(lambda x:x['name'], playerAbilities), name)
  currentName = playerAbilities[idx]['name']

  overallRatings, allAbilities = getAllAbilities(playerAbilities, DEFAULE_LEVEL)
  if NORM_FLAG:
    normAbilities = normalize(allAbilities)
  else:
    normAbilities = allAbilities
  normAbilitiesDimReduction = pca(normAbilities, PCA_N_COMPONENTS)

  if DEBUG:
    print('current player: %s (%d)' %(currentName, overallRatings[idx]))
    print('original ability:')
    print(allAbilities[idx])
    print('normalized ability:')
    print(normAbilities[idx])
    print('normalized ability with pca:')
    print(normAbilitiesDimReduction[idx])


  currentAbility = normAbilitiesDimReduction[idx]

  print('-' * 20 + currentName + '-' * 20)
  simiList = []
  for otherIdx, otherAbility in enumerate(normAbilitiesDimReduction):
    if idx == otherIdx:
      continue
    otherAbility = normAbilitiesDimReduction[otherIdx]
    currentVector = processAbility(currentAbility)
    otherVector = processAbility(otherAbility)
    simi = vectorDistance(currentVector, otherVector)
    simiList.append([otherIdx, simi])
    
  sortSimiList = sorted(simiList, key = lambda x: x[1], reverse = True)
  print('idx  ratings(30)  similarity  name')
  for i in range(10):
    print('%2d %8d       %8.3f    %s' %(i+1, overallRatings[sortSimiList[i][0]], sortSimiList[i][1], playerAbilities[sortSimiList[i][0]]['name']))

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

  
