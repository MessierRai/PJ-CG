#-*- coding: utf-8 -*-
# Aula sobre animacao - Exercicio em sala

from math import cos
from math import pi
from math import sin
from math import tan
import timeit
#import numpy
import ctypes
import random
from sys import argv
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

global esqdir
global cimabaixo
global aux1
global aux2
global angulo


esqdir = 0
cimabaixo = 0
aux1 = 0
aux2 = 0
angulo = 30
grau = 0
translate_x = 0
translate_y = 0
translate_z = 0
rotacao_x = 0
rotacao_y = 0
rotacao_z = 0
cor_R = 0
cor_G = 0
cor_B = 0




def eixos():      #desenha os eixos x e y do plano cartesiano.
    glColor3f(.9, .1, .1) # cor RGB  eixo X
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformacoes no objeto
    glRotatef(90, 0.0, 1.0, 0.0)     #Rotacao do objeto
    glTranslate( 0.0, 0.0, -2.0)  #Transtacao do objeto
    glutSolidCylinder(0.01, 4.0, 4, 10)
    glPopMatrix()

    glColor3f(.1, .1, .9) # cor RGB  eixo Y
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformacoes no objeto
    glRotatef(90, 1.0, 0.0, 0.0)     #Rotacao do objeto
    glTranslate( 0.0, 0.0, -2.0)  #Transtacao do objeto
    glutSolidCylinder(0.01, 4.0, 4, 10)
    glPopMatrix()

    glColor3f(.1, .9, .1) # cor RGB  eixo z
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformacoes no objeto
    #glRotatef(90, 1.0, 0.0, 0.0)     #Rotacao do objeto
    glTranslate( 0.0, 0.0, -2.0)  #Transtacao do objeto
    glutSolidCylinder(0.01, 4.0, 4, 10)
    glPopMatrix()

def calca():
    #Perna esquerda
    glColor3f(0, 0, 1)
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformacoes no objeto
    glTranslate(0.12, 0.25, 0)  #Transtacao do objeto
    glRotatef(-5, 0.0, 0.5, 0.5)     #Rotaçao do objeto
    glScalef(0.4, 1.9, 0.1)
    glutSolidCube(0.5)
    glPopMatrix()

    #Perna direita
    glColor3f(0, 0, 1)
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformacoes no objeto
    glTranslate(0.40, 0.25, 0)  #Transtacao do objeto
    glRotatef(5, 0.0, 0.5, 0.5)     #Rotaçao do objeto
    glScalef(0.4, 1.9, 0.1)
    glutSolidCube(0.5)
    glPopMatrix()

    #Base da calça
    glColor3f(0, 0, 1)
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformacoes no objeto
    glTranslate(0.25, 0.5, 0)  #Transtacao do objeto
    glRotatef(90, 0.0, 0.0, 1.0)     #Rotaçao do objeto
    glScalef(0.5, 0.40, 0)
    glutSolidCube(1.0)
    glPopMatrix()


    #boca da calça
    glColor3f(0, 0, 0)
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformacoes no objeto
    glTranslate(0.25, 0.7, 0.0)  #Transtacao do objeto
    glRotatef(90, 1.0, 0.0, 0.0)     #Rotaçao do objeto
    glScalef(1, 0.2, 1)
    glutSolidCylinder(0.25, 0.1, 10, 10)
    glPopMatrix()

def piso():
    glColor3f(1, 1, 1) # cor RGB  eixo z
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformacoes no objeto
    glTranslate(0.0, -1.0, 0.0)  #Transtacao do objeto
    glRotatef(180, 0.0, 0.0, 1.0)     #Rotacao do objeto
    glScalef(1.5, .04, 1)
    glutSolidCube(3)
    glPopMatrix()


