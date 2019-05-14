#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-13 17:43:12
# @Author  : zhaoqun.czq

import os
import json
from constants import *
from data_loader import load
from player_parser import parseName, parseScout


def main():
  playerAbilitiesMap = []
  for caseId in PLAYER_IDS:
    dataStr = load(caseId)
    name = parseName(dataStr)
    scouts = parseScout(dataStr)

    playerAbilitiesMap.append({'id': caseId,\
                               'name': name,\
                               'scouts': scouts})

  print(json.dumps(playerAbilitiesMap))

if __name__ == '__main__':
  main()