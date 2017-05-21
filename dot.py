import turtle
t=turtle.Pen()

dot_distance = 10
width = 30
height = 60
t.penup()
for i in range (height):
	for i in range (width):
		t.dot()
		t.forward(dot_distance)
	t.back(dot_distance*width)
	t.right(90)
	t.forward(dot_distance)
	t.left(90)

