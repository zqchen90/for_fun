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

def loadCandicateScout(dataPath):
  candicateScouts = []
  with open(dataPath, 'r') as fin:
    for line in fin:
      candicateScouts.append(line.strip())
  return candicateScouts

# get scouts given player's name
def getScoutsByName(scoutsMap, name):
  candicates = []
  idx = findName(map(lambda x:x['name'], scoutsMap), name)
  if idx >= 0:
    for scout in scoutsMap[idx]['scouts']:
      candicates.append('%20s %3s %36s %36s %36s' %(scoutsMap[idx]['name'], scout['rating'], scout['scouts'][0], scout['scouts'][1], scout['scouts'][2]))
  return candicates

# get scouts combinations given parts of the scouts
# may needs another scouts not in targetScouts
def getScoutsByScout(scoutsMap, targetScouts):
  candicates = []
  for player in scoutsMap:
    for scout in player['scouts']:
      findTarget = True
      for targetScout in targetScouts:
        if targetScout not in ' '.join(scout['scouts']):
          findTarget = False
      if findTarget:
        candicates.append('%20s %3s %36s %36s %36s' %(player['name'], scout['rating'], \
                                     scout['scouts'][0], scout['scouts'][1], \
                                     scout['scouts'][2]))
  return candicates

# get scouts combinations by candicateScouts only
def getScoutsByScoutOnly(scoutsMap, candicateScouts, maxRating = "4*"):
  candicateScoutsStr = ' '.join(candicateScouts)
  fullCandicates = []
  needOneCandicates = []
  for player in scoutsMap:
    for scout in player['scouts']:
      if scout['rating'] > maxRating:
        continue 
      if (scout['scouts'][0] in candicateScoutsStr or scout['scouts'][0] == '-') \
        and (scout['scouts'][1] in candicateScoutsStr or scout['scouts'][1] == '-') \
        and (scout['scouts'][2] in candicateScoutsStr or scout['scouts'][2] == '-'):
        fullCandicates.append('%20s %3s %34s %34s %34s' %(player['name'], scout['rating'], \
                                     scout['scouts'][0], scout['scouts'][1], \
                                     scout['scouts'][2]))
      elif scout['scouts'][0] in candicateScoutsStr and scout['scouts'][1] in candicateScoutsStr:
        needOneCandicates.append('%20s %3s %34s %34s %34s - %34s' %(player['name'], scout['rating'], \
                                     scout['scouts'][0], scout['scouts'][1], \
                                     scout['scouts'][2], scout['scouts'][2]))
      elif scout['scouts'][0] in candicateScoutsStr and scout['scouts'][2] in candicateScoutsStr:
        needOneCandicates.append('%20s %3s %34s %34s %34s - %34s' %(player['name'], scout['rating'], \
                                     scout['scouts'][0], scout['scouts'][1], \
                                     scout['scouts'][2], scout['scouts'][1]))
      elif scout['scouts'][1] in candicateScoutsStr and scout['scouts'][2] in candicateScoutsStr:
        needOneCandicates.append('%20s %3s %34s %34s %34s - %34s' %(player['name'], scout['rating'], \
                                     scout['scouts'][0], scout['scouts'][1], \
                                     scout['scouts'][2], scout['scouts'][0]))
      else:
        pass
  return fullCandicates, needOneCandicates

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
    targetScouts = sys.argv[2].split('#')
    print('find scouts by scout: %s' %(' + '.join(targetScouts)))
    candicates = getScoutsByScout(scoutsMap, targetScouts)
  elif 3 == len(sys.argv) and sys.argv[1] == '-f':
    candicateScouts = loadCandicateScout(sys.argv[2])
    print('find play by candicate scout: %s' %(', '.join(candicateScouts)))
    fullCandicates, needOneCandicates = getScoutsByScoutOnly(scoutsMap, candicateScouts)
    print('-' * 30 + ' have all scouts ' + '-' * 30)
    print('\n'.join(sortCandicates(fullCandicates)))
    print('-' * 30 + ' have two scouts and need another one ' + '-' * 30)
    print('\n'.join(sortCandicates(needOneCandicates)))
  elif 5 == len(sys.argv) and sys.argv[1] == '-p' and sys.argv[3] == '-s':
    name = sys.argv[2]
    targetScouts = sys.argv[4].split('#')
    print('find scouts by name %s and scout: %s' %(name, ' + '.join(targetScouts)))
    candicatesByName = getScoutsByName(scoutsMap, name)
    candicatesByScout = getScoutsByScout(scoutsMap, targetScouts)
    candicates = list(set(candicatesByName).intersection(set(candicatesByScout)))
  else:
    candicates = getScoutsNeedTwo(scoutsMap)

  sortedCandicates = sortCandicates(candicates)
  print('\n'.join(sortedCandicates))

if __name__ == '__main__':
  main()