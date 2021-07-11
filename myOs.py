import os
os.getcwd()                     #当前工作目录
os.chdir('')                    #改变工作目录
os.listdir()                    #列举当前目录文件
os.mkdir('')                    #创建新目录（文件夹）
os.makedirs('')                 #创建多层目录
os.remove('')                   #删除文件
os.rmdir('')                    #删除目录
os.removedirs('')               #删除多层目录
os.rename()                     #重命名
os.system()                     #运行shell命令

os.path.basename()              #返回文件名
os.path.dirname()               #返回路径
os.path.join('C:\\', 'A', 'B')  #合成路径
os.path.split()                 #分离路径和文件名
os.path.splitext()              #分离文件名和扩展名
os.path.getsize()               #以字节为单位返回大小
os.path.getatime()              #访问时间
os.path.getctime()              #创建时间
os.path.getmtime()              #修改时间

os.path.exists()
os.path.isabs()                 #判断是否为绝对路径
os.path.isdir()                 #判断是否为目录
os.path.isfile()                #判断是否为文件
os.path.islink()                #判断是否为符号链接（快捷方式）
os.path.ismount()               #判断是否为挂载点（C盘、D盘）
os.path.samefile()              #判断是否指向同一个文件