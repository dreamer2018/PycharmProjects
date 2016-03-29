#!/usr/bin/env python
#coding=utf-8
__author__ = 'zhoupana'

#mosi . --> 0 - -->1

#导入系统模块
import sys

#定义编码字典
drit={'A':'01',   'B':'1000', 'C':'1010', 'D':'100',  'E':'0',
      'F':'0010', 'G':'110',  'H':'0000', 'I':'00',   'J':'0111',
      'K':'101',  'L':'0100', 'M':'11',   'N':'10',   'O':'111',
      'P':'0110', 'Q':'1101', 'R':'010',  'S':'000',  'T':'1',
      'U':'001',  'V':'0001', 'W':'011',  'X':'1001', 'Y':'1011',
      'Z':'1100',

      '1':'01111', '2':'00111', '3':'00011', '4':'00001', '5':'00000',
      '6':'10000', '7':'11000', '8':'11100', '9':'11110', '0':'11111',

      '.':'010101',':':'111000', ',':'110011',';':'101010','?':'001100',
      '=':'10001', '!':'101011', '-':'100001','_':'001101','(':'10110',
      ')':'101101','$':'0001001','&':'01000','@':'011010','+':'01010',
      "'":'011110','/':'10010',
      ' ':' '
      }
#定义解码字典
drit_reversed={}

#反转编码字典得到解码字典
for key,value in drit.items():
    drit_reversed[value]=key

#加密，并写入文件
def EncodeReadFile():
      #加密文件
      encode=open("1.encode",'r')
      #解密文件
      decode=open("1.decode",'w')
      #迭代整合文件
      for string in encode.readlines():
            print(string,end="")
            for str in string:
                  try:
                        decode.write(drit[str.upper()])
                        decode.write(" ")
                  except KeyError:
                        pass
            decode.write("\n")
#解密，输出到文件到你中，并显示在屏幕上
def DecodeReadFile():
      #加密文件
      encode=open("2.encode",'w')
      #解密文件
      decode=open("1.decode",'r')
      #迭代整个文件
      for string in decode.readlines():
            #将读取的一行用空格分隔开
            result=Split(string)
            for str in result:
                  try:
                       print(drit_reversed[str.upper()],end="")
                       encode.write(drit_reversed[str.upper()])
                  except KeyError :
                        encode.write(drit_reversed[" "])
                        print(" ",end="")
            encode.write("\n")
            print()

def Split(String):
      ret=[]
      j=0
      for i in range(0,len(String)):
            if(String[i] == ' '):
                  if(i == 0):
                        pass
                  elif(i == j):
                        ret.append(String[j])
                  else:
                        ret.append(String[j:i])
                  j=i+1
      return ret
if __name__ == '__main__':
      #EncodeReadFile()
      DecodeReadFile()
