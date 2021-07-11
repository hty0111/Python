#0作为除数
a,b = map(int, input().split())
try:
    answer = a/b
except ZeroDivisionError:
    print("Cannot divide by 0!")
else:
    print(answer)

#找不到文件
try:
    f = open("hty.txt")
except FileNotFoundError:
    print("File dosen't exist!")
else:
    f.close()