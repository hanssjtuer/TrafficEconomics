import math
y=[i for i in range(1500,2600,100)]
m=[]
for i in y:
	def func(x,k):
	    return k/x-1-math.exp(0.02*(100+0.066*x-(25+0.081*(k-x)))+0.5*(1.25-2.25))
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
print(y)
print(m)
n=[]
q=[]
for index, item in enumerate(y):
	#n.append(item*m[index]+2.25*(1800-m[index])+350+0.75*m[index]-4050)
	n.append(item-m[index])
	q.append(1.25*m[index]+2.25*n[index]+350+0.75*m[index]-item*2.25)
#print(y)
print(n)
print(q)
#import matplotlib.pyplot as plt
#plt.plot(y, n, ls="-", lw=2, label="plot figure")
#plt.legend()
#plt.grid(c='r')
#plt.show()