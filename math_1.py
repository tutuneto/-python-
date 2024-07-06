# 这是小畅畅写的打招呼
from base64 import b16decode


print('hello world!')
print("happy,not hapy")

name1 = 'clevergua'

name2 = 'ccの哥哥'

print(name1, name2)

name4 = '345345'

print(f'my name is {name4}')

text = 'study English'
print(f'Im able to {text}')

# coding=UTF-8
print("这是中文打印,避免有出入")

# -*- coding: UTF-8 -*-
print("睡觉觉吧")

# 加法运算
a = 4 + 5
print(a)

TotalAge = 18 + 45
print(TotalAge)

Mymoney = 218 + 175
print(Mymoney)

# 除法运算
r = 30 / 3
print(r)

# 乘法运算
m = 3
n = 7
sale = m * n
print(f'today I earn {sale} RMB')

Totalspend = 40 * 90
print(Totalspend)

# 取整运算,也称取商数运算
print(9 // 4)

# 取模运算,也称取余数运算
print(9 % 4)

# 布尔数 是一种数据类型,只有真\假两种类型
a1 = True
a2 = False

# 比较运算符有六种
3 == 3
4 > 1
5 < 6
3 != 4
1, 2 <= 4
4, 5 >= 2

Myheight = 178
Yourheight = 176
print(Myheight > Yourheight)

# 逻辑运算常见的有:and并且\or或者\not非
print(True and True)
print(True and False)
print(False and False)

print(True or True)
print(True or False)
print(False or False)

# 由于变量名区分大小写,所以and不能作为变量名,但是And可以
And = 1
Mnd = 2
print(And > Mnd)

# IF判断语句
Myage = 19
Yourage = 15
if Myage > Yourage:
    print('I am older than you')
if Myage < Yourage:
    print("You are older tham me")

Myweight = 103
canride = True
if Myweight > 90:
    print("overweight can not ride")
    canride = False
print (canride)


Mylove = 100
cankiss = True
if Mylove < 60 :
    print("不能亲亲")
    cankiss = False
print(cankiss)


Myweight = 70.5
Yourweight = 81.3
if Myweight < Yourweight:
    print ("you are heavier than me")


#括号和比较运算的实例,仅当and运算两端都为True时,运算结果才为True,其他情况为false

TodayDate = 20181111
MyAccount = 9087.04
earpod = True
if (TodayDate == 20181111) and (MyAccount >18923):
    print("I will buy a earpod")
    earpod = False
print ("buy nothing")

Number1 = 10
Number2 = 20
Number3 = 30
Result = (Number1 < Number2) and (Number2 > Number3)
print (Result)

# str函数--取整\字符串
str(29)
print('I am ' + str(29) + ' years old.')

# 
spam = input (101)
spam = int(spam)