def desenho():
    global grau_helice
    global grau_ventilador
    global sentido_ventilador

    eixos()
   # piso()

   
    glColor3f(1,0 ,1)
    glPushMatrix()
    glTranslate(0.1,1.0,0.0)
    calca()
    glPopMatrix()


    glColor3f(0, 1, 1)
    glPushMatrix()
    glTranslate(0.1,1.0,0.2)
    calca()
    glPopMatrix()


    glColor3f(1, 1, 0)
    glPushMatrix()
    glTranslate(0.1,1.0,0.4)
    calca()
    glPopMatrix()


    glColor3f(1, 0, 1)
    glPushMatrix()
    glTranslate(0.1,1.0,0.6)
    calca()
    glPopMatrix()
    

    # Opcoes de objetos:
    #glutWireSphere( 0.5,50,50)
    #glutSolidSphere(0.5,100,100)
    #glutWireTorus(0.3,0.9,100,10)   # rosquinha
    # glutSoliube(0.5)
    #glutSolidCidTorus(0.5,0.5,100,100)
    # glutWireIcosahedron(1)
    #glutSolidIcosahedron(1)
    #glutWireDodecahedron(1)
    # glutSolidDodecahedron(0.5)
    #glutWireCone(0.5, 1.0, 40, 20)   # piramides e cones  (tamanho da base, altura, lados , camadas )
    #glutSolidCone(0.5, 1.0, 40, 40)
    # glutWireCube(0.3,0.5)
    #glutSolidClinder(0.5, 0.1, 30, 30)


    #deixando as coisas transparentes
    # glPushMatrix()
    # glEnable (GL_BLEND);
    # glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
    # glColor4f(.7, .7, .7, .4)
    #camisa(translate_x, translate_y, translate_z, rotacao_x, rotacao_y, rotacao_z, cor_R, cor_G, cor_B)
    # camisa(0, 0, 0, 0, 0, 0.6, 0, 0, 0)
    # camisa(0, 0, 0.2, 0, 0, 0.6, 1, 0, 0)
    # camisa(0, 0, 0.4, 0, 0, 0.6, 0, 1, 0)
    # camisa(0, 0, 0.6, 0, 0, 1.5, 0, 0, 1)
    # camisa(0, 0, 0.8, 0, 0, 1.5, 1, 1, 0)
    # camisa(0, 0, 1, 0, 0, 1.5, 0, 1, 1)
    # #cabo(translate_x, transl-at8_y, translate_z, rotacao_z)
    # cabide(0, -0.25, 0.0)
    # cabide(0, -0.25, 0.2)
    # cabide(0, -0.25, 0.4)
    # cabide(0, -0.25, 0.6)
    # cabide(0, -0.25, 0.8)
    # cabide(0, -0.25, 1)
    # cabo(0, 0.5, -0.4)
    # glColor4f(.7, .7, .7, .3)
    # glDisable(GL_BLEND)
    # glPopMatrix()


def iluminacao_da_cena():
    global aux1
    luzAmbiente=[0.2,0.2,0.2,1.0]
    luzDifusa=[0.7,0.7,0.7,1.0]  # ; // "cor"
    luzEspecular = [1.0, 1.0, 1.0, 1.0]  #;// "brilho"
    posicaoLuz=[aux1, 50.0, 50.0, 1.0]

    #Capacidade de brilho do material
    especularidade=[1.0,1.0,1.0,1.0]
    especMaterial = 60;

    # Especifica que a cor de fundo da janela sera preta
    glClearColor(0.0, 0.0, 0.0, 1.0)

    # Habilita o modelo de colorizacao de Gouraud
    glShadeModel(GL_SMOOTH)

    #  Define a refletancia do material
    glMaterialfv(GL_FRONT_AND_BACK,GL_SPECULAR, especularidade)
    #  Define a concentracao do brilho
    glMateriali(GL_FRONT,GL_SHININESS,especMaterial)

    # Ativa o uso da luz ambiente
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, luzAmbiente)

    # Define os parametros da luz de numero 0
    glLightfv(GL_LIGHT0, GL_AMBIENT, luzAmbiente)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, luzDifusa )
    glLightfv(GL_LIGHT0, GL_SPECULAR, luzEspecular )
    glLightfv(GL_LIGHT0, GL_POSITION, posicaoLuz )

    # Habilita a definicao da cor do material a partir da cor corrente
    glEnable(GL_COLOR_MATERIAL)
    # Habilita o uso de iluminacao
    glEnable(GL_LIGHTING)
    # Habilita a luz de numero 0
    glEnable(GL_LIGHT0)
    # Habilita o depth-buffering
    glEnable(GL_DEPTH_TEST)


