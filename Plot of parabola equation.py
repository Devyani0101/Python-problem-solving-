from pylab import*

import numpy as np

def f(x,y):

 return x**2+y**2

x=np.linspace(-6,6,30)

y=np.linspace(-6,6,30)

X,Y=np.meshgrid(x,y)

Z=f(X,Y)

ax=axes(projection='3d')

ax.plot_surface(X,Y,Z)

xlabel('x-axis')

ylabel('y-axis')

title('Surface Plot')

show()
