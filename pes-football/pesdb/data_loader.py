#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-13 17:44:10
# @Author  : zhaoqun.czq

import os

def load(caseId):
  dataStr = ''
  dataPath = './data/' + caseId + '.txt'
  with open(dataPath, 'r') as fin:
    dataStr = fin.read()
  return dataStr