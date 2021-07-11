# 映射关系，一对一or多对一
from collections import OrderedDict
dic = {}    #初始化为空

dic = {1:'a', 2:'b'}
dic[3] = 'c'

for keys in dic.keys():
    print(keys, end=' ')
print('\n', end='')

for value in dic.values():
    print(value, end=' ')
print('\n', end='')

for item in dic.items():
    print(item, end=' ')
print('\n', end='')

shallowCopy = dic.copy()                #浅拷贝，复制一模一样的对象
hardCopy = dic                          #深拷贝，即赋值，是同一个对象，相当于指针

print(dic.fromkeys((1, 3), 'd'))        #浅拷贝

print(dic.get(1))                       #查到key返回value,否则返回NULL
print(dic.setdefault(4, 'd'))           #查到key返回value，否则添加
dic.pop(3)                              
dic.popitem()                           #随机弹出，字典没有顺序(好像变成了先进后出)
print(dic)

dic2 = dict(HTY='学不完了呜呜呜')        #key不需要引号，默认为字符串
dic2['ZXA'] = '快乐看剧'
print(dic2)

dic.update(dic2)                        #将一个集合添加到另一个中去
print(dic)
dic.clear()                             #清空

#按顺序添加
code = OrderedDict()
code['1'] = 'C'
code['2'] = 'python'
code['3'] = 'Cpp'
print(code)