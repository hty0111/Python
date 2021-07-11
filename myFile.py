#with 语句可以省略close，让python自动判断是否关闭
with open('myFile.txt') as f:   #默认为只读方式打开
    for line in f:              #自动按行输出
        print(line, end='')     #文件末尾自带换行符   
    print(f.tell())             #文件指针已在末尾
    print(f.seek(3, 0))         #从0（头）开始重新定位，偏移量为3
    print(f.tell())             #当前指针位置
    print(f.read(1))            #按字节输出，当前指向'T'
    print()
with open('myFile.txt') as f:
    contents = f.read()         #read会在文件到达末尾时读一个空字符串
    print(contents.rstrip())    #去掉空字符串
    f.seek(0, 0)                #指向文件开头
    lines = f.readlines()       #按行读取，存为列表
    print(lines)                
    for line in lines:
        print(line.rstrip())    #去掉换行符
with open('myFile.txt','r+') as f:
    f.seek(0, 2)                #指向文件结尾
    f.write("NB\n")             #需自行换行
with open('myFile.txt','a') as f:   #附加模式直接在文件末尾写入
    f.write('bad')