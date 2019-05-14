#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-14 17:35:53
# @Author  : zhaoqun.czq

import string
import json

def getScoutName(lineStr):
  return lineStr.split('</a>')[0].split('>')[1].replace(' ', '_')

def parseScout(dataStr):
  scouts = []
  scoutLines = dataStr.split('<table class="scouts">')[1].split('</table>')[0].split('\n')
  for line in scoutLines:
    items = line.split('<td>')
    if len(items) != 6:
      continue
    rating = getScoutName(items[1])
    scout1 = getScoutName(items[2])
    scout2 = getScoutName(items[3])
    scout3 = getScoutName(items[4])
    percent = getScoutName(items[5])
    if percent == '100%':
      scouts.append({'rating': rating, 'scouts': [scout1, scout2, scout3]})
  return scouts

def parseMaxLevel(dataStr):
  maxLevel = dataStr.split('var max_level = ')[1].split(';')[0]
  return string.atoi(maxLevel)

def parseAbility(dataStr):
  abilityStr = dataStr.split('abilities = ')[1].split(';')[0]
  return json.loads(abilityStr)

# <tr><th>Player Name:</th><td>S. UMTITI</td></tr>
def parseName(dataStr):
  return dataStr.split('<tr><th>Player Name:</th><td>')[1].split('</td></tr>')[0]