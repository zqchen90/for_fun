#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-13 17:25:40
# @Author  : zhaoqun.czq
# 解析能力值

import json
from data_loader import load
from constants import *
from player_parser import parseName, parseMaxLevel, parseAbility

def main():
  playerAbilitiesMap = []
  for caseId in PLAYER_IDS:
    dataStr = load('raw_data/' + caseId)
    name = parseName(dataStr)
    maxLevel = parseMaxLevel(dataStr)
    abilities = parseAbility(dataStr)
    print('caseId = %s\n\tname = %s\n\tmaxLevel = %d' %(caseId, name, maxLevel))

    playerAbilitiesMap.append({'id': caseId,\
                               'name': name,\
                               'maxlevel': maxLevel,\
                               'abilityList': abilities})

  print(json.dumps(playerAbilitiesMap))

if __name__ == '__main__':
  main()
