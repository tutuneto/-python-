#!/usr/bin/python  json本身没有类型,通过变量名高速使用者类型
import json

taskJsonString = '{ "Date": "2023.6.8.21.58.00", "Content": "我要吃糯米鸡","IsChecked": true}'
taskDictionary = json.loads(taskJsonString)
print(taskDictionary['Date'])
if taskDictionary['IsChecked']:
    print("A")
else:
    print("B")


spam = ['cat', 'bat', 'rat', 'elephant']
spam[0]
'cat'
spam[1]
'bat'
spam[2]
'rat'
spam[3]
'elephant'
print('hello'+spam[0])

