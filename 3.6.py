from math import *
#part A
print('a')
def trapezint1(f,a,b):
    return ((b-a)/2)*(f(a)+f(b))
def f(x):
    return x
print (f'{trapezint1(f,a=1,b=5)} approximation')

#part B
print('b')
def test(f,a,b):
    return trapezint1(f,a,b)
print (f'{test(f=cos,a=0,b=pi)} cos error 0')

def test2(f,a,b):
    return trapezint1(f,a,b)
print (f'{test2 (f=sin,a=0,b=pi)} sin error 2')

def test3(f,a,b):
    return trapezint1(f,a,b)
print (f'{test3 (f=sin,a=0,b=pi/2)} sin error 0.215')

#Part C
print('c')
def trapezint2(f,a,b):
    return ((b-a)/4)*(f(a)+2*f((b-a)/2)+f(b))
def test(f,a,b):
    return trapezint2(f,a,b)
print (f'{test(f=cos,a=0,b=pi)} cos error 0')

def test2(f,a,b):
    return trapezint2(f,a,b)
print (f'{test2 (f=sin,a=0,b=pi)} sin error 0.43')

def test3(f,a,b):
    return trapezint2(f,a,b)
print (f'{test3 (f=sin,a=0,b=pi/2)} sin error 0.05')

#Part D
print('d')
def trapezint3(f,a,b,n):
    h=((b-a)/n)
    s=0
    x=a
    for i in range(n):
        x = a + (i) * h
        x_1 = a + (i+1) * h
        s+=(1/2)*h*(f(x)+f(x_1))
        #print(s)
        #print('h,i,x,x+i(h),f(x),f(x+i*h)=', h, i, x, x + i * h, f(x), f(x + (i + 1) * h))
    return s

def test4(f, a, b, n=100):
    return trapezint3(f,a,b,n)
print(test4(f=cos, a=0, b=pi, n=100))

def test5(f,a,b,n=10):
    return trapezint3(f,a,b,n)
print (test5 (f=sin,a=0,b=pi,n=100))

def test6(f,a,b,n=100):
    return trapezint3(f,a,b,n)
print (test6 (f=sin,a=0,b=pi/2,n=2))

#Part E
print ('e')

def test_trapezint(f,a,b,n):
    return trapezint3(f,a,b,n)
print(f'(sqrt(2)*pi)/2+(sqrt(2)*pi)/2+pi/8=',{test_trapezint(sin,0,pi/2,2)})
