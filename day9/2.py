
import numpy as np
import matplotlib.pyplot as plt
'''定义x、y散点坐标'''

x = [1,1.5,2,2.5,3,3.5,4,4.5]
x = np.array(x)
print('x is :\n',x)
num = [174,236,305,334,349,351,342,323]
y = np.array(num)
print('y is :\n',y)
#用3次多项式拟合
f1 = np.polyfit(x, y, 3)
print('f1 is :\n',f1)
p1 = np.poly1d(f1)

plot(x,y,color="red",label="origin",linewidth=2)
plot(x,yfit,"b--",label="fit",linewidth=2)
legend(loc="upper right",frameon=False)
annotate('R=110.123575696',xy=(100,10))
show()rint('p1 is :\n',p1)



pylab.show()