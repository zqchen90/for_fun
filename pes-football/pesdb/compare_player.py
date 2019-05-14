#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-14 15:02:41
# @Author  : zhaoqun.czq
# 球员对比

import sys
import json
import string
from constants import *
from utils import stringSimi, findName

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

def comparePlayer(playerAbilities, name1, level1, name2, level2):
  name1, level1, abilities1 = getAbility(playerAbilities, name1, level1)
  name2, level2, abilities2 = getAbility(playerAbilities, name2, level2)

  if len(abilities1) == len(ABILITY_NAMES) and \
    len(abilities2) == len(ABILITY_NAMES):
    print('Compare\n %s (%d) v.s. %s (%d)\n' %(name1, level1, name2, level2))
    for i, abilityName in enumerate(ABILITY_NAMES):
      if abilities1[i] == abilities2[i]:
        print('\033[0m%d  %20s  %d\033[0m' %(abilities1[i], abilityName.center(20), abilities2[i]))
      elif abilities1[i] > abilities2[i]:
        print('\033[1;35m%d\033[0m  %20s  %d\033[0m' %(abilities1[i], abilityName.center(20), abilities2[i]))
      else:
        print('\033[0m%d  %20s  \033[1;35m%d\033[0m' %(abilities1[i], abilityName.center(20), abilities2[i]))

  else:
    print('Data invalid...')
    print(abilities1)
    print(abilities2)

def main():
  playerAbilities = loadPlayerAbilities('./data/abilities.txt')
  print('load %d players' %(len(playerAbilities)))

  name1 = 'insigne'
  level1 = 30
  name2 = 'sane'
  level2 = 30

  if len(sys.argv) == 5:
    name1 = sys.argv[1]
    level1 = string.atoi(sys.argv[2])
    name2 = sys.argv[3]
    level2 = string.atoi(sys.argv[4])
  elif len(sys.argv) == 3:
    name1 = sys.argv[1]
    name2 = sys.argv[2]
  else:
    pass
  comparePlayer(playerAbilities, name1, level1, name2, level2)
  

if __name__ == '__main__':
  main()

  
