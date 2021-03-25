from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math

a = 0 #vai controlar o angulo da piramide em torno do eixo do y

cores = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) )

def piramide_tronco():
    raio = 2
    raio2 = 1
    N = 5 #num de faces
    H = 2 #altura
    pontosBase = []
    pontosBase2 = []
    angulo = (2*math.pi)/N

    glPushMatrix() #guarda o contexto, faz o desenho q tiver q fazer
    glTranslatef(0,-2,0)
    glRotatef(a,0.0,1.0,0.0) #angulo em graus
    glRotatef(-110,1.0,0.0,0.0) #inclinar p ver a base
    glColor3fv(cores[0]) #cor da base

    # Base maior
    glBegin(GL_POLYGON) #desenha um pentagono com preenchimento
    for i in range(0,N):
        x = raio * math.cos(i*angulo)
        y = raio * math.sin(i*angulo)
        pontosBase += [ (x,y) ]
        glVertex3f(x,y,0.0)
    glEnd()

    # Base menor
    glBegin(GL_POLYGON) #desenha um pentagono com preenchimento
    for i in range(0,N):
        x = raio2 * math.cos(i*angulo)
        y = raio2 * math.sin(i*angulo)
        pontosBase2 += [ (x,y) ]
        glVertex3f(x,y,H)
    glEnd()

    # LATERAL
    glBegin(GL_QUAD_STRIP) #a cada 6 vertices formam-se 2 retangulos
    for i in range(0,N):
        glColor3fv(cores[(i+1)%len(cores)]) #p cada face ser uma cor diferente
        glVertex3f(pontosBase2[i][0],pontosBase2[i][1],H)
        glVertex3f(pontosBase2[(i+1)%N][0],pontosBase2[(i+1)%N][1],H)
        
        glVertex3f(pontosBase[i][0],pontosBase[i][1],0.0)
        glVertex3f(pontosBase[(i+1)%N][0],pontosBase[(i+1)%N][1],0.0)
    glEnd()

    glPopMatrix()


def desenha():
    global a #precisa colocar aqui q é variavel global
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    piramide_tronco()
    a+=1 #como estou modificando o valor
    glutSwapBuffers()
  
def timer(i): #fica chamando de novo o redisplay da função de desenho
    glutPostRedisplay()
    glutTimerFunc(10,timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("TRONCO DE PIRAMIDE")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0,0,0,1)
gluPerspective(45,800.0/600.0,0.1,100.0)
glTranslatef(0.0,0.0,-10)
glutTimerFunc(10,timer,1) #registrar função de timer
glutMainLoop()
