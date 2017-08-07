#!/usr/bin/python
#coding=utf-8

'''
python里，标识符由数字字母下划线组成,但是不能以数字开头,标识符区分大小写
以单下划线开头的_foo代表不能直接访问的类属性，需要通过类提供的接口访问，
不能用from xxx import *导入;

以双下划线开头的__foo代表类的私有成员；一双下划线开头和结尾的__foo__代表
python里特殊方法专用的标识，如__init__()代表类的构造函数。

python可以一行显示多条语句，但是中间必须要用;隔开

python一般以新行作为语句的结束符，但是我们可以使用斜杠\将一行语句分为多行显示
或者用[]{}()
'''

print "你好";
print '-----------------'

import sys
x='yuhao'
sys.stdout.write(x + '\n' + 'hehe' + '\n')
print '-----------------'

x='a'
y='b'
print x
print y
print '-----------------'
print x,
print y

print '-----------------'
print sys.argv

print '-----------------'
raw_input("\n\nPress enter to exit.")
