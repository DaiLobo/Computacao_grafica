from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import pi, cos, sin


n1 = 50
n2 = 50
r = 2
a = 0


def f(i, j):
	theta = ((pi*i)/(n1-1))-(pi/2)
	phi = 2*pi*j/(n2-1)
	x = r*cos(theta)*cos(phi)
	y = r*sin(theta)
	z = r*cos(theta)*sin(phi)

	return x, y**2, z


def mesh():
	glPushMatrix()
	glRotatef(a,0.0,1.0,0.0) #girar em torno do eixo y

	for i in range(0, n1):
		glBegin(GL_QUAD_STRIP)
		
		for j in range(0, n2):
			glColor3f(0.94, 0.76, 0.18)
			x, y, z = f(i, j)
			glVertex3f(x, y, z)

			glColor3f(0.94, 0.69, 0.22)
			x, y, z = f(i+1, j+1)
			glVertex3f(x, y, z)

		glEnd()

	glPopMatrix()


def desenha():
	global a
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	mesh()
	a+=0.3
	glutSwapBuffers()
  
def timer(i):
	glutPostRedisplay()
	glutTimerFunc(10,timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(1024,1024)
glutCreateWindow("Sólido de revolução")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0,0,0,1)
gluPerspective(45,800.0/600.0,0.1,100.0)
glTranslatef(0.0, -1.5, -10)
glutTimerFunc(10,timer,1)
glutMainLoop()