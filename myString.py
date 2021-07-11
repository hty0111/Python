#可索引，不可修改，可以通过切片裁剪
str = 'hty'
print(str.capitalize())             #大写首字母

str = 'HTY'
print(str.casefold())               #全部小写
print(str.center(10))               #将字符串放到中心
print(str.count('H',0,2))           #计算字符出现次数
print(str.endswith('Y',0,3))        #判断结尾
print(str.swapcase())               #翻转大小写

str = 'h\tt\ty'
print(str.expandtabs())             #将\t以八位空格输出
print(str.find('y'))                #找到字符返回下标

str = 'hty'
print(str.join('123'))              #将字符串插入目标
print(str.partition('t'))           #以目标分割成元组
print(str.replace('hty', 'HTY', 4)) #替换

str = '   hty'
print(str.lstrip())                 #去除左空格
str.rstrip()
str.strip()

str = 'h t y'
print(str.split())                  #type为列表           
print(str.translate(str.maketrans(' ', '1')))

print(str.join(['h', 't', 'y']))    #'hty'

str.title()                         #每个单词的首字母大写
str.upper()                         #大写
str.lower()                         #小写
str = "hty" + '' + 'zxa'            #拼接
