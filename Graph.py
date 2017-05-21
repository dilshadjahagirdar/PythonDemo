import matplotlib.pyplot as pt
fig = pt.figure()
rect = fig.patch
rect.set_facecolor("red")
graph1 = fig.add_subplot(2,2,1,axisbg='black')
x = [0,7,8,10]
y = [0,13,2,8]
x1 = [0,8,9,11]
y1= [0,1,9,4]
x3 = [0,4,6,8]
y3 = [0,5,8,2]

graph1.plot(x,y,"white",linewidth='4.0')
graph1.tick_params(axis='x' ,color = 'yellow')
graph1.tick_params(axis='y',color='white')
graph1.spines["top"].set_color("w")
graph1.spines["bottom"].set_color("w")
graph1.spines["left"].set_color("w")
graph1.spines["right"].set_color("w")
graph1.set_title("random",color="white")


graph2 = fig.add_subplot(2,2,2,axisbg='black')

graph2.plot(x3,y3,"white",linewidth='4.0')
graph2.tick_params(axis='x' ,color = 'yellow')
graph2.tick_params(axis='y',color='white')
graph2.spines["top"].set_color("w")
graph2.spines["bottom"].set_color("w")
graph2.spines["left"].set_color("w")
graph2.spines["right"].set_color("w")
graph2.set_title("random",color="white")

graph3 = fig.add_subplot(2,1,2,axisbg='black')

graph3.plot(x1,y1,"white",linewidth='4.0')
graph3.tick_params(axis='x' ,color = 'yellow')
graph3.tick_params(axis='y',color='white')
graph3.spines["top"].set_color("w")
graph3.spines["bottom"].set_color("w")
graph3.spines["left"].set_color("w")
graph3.spines["right"].set_color("w")
graph3.set_title("random",color="white")





pt.show()
