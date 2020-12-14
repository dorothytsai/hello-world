# -*- coding: utf-8 -*-

# 導入 random 套件，用以產生隨機變數
import random

answer = '' # initial user answer (存放產生的 4 位數字) 
a_count=0 # initial A count (正確數字和正確位置計數)
b_count=0 # initial B count (正確數字不正確位置計數)
name=input("Please enter your name:")
print("Hi!%s~Welcome!"%name)
times=0
import time as t
import random as r
#设置开始时间
starttime=t.time()

# start 產生隨機四個數字
# 數字列表 (list)
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# shuffle() 方法將序列的所有元素隨機排序
random.shuffle(items)
# 從數字列表中挑選前4個數字
for i in range(4):
    # 將正確答案以字串格式處理
    answer+=str(items[i])
# end 產生隨機四個數字

# start 進入迴圈，直到玩家正確猜出數字
while(True):
    # 取得使用者輸入的數字，number 屬於 string type
    number=input('Please enter four numbers: ')
    # 判斷使用者是否輸入非數字或少於 4 個數字的內容
    # isdigit() 方法檢測字串是否只由數位組成
    # len() 方法用以取得變數的長度
    if not number.isdigit() or len(number) != 4:  #cheak all input is digit
        # 使用者輸入非數字的內容，提醒使用者輸入 4 個數字
        print('Please enter four digits number')
    # 使用者正確輸入數字
    else:
        # 使用者輸入正確 4 個數字
        times=times+1
        if number==answer:
            print('excellent you guess the correct number')
            # break 用以跳出 while 迴圈
            break
        # 判斷使用者輸入的 4 個數字有幾個對
        # i 用以指向使用者輸入的第 i 個位置
        for i in range(4):
            # j 用以指向正確答案的第 j 個位置
            for j in range(4):
                # 計數位置對且數字對的個數
                if i==j and number[i]==answer[j]:
                    a_count+=1
                # 計數位置錯但數字對的個數
                elif number[i]==answer[j]:
                    b_count+=1
        # 告訴使用者輸入的數字 XAXB
        print('{0}A{1}B'.format(a_count,b_count))
        # 將計數歸零
        a_count=0
        b_count=0
# end 進入迴圈，直到玩家正確猜出數字
print("Wow~ Nice job %s well done~"%name)
#设置结束时间
endtime=t.time()
time=endtime-starttime
print("你共猜了%d次,花了%.2f秒的時間"%(times,time))

