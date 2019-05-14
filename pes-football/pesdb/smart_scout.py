#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-14 17:39:42
# @Author  : zhaoqun.czq

import sys
import json
from utils import findName

def loadScouts(dataPath):
  with open(dataPath, 'r') as fin:
    playerAbilities = json.loads(fin.read())
  return playerAbilities

def getScoutsByName(scoutsMap, name):
  candicates = []
  idx = findName(map(lambda x:x['name'], scoutsMap), name)
  if idx >= 0:
    for scout in scoutsMap[idx]['scouts']:
      candicates.append('%s  %s  %s  %s  %s' %(scoutsMap[idx]['name'], scout['rating'], scout['scouts'][0], scout['scouts'][1], scout['scouts'][2]))
  return candicates

def getScoutsByScout(scoutsMap, targetScounts):
  candicates = []
  for player in scoutsMap:
    for scout in player['scouts']:
      findTarget = True
      for targetScout in targetScounts:
        if targetScout not in ' '.join(scout['scouts']):
          findTarget = False
      if findTarget:
        candicates.append('%s  %s  %s  %s  %s' %(player['name'], scout['rating'], \
                                     scout['scouts'][0], scout['scouts'][1], \
                                     scout['scouts'][2]))
  return candicates

def getScoutsNeedTwo(scoutsMap):
  candicates = []
  for player in scoutsMap:
    for scout in player['scouts']:
      if scout['scouts'][2] == '-':
        candicates.append('%s  %s  %s  %s  %s' %(player['name'], scout['rating'], \
                                     scout['scouts'][0], scout['scouts'][1], \
                                     scout['scouts'][2]))
  return candicates

def sortCandicates(candicates):
  return sorted(candicates, key = lambda x: x.find('  -'), reverse = True)

def main():
  scoutsMap = loadScouts('./data/scouts.txt')
  print('load %d players' %(len(scoutsMap)))
  candicates = []
  if 3 == len(sys.argv) and sys.argv[1] == '-p':
    name = sys.argv[2]
    print('find scouts by name: %s' %(name))
    candicates = getScoutsByName(scoutsMap, name)
  elif 3 == len(sys.argv) and sys.argv[1] == '-s':
    targetScounts = sys.argv[2].split('#')
    print('find scouts by scout: %s' %(' + '.join(targetScounts)))
    candicates = getScoutsByScout(scoutsMap, targetScounts)
  elif 5 == len(sys.argv) and sys.argv[1] == '-p' and sys.argv[3] == '-s':
    name = sys.argv[2]
    targetScounts = sys.argv[4].split('#')
    print('find scouts by name %s and scout: %s' %(name, ' + '.join(targetScounts)))
    candicatesByName = getScoutsByName(scoutsMap, name)
    candicatesByScout = getScoutsByScout(scoutsMap, targetScounts)
    candicates = list(set(candicatesByName).intersection(set(candicatesByScout)))
  else:
    candicates = getScoutsNeedTwo(scoutsMap)

  sortedCandicates = sortCandicates(candicates)
  print('\n'.join(sortedCandicates))

if __name__ == '__main__':
  main()