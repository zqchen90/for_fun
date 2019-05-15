#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-14 16:47:30
# @Author  : zhaoqun.czq

import difflib

def stringSimi(s1, s2):
  s1 = s1.upper().replace(' ', '').replace('.', '')
  s2 = s2.upper().replace(' ', '').replace('.', '')
  return difflib.SequenceMatcher(None, s1, s2).ratio()

def findName(nameList, name):
  targetIdx = -1
  nameSimiThreshold = 0.8
  nameSimi = 0
  name = name.upper()
  for i, player in enumerate(nameList):
    if player == name:
      return i
    if ' ' in player:
      if player.split(' ')[1] == name:
        return i
    simi = stringSimi(name, player)
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
