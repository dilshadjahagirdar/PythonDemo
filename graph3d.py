from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure()
chart = fig.add_subplot(1,1,1,projection = '3d')
x,y,z =[1,2,3,4,5,6,7,8],[2,5,3,8,9,5,6,1],[3,6,2,7,5,4,5,6]
xx,yy,zz =[-1,-2,-3,-4,-5,-6,-7,-8],[-2,5,-3,8,-9,5,-6,1],[3,-6,2,-7,5,-4,5,-6]
#chart.plot_wireframe(x,y,z)
#chart.scatter(x,y,z,color="red",marker="o")
#chart.scatter(xx,yy,zz,color="blue",marker='^')
dx = np.ones(10)
dy = np.ones(10)
dz = [1,2,3,4,5,6,7,8,9,10]

chart.bar3d(x,y,z,dx,dy,dz,color="cyan")

chart.set_xlabel("x axis")
chart.set_ylabel("y axis")
chart.set_zlabel("z axis")
plt.show()
