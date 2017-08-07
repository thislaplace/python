#!/usr/bin/python
#coding=utf-8

'''
变量赋值简单粗暴不需要声明类型, 灵活多变,非常好用。
数字数据类是不可改变的数据类型，改变数字数据类型会分配一个新的对象。
字符串的操作有基本的功能不需要再自己进行拼接遍历的操作。
列表用 "[ ]" 标识类似 C 语言中的数组。
元组用 "( )" 标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表。
字典用 "{ }" 标识。字典由索引 key 和它对应的值 value 组成。
赵琪
赵琪
169***3273@qq.com
5个月前 (03-07)
唐
454***373@qq.com
变量赋值
a = 1
b = "god"
字符串赋值
str = 'this is string 1'
列表串赋值
list = ['this', 'is', 'list', 2]
元组赋值
tuple = ('this', 'is', 'tuple', 3)
字典赋值
dict = {1:'this', 2:'is', 3:'dictionary', 4:4}
唐
唐
454***373@qq.com
5个月前 (03-10)
tuister
tui***r@foxmail.com
python 的所有数据类型都是类,可以通过 type() 查看该变量的数据类型:
>>> n=1
>>> type(n)
<type 'int'>
>>> n="runoob"
>>> type(n)
<type 'str'>
>>> 
此外还可以用 isinstance 来判断：
a = 111
isinstance(a, int)
True
isinstance 和 type 的区别在于：
>>> class A:
...     pass
... 
>>> class B(A):
...     pass
... 
>>> isinstance(A(), A)
True
>>> type(A()) == A
False
>>> isinstance(B(), A)
True
>>> type(B()) == A 
False
区别就是:
type()不会认为子类是一种父类类型。
isinstance()会认为子类是一种父类类型。
tuister
tuister
tui***r@foxmail.com
5个月前 (03-12)
流浪猴子
122***6850@qq.com
数据类型 分为数字型和非数字型。
数字型包括整型，长整型，浮点型，复数型；
非数字型包括字符串，列表，元组和字典 ；
非数字型的共同点：都可以使用切片、链接（+）、重复（*）、取值（a[]）等相关运算;
非数字型的不同点：
列表 可以直接赋值，元组不可以赋值，字典按照 dict[k]=v 的方式赋值。
流浪猴子
流浪猴子
122***6850@qq.com
3个月前 (04-27)
python.熊
767***386@qq.com
字符串表示方式：str="hello,world"
列表表示方式：list=['hello',2,3,4,'world']
元组：tuple={'hello',2,3,4,'world'}
截取方式相同：名称[头下标:尾下标]
下标是从0开始算起，可以是正数或者负数，下标为空则表示取到头或者尾
开始截取时，包含了下边界，而截取到最大范围不包括上边界。
元组不能二次赋值，列表可以
python.熊
python.熊
767***386@qq.com
3个月前 (05-02)
sunny想学python
139***38053@163.com
Python变量类型：
（1）Numbers
（2）String
（3）List  []
（4）Tuple（元祖）(),相当于只读列表，不可以二次赋值
（5）dictionary（字典）{}，key值对
'''

counter = 100
miles = 1000.0
name = 'yuhao'

print '------------var----------------'
print counter
print miles
print name

a = b = c = 1
a, b, c = 1, 2, 'yuhao'

'''
Numbers
String
List
Tuple
Dictionary
'''

var = 1
del var

print '\n\n-------------string---------------'
str = 'hfut.edu.cn'
print str[2]
print str[2:7]+'yuhao'
print str * 2

print '\n\n-------------list---------------'
list1 = ['yuhao', 1, 1.123, 15]
list2 = ['heh', 'e']
print list1
print list1[0]
print list1[1:3]
print list1[2:]
print list2 * 2
print list1 + list2 

print '\n\n-------------tuple--------------'
tuple1 = ('yuhao', 1, 1.123, 15)
tuple2 = ('heh', 'e')
print tuple1
print tuple1[0]
print tuple1[1:3]
print tuple1[2:]
print tuple2 * 2
print tuple1 + tuple2 

list1[2] = 2.123
#tuple[2] = 2.213非法元祖不允许更新


print '\n\n-------------dictionary---------------'
'''
字典当中的元素是通过键来存取的，不是通过偏移存取
字典由索引key和它对应的值value组成
'''
dict = {}
dict['one'] = 'this is one'
dict[2] = 'this is two'

tinydict = {'name':'yuhao', 'height':'169', 'weight':'60kg'}

print dict['one']
print dict[2]
print dict['one']
print dict
print tinydict
print tinydict.keys()
print tinydict.values()



