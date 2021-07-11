import sympy as sp

x = sp.Symbol("x")
f = x**2 - 2*x + 1
x0 = 0
df = sp.diff(f, x)          #一阶导表达式
ddf = sp.diff(f, x, 2)      #二阶导表达式

int = sp.integrate(f, (x, 0, 1))    #积分 #1/3
total = sp.summation(f, (x, 0, 2))  #求和 #2
fx0 = f.evalf(subs={x: x0})         #0
dfx0 = df.evalf(subs={x: x0})       #-2
ddfx0 = ddf.evalf(subs={x: x0})     #2


