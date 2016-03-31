# -*- coding: utf-8 -*-

import random

class RandomChar():
  """用于随机生成汉字"""
  @staticmethod
  def Unicode():
    val = random.randint(0x4E00, 0x9FBF)
    return unichr(val)

  @staticmethod
  def GB2312():
    head = random.randint(0xB0, 0xCF)
    body = random.randint(0xA, 0xF)
    tail = random.randint(0, 0xF)
    val = ( head << 8 ) | (body << 4) | tail
    str = "%x" % val
    return str.decode('hex').decode('gb2312')
  @staticmethod
  def GetRandom():
    val = random.randint(1,1000000)
    if(val%2 == 0):
      return True
    else:
      return False
if __name__ == '__main__':
    name=RandomChar.GB2312()+RandomChar.GB2312()+RandomChar.GB2312()
    print name
    print RandomChar.GetRandom()