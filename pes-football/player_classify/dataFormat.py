#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Date    : 2018-10-06 14:08:10
# @Author  : zhaoqun.czq

import json

dataFilePath = "./data/player.json"
dataFormatter = [u"编号",u"名称",u"位置",u"评分",u"身高",u"体重",u"攻击能力",u"控球",u"盘球",u"地面传球",u"空中传球",u"射门",u"定位球",u"弧度",u"头球",u"防守能力",u"抢球",u"脚下力量",u"速度",u"爆发力",u"身体平衡",u"跳跃",u"体力",u"守门",u"接球",u"解围",u"扑救反应",u"覆盖区域",u"状态持续性",u"抗受伤程度",u"非惯用脚使用频率",u"非惯用脚精准度"]

def readData():
  with open(dataFilePath, 'r') as fin:
    return json.loads(''.join(fin.readlines()).decode('utf8'))

def findPlayer(data, playerId, dataFormatter):
  formatPlayerData = []
  for player in data["data"]:
    if player[u"编号"] == playerId:
      print("Find player %s %s" %(playerId, player[u"名称"]))
      for item in dataFormatter:
        formatPlayerData.append(player[item])
  return formatPlayerData

def demoFindPlayer():
  data = readData()
  playerId = "6182559"
  playerData = findPlayer(data, playerId, dataFormatter)
  print '\n'.join(playerData)

def convertDataFormat(data, dataFormatter, seperator):
  for player in data["data"]:
    convertedData = []
    for item in dataFormatter:
      convertedData.append(player[item])
    print seperator.join(convertedData)

if __name__ == '__main__':
  # demoFindPlayer()
  convertDataFormat(readData(), dataFormatter, "#")