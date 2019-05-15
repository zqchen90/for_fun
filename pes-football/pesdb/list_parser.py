#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-14 14:37:17
# @Author  : zhaoqun.czq

import os
from data_loader import load

def parsePlayerIds(dataStr):
  playerIds = []
  players = dataStr.split('<table class="players">')[1].split('</table>')[0].split('\n')
  for player in players:
    if 'href="./?id=' in player:
      id = player.split('href="./?id=')[1].split('"')[0]
      playerIds.append(id)
  return playerIds

def main():
  playerIds = []
  for i in range(5, 11, 1):
    dataId = 'list_page%d' % (i)
    dataStr = load('raw_data/' + dataId)
    ids = parsePlayerIds(dataStr)
    print('read %d players from %s' % (len(ids), dataId))
    playerIds.extend(ids)
  print(playerIds)

if __name__ == '__main__':
  main()