#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Date    : 2018-10-06 16:28:00
# @Author  : zhaoqun.czq

import numpy as np
import string

positionMap = {u"中锋": 0,u"影锋": 0,u"右边锋": 1,u"左边锋": 1,u"左边卫": 2,u"右边卫": 2,u"前腰":2,u"中场":3,u"后腰":4,u"左后卫": 5,u"右后卫": 5,u"中后卫":6,u"门将":7}
simplePositionMap = {u"中锋": 0,u"影锋": 0,u"右边锋": 0,u"左边锋": 0,u"左边卫": 1,u"右边卫": 1,u"前腰":1,u"中场":1,u"后腰":1,u"左后卫": 2,u"右后卫": 2,u"中后卫":2,u"门将":3}

def loadData():
  dataFilePath = "./data/player.txt"
  lineCnt = 0
  attributes = []
  abilities = []
  with open(dataFilePath, 'r') as fin:
    for line in fin.readlines():
      item = []
      if 0 == lineCnt:
        lineCnt = lineCnt + 1
        continue
      parts = line.decode('utf8').strip().split('#')
      if parts[2] == u"门将":
        continue
      # name, position, standard_position, simple_position, all_rating
      attributes.append([parts[1]
                        , parts[2], positionMap[parts[2]], simplePositionMap[parts[2]] 
                        , string.atoi(parts[3])
                        ]
                        )  
      for i in range(6, 23):
        item.append(string.atoi(parts[i]))
      abilities.append(item)
  # print("data sample:")
  # print(attributes[0])
  # print(abilities[0])
  # print("load data: %d" %(len(attributes)))
  return np.array(attributes), np.array(abilities, dtype=np.float64)

if __name__ == '__main__':
  loadData()
