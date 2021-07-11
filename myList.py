#可索引，可切片，可修改
plist = list(range(1,4))            #前闭后开
plist.append(4)                     #加元素
plist.extend([5, 6])                #加列表
plist.insert(0, 0)                  #插入
plist.remove(6)                     #移除
del plist[0]                        #删除
print(plist.pop())                  #弹栈
print(plist[1:3] + plist[2:3])      #拼接
print(plist.count(3))               #计算出现次数
print(plist.index(3,1,5))           #找下标                      
plist.reverse()                     #对原序列翻转
plist.sort()                        #对原序列升序
plist.sort(reverse=True)            #对原序列降序
print(sorted(plist))                #拷贝新序列
plist.reverse()                     #翻转原序列
print(list(reversed(plist)))        #拷贝新序列
print(list(enumerate(plist)))

#改变类型
a = ['1', '2', '3']
b = []
for x in a:
    b.append(int(x))
c = [int(x) for x in a]             #列标解析
d = map(int, a)
