import math
y=[i/100 for i in range(0,325,25)]
y.append(1.05)
m=[]
for i in y:
	def func(x,k):
	    return 1800/x-1-math.exp(0.02*(100+0.066*x-(25+0.081*(1800-x)))+0.5*(k-2.25))
	a=1
	b=1800
	fa=func(a,i)
	fb=func(b,i)
	while a<=b:
	    x0=(a+b)/2
	    fx0=func(x0,i)   
	    if abs(fx0)<10e-6:
	        #print('x0:',x0,fx0,'<10e-6')
	        #print(x0,'二分法解方程')
	        #print(int(x0))
	        m.append(int(x0+0.5))
	        #m.append(x0)
	        break
	    if fa*fx0<0:
	        b=x0
	        fb=fx0
	        #print('解在左侧,a:',a,'  b:',b,'  x0:',x0)
	    elif fb*fx0<0:
	        a=x0
	        fa=fx0
	        #print('解在右侧,a:',a,'  b:',b,'  x0:',x0)
#print(y)
print(m)
n=[]
for index, item in enumerate(y):
	n.append(item*m[index]+2.25*(1800-m[index])+350+0.75*m[index]-4050)
print(y)
print(n)
#import matplotlib.pyplot as plt
#plt.plot(y, n, ls="-", lw=2, label="plot figure")
#plt.legend()
#plt.grid(c='r')
#plt.show()