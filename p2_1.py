# p2_1.py
"""---第一个小游戏---"""
import random

secret = random.randint(1,10)
temp = input("不妨猜测一下刘向阳现在心里想的数字：")
guess = int(temp)
i = 0

if guess == secret:
   print("你是小刘心里的蛔虫吗？！")
   print("哼，猜对了也没有奖励！")
else:
   while (guess != secret) and (i<=10):
      temp = input("哎呀，猜错了，请重新输入吧：")
      guess = int(temp)
      i = i+1
   
   if guess == secret:
      print("你是小刘心里蛔虫吗？！")
      print("哼，猜对了也没有奖励！")
   else:
      if guess > secret:
         print("哥，大了大了...")
      else:
         print("嘿，小了小了...")
print("游戏结束，不玩啦^_^")
