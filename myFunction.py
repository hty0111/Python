#函数文档
def FirstFunction(str):
    '这是一个函数文档'
    print('The str is', str )
FirstFunction('HTY')

#默认参数
def SomeoneSay(name='HTY ',words='NB'):
    print(name + words)
SomeoneSay()
SomeoneSay('ZXA ')

#可变长度参数
def test(*params, exp):
    print('Lenth of params:', len(params), exp)
    print('The second param is:', params[1])
test(0,1,2,3,4,5, exp=6)

#传字典，**user_info接受任意数量的键值对
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('albert', 'einstin',
                            location='princeton',
                            field='physics')
print(user_profile)

#返回值多类型
def back():
    return 1, 'hty', 3.14
print(back())

#全局变量和局部变量
count = 10
def alter():
    count = 5
    print(count)
alter()
print(count)

count = 10
def glob():
    global count
    count = 20
    print(count)
glob()
print(count)

#嵌套函数
def fun1():
    def fun2():
        print('Fun2')
    fun2()
    print('Fun1')
fun1()

#闭包：内部函数引用了外部函数的变量（非全局变量）
def funx(x):
    def funy():
        return x
    return funy()
print(funx(5))

def funx(x):
    def funy(y):
        return x*y
    return funy
print(funx(5)(8))

def funx():
    x = [5]
    def funy():
        x[0] *= x[0]
        return x[0]
    return funy()
print(funx())

def funx():
    x = 5
    def funy():
        nonlocal x
        x *= x
        return x
    return funy()
print(funx())

#匿名函数
g = lambda x : 2 * x + 1
print(g(5))

#过滤器
print(list(filter( lambda x : x % 2, range(10) )))

#映射
print(list(map( lambda x : x * 2, range(10) )))
a, b, c = map( int, input().split() )
print(a,b,c)
