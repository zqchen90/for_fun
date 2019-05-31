#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-14 16:47:30
# @Author  : zhaoqun.czq

import difflib
from constants import *
import numpy as np

def normalize(data, axis = 1):
  rowMax = np.max(data, axis = axis)
  rowMaxT = np.reshape(rowMax, (len(rowMax), 1))
  normData = data / rowMaxT
  assert(data.shape == normData.shape)
  return normData

def vectorDistance(vector1, vector2, type = 'cosine'):
  if type == 'cosine':
    return vector1.dot(vector2) / np.sqrt(vector1.dot(vector1) * vector2.dot(vector2))
  else:
    return 0

def stringSimi(s1, s2):
  s1 = s1.upper().replace(' ', '').replace('.', '')
  s2 = s2.upper().replace(' ', '').replace('.', '')
  return difflib.SequenceMatcher(None, s1, s2).ratio()

def replaceLatinChar(name):
  convertName = name
  for item in LATIN_MAPPING:
    convertName = convertName.replace(item['latin'], item['eng'])
  return convertName

def findName(nameList, name):
  targetIdx = -1
  nameSimiThreshold = 0.8
  nameSimi = 0
  name = name.upper()
  for i, player in enumerate(nameList):
    compareName = replaceLatinChar(player)
    if compareName == name:
      return i
    if ' ' in compareName:
      if compareName.split(' ')[1] == name:
        return i
    simi = stringSimi(name, compareName)
    if simi > nameSimi:
      targetIdx = i
      nameSimi = simi
  if nameSimi >= nameSimiThreshold:
    return targetIdx
  else:
    return -1

def main(s1, s2):
  print('%s\t%s\t%4.3f' %(s1, s2, stringSimi(s1, s2)))
  print(findName(['L. INSIGNE', 'S. MANE'], 'insigne'))


if __name__ == '__main__':
  main('L. INSIGNE', 'insigne')
