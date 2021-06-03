from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math
import sys


#https://www.opengl.org/wiki/Calculating_a_Surface_Normal
#Begin Function CalculateSurfaceNormal (Input Triangle) Returns Vector
#  Set Vector U to (Triangle.p2 minus Triangle.p1)
#  Set Vector V to (Triangle.p3 minus Triangle.p1)
#  Set Normal.x to (multiply U.y by V.z) minus (multiply U.z by V.y)
#  Set Normal.y to (multiply U.z by V.x) minus (multiply U.x by V.z)
#  Set Normal.z to (multiply U.x by V.y) minus (multiply U.y by V.x)
#  Returning Normal
#End Function

def calculaNormalFace(v0, v1, v2):
    x = 0
    y = 1
    z = 2
    
    U = ( v2[x]-v0[x], v2[y]-v0[y], v2[z]-v0[z] )
    V = ( v1[x]-v0[x], v1[y]-v0[y], v1[z]-v0[z] )
    N = ( (U[y]*V[z]-U[z]*V[y]),(U[z]*V[x]-U[x]*V[z]),(U[x]*V[y]-U[y]*V[x]))
    NLength = math.sqrt(N[x]*N[x]+N[y]*N[y]+N[z]*N[z]) #modulo do vetor, tamanho do vetor, teorema de pitagoras
    return ( N[x]/NLength, N[y]/NLength, N[z]/NLength) #normaliza o vetor da normal

def piramide_tronco():

    raio = 2
    raio2 = 1
    N = 5 #num de faces
    H = 2 #altura
    pontosBase = []
    pontosBase2 = []
    angulo = (2*math.pi)/N

    glPushMatrix()

    #Base maior
    glBegin(GL_POLYGON) #desenha um pentagono com preenchimento
    for i in range(0, N):
        x = raio * math.cos(i*angulo)
        y = raio * math.sin(i*angulo)
        pontosBase += [ (x, y) ]
        glVertex3f(x, y, 0.0)

    a = (pontosBase[0][0], pontosBase[0][1], 0.0)
    b = (pontosBase[1][0], pontosBase[1][1], 0.0)
    c = (pontosBase[2][0], pontosBase[2][1], 0.0)

    glNormal3fv(calculaNormalFace(a, b, c))

    glEnd()

    #Base menor
    glBegin(GL_POLYGON) #desenha um pentagono com preenchimento
    for i in range(0, N):
        x = raio2 * math.cos(i*angulo)
        y = raio2 * math.sin(i*angulo)
        pontosBase2 += [ (x, y) ]
        glVertex3f(x, y, H)

    a = (pontosBase2[0][0], pontosBase2[0][1], H)
    b = (pontosBase2[1][0], pontosBase2[1][1], H)
    c = (pontosBase2[2][0], pontosBase2[2][1], H)
    glNormal3fv(calculaNormalFace(a, b, c))

    glEnd()

    #LATERAL
    glBegin(GL_QUAD_STRIP) #a cada 6 vertices formam-se 2 retangulos
    for i in range(0, N):

        a = (pontosBase2[i][0],pontosBase2[i][1],H)
        b = (pontosBase2[(i+1)%N][0],pontosBase2[(i+1)%N][1],H)
        c = (pontosBase[i][0],pontosBase[i][1],0.0)
        d = (pontosBase[(i+1)%N][0],pontosBase[(i+1)%N][1],0.0)

        glNormal3fv(calculaNormalFace(a, b, c))
        glVertex3fv(a)
        glVertex3fv(b)
        
        glVertex3fv(c)
        glVertex3fv(d)

    glEnd()

    glPopMatrix()
    
def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2, 1, 3, 0)
    piramide_tronco()
    glutSwapBuffers()

def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50, timer, 1)

def reshape(w,h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45,float(w)/float(h), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # Camera Virtual
    #          onde    Pra onde 
    gluLookAt( 10,0,0, 0,0,0,     0,1,0 )

def init():
    mat_ambient = (0.4, 0.0, 0.0, 1.0)
    mat_diffuse = (1.0, 0.0, 0.0, 1.0)
    mat_specular = (1.0, 0.5, 0.5, 1.0)
    mat_shininess = (50,)
    light_position = (10, 0, 0)
    glClearColor(0.0, 0.0, 0.0, 0.0)
#    glShadeModel(GL_FLAT)
    glShadeModel(GL_SMOOTH)

    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_MULTISAMPLE)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
    glutInitWindowSize(800, 600)
    glutCreateWindow("Tronco de Piramide")
    glutReshapeFunc(reshape)
    glutDisplayFunc(display)
    glutTimerFunc(50, timer, 1)
    init()
    glutMainLoop()

main()