def tela():
    global angulo

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Limpar a tela
    glClearColor(1.0, 1.0, 1.0, 1.0) # Limpa a janela com a cor especificada
    glMatrixMode(GL_PROJECTION) # Muda a matriz de projecao
    glLoadIdentity()# carrega a matriz identidade

    #gluPerspective(angulo, aspecto , near, far )
    #  angulo = angulo em graus na direcao y.
    #  aspecto = deformacao da janela. normalmente e a razao entre a largura e altura
    #  near = a menor distancia desenhada
    #  far = a maior distancia para que o objeto seja desenhado
    gluPerspective(angulo,1,0.1,500) # Especifica a projecao perspectiva

    #glOrtho(left,right,bottom, top, near, far)
    #  left,right,bottom, top = limites da projecao
    #  near = a menor distancia desenhada
    #  far = a maior distancia para que o objeto seja desenhado
    #glOrtho(-5,5,-5,5,0.1,500) # Especifica a projecao paralela ortogonal

    glMatrixMode(GL_MODELVIEW) # Especifica sistema de coordenadas do modelo
    glLoadIdentity() # Inicializa sistema de coordenadas do modelo

    #gluLookAt(eyex, eyey, eyez, alvox, alvoy, alvoz, upx, upy, upz)
    #    eyex, eyey, eyez = posicao da camera
    #    alvox, alvoy, alvoz = coordenada para onde a camera olha.
    #    upx, upy, upz = indica a posicao vertical da camera.
    gluLookAt(sin(esqdir) * 10, 0 + cimabaixo ,cos(esqdir) * 10, aux1,aux2,0, 0,1,0) # Especifica posicao do observador e do alvo
    #iluminacao_da_cena()
    glEnable(GL_DEPTH_TEST) # verifica os pixels que devem ser plotados no desenho 3d

    desenho()
    glFlush()                    # Aplica o desenho

# Funcao callback chamada para gerenciar eventos de teclas normais
def Teclado (tecla, x, y):
    global aux1
    global aux2


    print("*** Tratamento de teclas comuns")
    print(">>> Tecla: ",tecla)

    if tecla==chr(27): # ESC ?
        sys.exit(0)

    if tecla == b'a':  # A
        aux1 = aux1 - 0.1
        print ("aux1 = ", aux1 )

    if tecla == b's': # S
        aux1 = aux1 + 0.1
        print ("aux1 = ", aux1 )

    if tecla == b'w': # W
        aux2 = aux2 + 0.1
        print ("aux2 = ", aux2 )

    if tecla == b'z': # Z
        aux2 = aux2 - 0.1
        print ("aux2 = ", aux2 )

    # if tecla == b'l': # L
    #     if (liga_ventilador == 0):
    #         liga_ventilador = 1
    #     else:
    #         liga_ventilador = 0
    #     print ("Pressionou o interruptor do ventilador" )

    tela()
    glutPostRedisplay()

# Funcao callback chamada para gerenciar eventos de teclas especiais
def TeclasEspeciais (tecla, x, y):
    global esqdir
    global cimabaixo
    #print("*** Tratamento de teclas especiais")
    #print ("tecla: ", tecla)
    if tecla == GLUT_KEY_F1:
        print(">>> Tecla F1 pressionada")
    elif tecla == GLUT_KEY_F2:
        print(">>> Tecla F2 pressionada")
    elif tecla == GLUT_KEY_F3:
        print(">>> Tecla F3 pressionada")
    elif tecla == GLUT_KEY_LEFT:
        esqdir = esqdir - 0.1
    elif tecla == GLUT_KEY_RIGHT:
        esqdir = esqdir + 0.1
    elif tecla == GLUT_KEY_UP:
        cimabaixo = cimabaixo + 0.1
    elif tecla == GLUT_KEY_DOWN:
        cimabaixo = cimabaixo - 0.1
    else:
        print ("Apertou... " , tecla)
    tela()
    glutPostRedisplay()

# Funcao callback chamada para gerenciar eventos do mouse
def ControleMouse(button, state, x, y):
    global angulo
    if (button == GLUT_LEFT_BUTTON):
        if (state == GLUT_DOWN):
            if (angulo >= 10):
                angulo -= 2

    if (button == GLUT_RIGHT_BUTTON):
        if (state == GLUT_DOWN):   # Zoom-out
            if (angulo <= 130):
                angulo += 2
    tela()
    glutPostRedisplay()



glutInit(argv)
glutInitDisplayMode(GLUT_RGBA | GLUT_DEPTH)
glutInitWindowSize(600,600)
glutCreateWindow(b"Aula10 - Animacao")
glutDisplayFunc(tela)
glutMouseFunc(ControleMouse)
glutKeyboardFunc (Teclado)
glutSpecialFunc (TeclasEspeciais)
glutMainLoop()  # Inicia o laco de eventos da GLUT
