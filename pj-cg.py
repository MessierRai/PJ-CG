#coding: latin1


from math import cos
from math import pi
from math import sin
import numpy
import ctypes
import random
from sys import argv
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.GLE import *
from PIL import Image, ImageFilter

global esqdir
global cimabaixo
global aux1
global aux2
global angulo
global distanciamax
global aux
global estadoluz0, estadoluz1, estadoluz2
global abertoPorta
global temp
global angulo1

global n, faces, v

esqdir = 0
cimabaixo = 0
aux1 = 0
aux2 = 0
aux3 = 0
aux4 = 0
angulo = 60
distanciamax = 100
aux = 0 
estadoluz0 = 1
estadoluz1 = 0
estadoluz2 = 0
abertoPorta = 0
temp = 0
angulo1 = 0

def eixos():      #desenha os eixos x e y do plano cartesiano.
    glColor3f(.9, .1, .1) # cor RGB  eixo X
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    glRotatef(90, 0.0, 1.0, 0.0)     #Rotaçao do objeto
    glTranslate( 0.0, 0.0, -2.0)  #Transtaçao do objeto
    glutSolidCylinder(0.01, 4.0, 4, 10)
    glPopMatrix()

    glColor3f(.1, .1, .9) # cor RGB  eixo Y
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    glRotatef(90, 1.0, 0.0, 0.0)     #Rotaçao do objeto
    glTranslate( 0.0, 0.0, -2.0)  #Transtaçao do objeto
    glutSolidCylinder(0.01, 4.0, 4, 10)
    glPopMatrix()

    glColor3f(.1, .9, .1) # cor RGB  eixo z
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    #glRotatef(90, 1.0, 0.0, 0.0)     #Rotaçao do objeto
    glTranslate( 0.0, 0.0, -2.0)  #Translaçao do objeto
    glutSolidCylinder(0.01, 4.0, 4, 10)
    glPopMatrix() 

def pegadorPorta():
    glColor3f(0.6, 0.6, 0.6)
    glPushMatrix()

    glPushMatrix()
    glRotatef(-90, 1.0, 0.0, 0.0)
    glutSolidCylinder(0.03, 0.9, 7, 7)
    glPopMatrix()

    glPushMatrix()
    glTranslate(0.0, 0.2, 0.0)
    glutSolidCylinder(0.03, 0.2, 7, 7)
    glPopMatrix()

    glPushMatrix()
    glTranslate(0.0, 0.7, 0.0)
    glutSolidCylinder(0.03, 0.2, 7, 7)
    glPopMatrix()

    glPushMatrix()
    glRotatef(-90, 1.0, 0.0, 0.0)
    glTranslate(0.0, -0.2, 0.0)
    glutSolidCylinder(0.03, 0.9, 7, 7)
    glPopMatrix()

    glPopMatrix()

def read_texture(filename):
    img = Image.open(filename)
    img_data = numpy.array(list(img.getdata()), numpy.int8)
    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, img.size[0], img.size[1], 0,
                 GL_RGB, GL_UNSIGNED_BYTE, img_data)
    return texture_id

def paredesSuperior():
    glColor3f(1, 1, 1)
    glPushMatrix()
    texture_id = read_texture('img/brick14.jpg')
    glEnable(GL_TEXTURE_2D)
    glEnable(GL_TEXTURE_GEN_S)
    glEnable(GL_TEXTURE_GEN_T)
    glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, GL_OBJECT_LINEAR)
    glTexGeni(GL_T, GL_TEXTURE_GEN_MODE, GL_OBJECT_LINEAR)

    #parede superior frente
    glPushMatrix()
    glScale(2.13, 0.83, 0.05)
    glTranslate(0.0, 1.5, 0.0)
    glutSolidCube(3)
    glPopMatrix()

    #parede superior atras
    glPushMatrix()
    glTranslate(0.0, 0.0, -4.0)

    glPushMatrix()
    glScale(2.13, 0.83, 0.05)
    glTranslate(0.0, 1.5, 0.0)
    glutSolidCube(3)
    glPopMatrix()

    glPopMatrix()

    #parede superior direita
    glPushMatrix()
    glTranslate(3.2, 1.65, -2.0)
    glRotatef(90, 0.0, 1.0, 0.0)

    glPushMatrix()
    glScale(1.38, 0.83, 0.05)
    glTranslate(0.0, -0.5, 0.0)
    glutSolidCube(3)
    glPopMatrix()

    glPopMatrix()

    #parede superior esquerda
    glPushMatrix()
    glTranslate(-3.2, 1.65, -2.0)
    glRotatef(90, 0.0, 1.0, 0.0)

    glPushMatrix()
    glScale(1.38, 0.83, 0.05)
    glTranslate(0.0, -0.5, 0.0)
    glutSolidCube(3)
    glPopMatrix()

    glPopMatrix()

    glDisable(GL_TEXTURE_2D)
    glPopMatrix()

def degrau():
    glPushMatrix()
    glTranslate(0.7, 0.07, 0.0)

    glColor3f(0.7, 0.7, 0.7)
    glPushMatrix()
    glScale(0.7, 0.05, 0.2)
    glutSolidCube(2)
    glPopMatrix()

    glPopMatrix()

def unEscada():
    #centro
    glColor3f(0.7, 0.7, 0.7)
    glPushMatrix()
    glRotate(270, 1.0, 0.0, 0.0)
    glutSolidCylinder(0.2, 1.6, 20, 10)
    glPopMatrix()

    #degrau 1
    degrau()

    #degrau 2
    glPushMatrix()
    glRotatef(25, 0.0, 1.0, 0.0)
    glTranslate(0.0, 0.2, 0.0)

    degrau()

    glPopMatrix()

    #degrau 3
    glPushMatrix()
    glRotatef(50, 0.0, 1.0, 0.0)
    glTranslate(0.0, 0.4, 0.0)

    degrau()

    glPopMatrix()

    #degrau 4
    glPushMatrix()
    glRotatef(75, 0.0, 1.0, 0.0)
    glTranslate(0.0, 0.6, 0.0)

    degrau()

    glPopMatrix()

    #degrau 5
    glPushMatrix()
    glRotatef(100, 0.0, 1.0, 0.0)
    glTranslate(0.0, 0.8, 0.0)

    degrau()

    glPopMatrix()

    #degrau 6
    glPushMatrix()
    glRotatef(125, 0.0, 1.0, 0.0)
    glTranslate(0.0, 1.0, 0.0)

    degrau()

    glPopMatrix()

    #degrau 7
    glPushMatrix()
    glRotatef(150, 0.0, 1.0, 0.0)
    glTranslate(0.0, 1.2, 0.0)

    degrau()

    glPopMatrix()

    #degrau 8
    glPushMatrix()
    glRotatef(175, 0.0, 1.0, 0.0)
    glTranslate(0.0, 1.4, 0.0)

    degrau()

    glPopMatrix()

def animation():

    global aux

    glColor3f(0.0, 0.0, 0.0)
    glPushMatrix()
    glRotatef(90 - aux, 0.0, 0.0, 1.0)
    glTranslate(1.0 , 0.6, 0.0)
    glutSolidSphere(0.6, 15, 5)
    for x in numpy.arange(0.1, 0.7, 0.1):
        aux = aux + x

    glutPostRedisplay()
    glPopMatrix()

    glColor3f(1.0, 0.0, 0.0)
    glPushMatrix()
    glRotatef(90 + aux, 1.0, 0.0, 0.0)
    glTranslate(0.0 , 0.6, 1.0)
    glutSolidSphere(0.6, 15, 10)
    #for x in xrange(10, 20, 1):
    #    aux = aux + (x / 100)

    glutPostRedisplay()
    glPopMatrix()

    glColor3f(0.0, 0.0, 1.0)
    glPushMatrix()
    glRotatef(90 - aux, 0.0, 1.0, 0.0)
    glTranslate(0.0 , 0.0, 1.0)
    glutSolidSphere(0.6, 15, 10)
    #for x in np.arange(0.1, 0.2, 0.1):
    #    aux = aux + x

    glutPostRedisplay()
    glPopMatrix()

    glPushMatrix()
    glutWireSphere(1.77, 40, 20)
    glPopMatrix()

def tv():
    #corpo principal
    glColor3f(0.0, 0.0, 0.0)
    glPushMatrix()
    glScale(1.8, 1.1, 0.03)
    glutSolidCube(1)
    glPopMatrix()

    #borda esquerda
    glPushMatrix()
    glTranslate(-0.88, 0.0, 0.02)
    glScale(.04, 1.1, 0.03)
    glutSolidCube(1)
    glPopMatrix()

    #borda direita
    glPushMatrix()
    glTranslate(0.88, 0.0, 0.02)
    glScale(.04, 1.1, 0.03)
    glutSolidCube(1)
    glPopMatrix()

    #borda superior
    glPushMatrix()
    glRotatef(90, 0.0, 0.0, 1.0)
    glTranslate(-0.35, 0.0, 0.0)

    glPushMatrix()
    glTranslate(0.88, 0.0, 0.02)
    glScale(.04, 1.8, 0.03)
    glutSolidCube(1)
    glPopMatrix()

    glPopMatrix()

    #borda inferior
    glPushMatrix()
    glRotatef(90, 0.0, 0.0, 1.0)
    glTranslate(-1.41, 0.0, 0.0)

    glPushMatrix()
    glTranslate(0.88, 0.0, 0.02)
    glScale(.04, 1.8, 0.03)
    glutSolidCube(1)
    glPopMatrix()

    glPopMatrix()

    glColor3f(0.8, 0.8, 0.8)
    glPushMatrix()
    glScale(1.72, 1.02, 0.03)
    glTranslate(0.0, 0.0, 0.01)
    glutSolidCube(1)
    glPopMatrix()

def suporteGiratorio():
    global angulo1

    for t in numpy.arange(0.0, 0.4, 0.1):
        angulo1 += t

    glPushMatrix()
    glRotate(angulo1, 0.0, 1.0, 0.0)

    glPushMatrix()
    glColor3f(0.0, 0.7, 0.7)
    glTranslate(0.0, -1.7, 0.0)
    glutSolidTeapot(0.2)
    glPopMatrix()

    #suporte
    glColor3f(1.0, 0.0, 0.0)
    glPushMatrix()
    glRotatef(90, 1.0, 0.0, 0.0)
    glTranslate(0.0, 0.0, 1.84)
    glutSolidCylinder(0.3, 0.1, 20, 20)
    glPopMatrix()

    #eixo
    glPushMatrix()
    glRotatef(90, 1.0, 0.0, 0.0)
    glTranslate(0.0, 0.0, 1.84)
    glutSolidCylinder(0.09, 0.6, 20, 20)
    glPopMatrix()

    glPopMatrix()

def luminaria():
    glPushMatrix()
    
    glColor3f(1.0, 0.4, 0.0) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaÃ§oes no objeto
    glTranslate( 0.0, 0.4, 0.22)  #TranstaÃ§ao do objeto
    glRotatef(90, 1.0, 0.0, 0.0)     #RotaÃ§ao do objeto
    glutSolidCylinder(0.03, 0.2, 5, 3) #(raio, comprimento, faces, nao sei o que é)
    glPopMatrix()

    
    glColor3f(1.0, 0.4, 0.0) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaÃ§oes no objeto
    glTranslate( 0.0, 0.4, -0.22)  #TranstaÃ§ao do objeto
    glRotatef(90, 1.0, 0.0, 0.0)     #RotaÃ§ao do objeto
    glutSolidCylinder(0.03, 0.2, 5, 3) #(raio, comprimento, faces, nao sei o que é)
    glPopMatrix()
    
#parte mais gordinha da luminária

    glColor3f(1.0, 0.4, 0.0) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaÃ§oes no objeto
    #glTranslate( -0.5, 0.0, 0.0)  #TranstaÃ§ao do objeto
    glRotatef(-90, 1.0, 0.0, 0.0)     #RotaÃ§ao do objeto
    cont = 1
    while (cont <= 8): #quanto maior mais fino a ponta( a quant de voltas)
        cont += 1.0
        glutSolidTorus(0.02,0.2,3,6)
        glTranslate( 0.0, 0.0, 0.035)
    glPopMatrix()


    #cilindro mrio/cima
    glColor3f(1.0, 0.4, 0.0) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaÃ§oes no objeto
    glTranslate( 0.0, 0.6, 0.0)  #TranstaÃ§ao do objeto
    glRotatef(90, 1.0, 0.0, 0.0)     #RotaÃ§ao do objeto
    glutSolidCylinder(0.03, 0.2, 5, 3) #(raio, comprimento, faces, nao sei o que é)
    glPopMatrix()

    #cilindro deitado
    glColor3f(1.0, 0.4, 0.0) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaÃ§oes no objeto
    glTranslate( 0.0, 0.4, 0.25)   #TranstaÃ§ao do objeto
    glRotatef(180, 0.0, 1.0, 0.0)     #RotaÃ§ao do objeto
    glutSolidCylinder(0.03, 0.5, 5, 3) #(raio, comprimento, faces, nao sei o que é)
    glPopMatrix()

    glColor3f(1.0, 0.4, 0.0) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaÃ§oes no objeto
    glTranslate( 0.0, 0.25, 0.0)   #TranstaÃ§ao do objeto
    glRotatef(90, 1.0, 0.0, 0.0)     #RotaÃ§ao do objeto
    glutSolidCylinder(0.2, 0.002, 6, 3) #(raio, comprimento, faces, nao sei o que é)
    glPopMatrix()

    glPushMatrix()
    glColor3f(1.0, 1.0, 1.0)
    glutSolidSphere(0.1, 5, 30, 30)
    glPopMatrix()
    
    glPopMatrix()

def luminaria_central():
    glPushMatrix()
    
    glColor3f(0.0, 0.0, 0.0) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    glScale(1.0,0.4,1.0)
    glutSolidCube(1)
    glPopMatrix()

    glColor3f(1.0, 1.0, 1.0) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    glTranslate(0.25,-0.2,0.3)
    glutSolidSphere(0.15,10,10)
    glPopMatrix()

    glColor3f(1.0, 1.0, 1.0) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    glTranslate(0.25,-0.2,-0.3)
    glutSolidSphere(0.15,10,10)
    glPopMatrix()

    glColor3f(1.0, 1.0, 1.0) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    glTranslate(-0.25,-0.2,-0.3)
    glutSolidSphere(0.15,10,10)
    glPopMatrix()

    glColor3f(1.0, 1.0, 1.0) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    glTranslate(-0.25,-0.2,0.3)
    glutSolidSphere(0.15,10,10)
    glPopMatrix()
    
    glPopMatrix()

def cabide(translate_x, translate_y, translate_z, rotacao_x, rotacao_y, rotacao_z):
    glColor3f(1, 0, 1.025)
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformacoes no objeto
    glTranslate(translate_x, translate_y + 0.5, translate_z)  #Transtacao do objeto
    glRotatef(90, rotacao_x, rotacao_y, rotacao_z)
    glScale(0.1, 1.0, 0.04)
    glutSolidCube(0.5)
    glPopMatrix()

    glPushMatrix()                # Push e Pop Isolam os efeitos das transformacoes no objeto
    glTranslate(translate_x + 0.11,translate_y + 0.63, translate_z)  #Transtacao do objeto
    glRotatef(45, rotacao_x, rotacao_y, rotacao_z)
    glScale(0.1, 0.7, 0.04)
    glutSolidCube(0.5)
    glPopMatrix()

    glPushMatrix()                # Push e Pop Isolam os efeitos das transformacoes no objeto
    glTranslate(translate_x - 0.11,translate_y + 0.63, translate_z)  #Transtacao do objeto
    glRotatef(-45, rotacao_x, rotacao_y, rotacao_z)
    glScale(0.1, 0.7, 0.04)
    glutSolidCube(0.5)
    glPopMatrix()

def cabo(translate_x, translate_y, translate_z, rotacao_x, rotacao_y, rotacao_z):
    glColor3f(0, 0, 0) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    glTranslate(translate_x, translate_y, translate_z)  #Transtaçao do objeto
    glScalef(3, 1, 0.4)
    glRotatef(90, rotacao_x, rotacao_y, rotacao_z)     #Rotaçao do objeto
    glutSolidCylinder(0.01, 4.0, 50, 50)

    glPopMatrix()

def camisa(translate_x, translate_y, translate_z, rotacao_x, rotacao_y, rotacao_z, cor_R, cor_G, cor_B):
    glColor3f(cor_R, cor_G, cor_B)
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformacoes no objeto
    glTranslate(translate_x, translate_y, translate_z)  #Transtacao do objeto
    glRotatef(180, rotacao_x, rotacao_y, rotacao_z)
    glScale(0.4, 0.7, 0.03)
    glutSolidCube(1.0)
    glPopMatrix()

    #manga esq
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformacoes no objeto
    glTranslate(translate_x - 0.3, translate_y + 0.175, translate_z)  #Transtacao do objeto
    glRotatef(-60, rotacao_x, rotacao_y, rotacao_z)
    glScale(0.4, 0.7, 0.05)
    glutSolidCube(0.5)
    glPopMatrix()

    #manga dir
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformacoes no objeto
    glTranslate(translate_x + 0.3, translate_y + 0.175, translate_z)  #Transtacao do objeto
    glRotatef(60, rotacao_x, rotacao_y, rotacao_z)
    glScale(0.4, 0.7, 0.05)
    glutSolidCube(0.5)
    glPopMatrix()

def chamaTudo():
    camisa(0, 0, 0, 0, 0, 0.6, 0, 0, 0)
    camisa(0, 0, 0.2, 0, 0, 0.6, 1, 0, 0)
    camisa(0, 0, 0.4, 0, 0, 0.6, 0, 1, 0)
    camisa(0, 0, 0.6, 0, 0, 1.5, 0, 0, 1)
    camisa(0, 0, 0.8, 0, 0, 1.5, 1, 1, 0)
    camisa(0, 0, 1, 0, 0, 1.5, 0, 1, 1)
    cabide(0, -0.25, 0.0, 0, 0, 2)
    cabide(0, -0.25, 0.2, 0, 0, 2)
    cabide(0, -0.25, 0.4, 0, 0, 2)
    cabide(0, -0.25, 0.6, 0, 0, 2)
    cabide(0, -0.25, 0.8, 0, 0, 2)
    cabide(0, -0.25, 1, 0, 0, 2)
    cabo(0, 0.5, -0.4,0, 0, 1)
    cabo(0, 0.5, -2, 0, 0, 1)
    camisa(0, 0, -1.8, 0, 0, 0.6, 0.7, 0.7, 0.7)
    camisa(0, 0, -1.6, 0, 0, 0.6, 0.2, 1, 0.3)
    camisa(0, 0, -1.4, 0, 0, 0.6, 0.6, 0.2, 1)
    camisa(0, 0, -1.2, 0, 0, 0.6, 0.6, 0, 0)
    camisa(0, 0, -1.0, 0, 0, 0.6, 1, 0.1, 0.9)
    camisa(0, 0, -0.8, 0, 0, 0.6, 0.4, 0, 1)
    cabide(0, -0.25, -1.8, 0, 0, 2)
    cabide(0, -0.25, -1.6, 0, 0, 2)
    cabide(0, -0.25, -1.4, 0, 0, 2)
    cabide(0, -0.25, -1.2, 0, 0, 2)
    cabide(0, -0.25, -1.0, 0, 0, 2)
    cabide(0, -0.25, -0.8, 0, 0, 2)

def manequim():
    #cabeça
    glColor3f(0, 0, 0)
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformacoes no objeto
    # glTranslate(0.0, 0, 0.02)  #Transtacao do objeto
    glTranslate(0.24, 1.7, 0.02)  #Transtacao do objeto
    glutSolidSphere(0.2, 50, 50)
    glPopMatrix()

    glColor3f(1, 1, 1)
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformacoes no objeto
    glTranslate(0.15, 1.75, 0.2)  #Transtacao do objeto
    glutSolidSphere(0.03, 50, 50)
    glPopMatrix()

    glPushMatrix()                # Push e Pop Isolam os efeitos das transformacoes no objeto
    glTranslate(0.3, 1.75, 0.2)  #Transtacao do objeto
    glutSolidSphere(0.03, 50, 50)
    glPopMatrix()

    glPushMatrix()                # Push e Pop Isolam os efeitos das transformacoes no objeto
    glTranslate(0.23, 1.6, 0.2)  #Transtacao do objeto
    glScalef(1, 2, 0.8)
    glutSolidSphere(0.03, 50, 50)
    glPopMatrix()

    glColor3f(0, 1, 0)
    glPushMatrix()
    glTranslate(0.23, 1.7, 0.22)  #Transtacao do objeto
    glRotatef(45, 0, 0, 1)
    glutSolidCube(0.02)
    glPopMatrix()

    #corpo
    glColor3f(1, 0, 0)
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformacoes no objeto
    glTranslate(0.25, 1.1, 0)  #Transtacao do objeto
    glScale(0.4, 0.7, 0.05)
    glutSolidCube(1.0)
    glPopMatrix()

    #manga esq
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformacoes no objeto
    glTranslate(-0.06, 1.28, 0)  #Transtacao do objeto
    glRotatef(-60, 0, 0, 1)
    glScale(0.4, 0.7, 0.05)
    glutSolidCube(0.5)
    glPopMatrix()

    #manga dir
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformacoes no objeto
    glTranslate(0.55, 1.28, 0)  #Transtacao do objeto
    glRotatef(60, 0, 0, 1)
    glScale(0.4, 0.7, 0.05)
    glutSolidCube(0.5)
    glPopMatrix()

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

def desenho():
    global abertoPorta
    global temp
    global angulo
    global angulo1
    
   
    eixos()

    glPushMatrix()
    glTranslate(-2.2, -0.1, 1.7)
    glutSolidSphere(0.05, 10, 10, 10)
    glPopMatrix()

    #luminaria vitrine - centro
    glPushMatrix()
    glTranslate(-1.1, -0.2, 1.7)

    glPushMatrix()
    glScale(0.4, 0.4, 0.4)
    luminaria()
    glPopMatrix()

    glPopMatrix()

    #luminaria vitrine - esquerda
    glPushMatrix()
    glTranslate(-2.2, -0.2, 1.7)

    glPushMatrix()
    glScale(0.4, 0.4, 0.4)
    luminaria()
    glPopMatrix()

    glPopMatrix()

    #luminaria vitrine - direita
    glPushMatrix()
    glTranslate(0.0, -0.2, 1.7)

    glPushMatrix()
    glScale(0.4, 0.4, 0.4)
    luminaria()
    glPopMatrix()

    glPopMatrix()

    ##luminaria centro
    glPushMatrix()
    glScale(0.7, 0.7, 0.7)
    luminaria_central()
    glPopMatrix()

    glPushMatrix()
    glTranslate(0.0, 0.0, 2.0)
########################
    #suporte giratorio
    glPushMatrix()
    glTranslate(-1.1, 0.0, -0.3)
    suporteGiratorio()
    glPopMatrix()

    #motor
    glPushMatrix()
    glRotatef(90, 1.0, 0.0, 0.0)
    glTranslate(-1.1, -0.3, 2.35)
    glutSolidCylinder(0.2, 0.1, 20, 20)
    glPopMatrix()
########################



    ###delimitador vitrine
    glPushMatrix()
    glColor3f(0.7, 0.7, 0.7)

    glPushMatrix()
    glRotatef(180, 1.0, 0.0, 0.0)
    glTranslate(0.8, 2.2, 0.0)
    glutSolidCylinder(0.05, 0.6, 20, 20)
    glPopMatrix()

    glPushMatrix()
    glRotatef(90, 0.0, 1.0, 0.0)
    glTranslate(0.6, -2.2, -3.1)
    glutSolidCylinder(0.05, 3.9, 20, 20)
    glPopMatrix()

    glPopMatrix()

    ########## TV
    glPushMatrix()
    glTranslate(0.0, -0.6, -4.0)

    tv()
    
    #animação 
    glPushMatrix()
    glScale(0.27, 0.27, 0.01)
    glTranslate(0.0, 0.0, 2.2)
    animation()
    glPopMatrix()

    glPopMatrix()

    ######## escada
    glPushMatrix()
    glTranslate(-2.45, -2.45, -3.2)
    
    glPushMatrix()
    glScale(0.5, 0.52, 0.5)
    glRotatef(-40, 0.0, 1.0, 0.0)

    unEscada()

    glPushMatrix()
    glTranslate(0.0, 1.6, 0.0)
    glRotatef(-155, 0.0, 1.0, 0.0)
    unEscada()
    glPopMatrix()

    glPushMatrix()
    glTranslate(0.0, 3.2, 0.0)
    glRotatef(45, 0.0, 1.0, 0.0)
    unEscada()
    glPopMatrix()

    glPopMatrix()

    glPopMatrix()

    
    paredesSuperior()

    #coluna frente direita
    glPushMatrix()
    glRotatef(45, 0.0, 1.0, 0.0)
    glTranslate(2.2, -2.5, 2.2)

    glColor3f(0.7, 0.0, 0.0)
    glPushMatrix()
    glRotatef(-90, 1.0, 0.0, 0.0)
    glutSolidCylinder(0.2, 2.5, 4, 2)
    glPopMatrix()

    glPopMatrix()

    #coluna frente esquerda
    glPushMatrix()
    glRotatef(45, 0.0, 1.0, 0.0)
    glTranslate(-2.2, -2.5, -2.2)

    glColor3f(0.7, 0.0, 0.0)
    glPushMatrix()
    glRotatef(-90, 1.0, 0.0, 0.0)
    glutSolidCylinder(0.2, 2.5, 4, 2)
    glPopMatrix()

    glPopMatrix()

    #coluna atras direita
    glPushMatrix()
    glTranslate(0.0, 0.0, -4.0)

    glPushMatrix()
    glRotatef(45, 0.0, 1.0, 0.0)
    glTranslate(2.2, -2.5, 2.2)

    glColor3f(0.7, 0.0, 0.0)
    glPushMatrix()
    glRotatef(-90, 1.0, 0.0, 0.0)
    glutSolidCylinder(0.2, 2.5, 4, 2)
    glPopMatrix()

    glPopMatrix()

    glPopMatrix()

    #coluna atras esquerda
    glPushMatrix()
    glTranslate(0.0, 0.0, -4.0)

    glPushMatrix()
    glRotatef(45, 0.0, 1.0, 0.0)
    glTranslate(-2.2, -2.5, -2.2)

    glColor3f(0.7, 0.0, 0.0)
    glPushMatrix()
    glRotatef(-90, 1.0, 0.0, 0.0)
    glutSolidCylinder(0.2, 2.5, 4, 2)
    glPopMatrix()

    glPopMatrix()

    glPopMatrix()
    

    glPushMatrix()
    texture_id = read_texture('img/floor1.jpg')
    glEnable(GL_TEXTURE_2D)
    #glBindTexture(GL_TEXTURE_2D, texture_id)
    glEnable(GL_TEXTURE_GEN_S)
    glEnable(GL_TEXTURE_GEN_T)
    glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, GL_OBJECT_LINEAR)
    glTexGeni(GL_T, GL_TEXTURE_GEN_MODE, GL_OBJECT_LINEAR)

    glPushMatrix()
    glRotatef(90, 1.0, 0.0, 0.0)

    #piso
    glColor3f(0.8, 0.4, 0.4)
    glPushMatrix()
    glTranslate(0.0, -2.0, 2.45)
    glScale(2.15, 1.4, 0.009)
    glutSolidCube(3)

    glPopMatrix()

    glPopMatrix()

    glDisable(GL_TEXTURE_2D)
    glPopMatrix()

    ############ teto
    glColor3f(1.0, 1.0, 1.0)
    glPushMatrix()
    glTranslate(0.0, 2.05, 0.0)

    #piso
    glPushMatrix()
    glRotatef(90, 1.0, 0.0, 0.0)

    glPushMatrix()
    glTranslate(0.7, -2.0, 2.0)
    glScale(1.65, 1.38, 0.009)
    glutSolidCube(3)

    glPopMatrix()

    glPopMatrix()

    #piso
    glPushMatrix()
    glRotatef(90, 1.0, 0.0, 0.0)
    
    glPushMatrix()
    glTranslate(-2.5, -1.58, 2.0)
    glScale(0.5, 1.08, 0.009)
    glutSolidCube(3)

    glPopMatrix()

    glPopMatrix()

    glPopMatrix()


    if(abertoPorta == 0):
        for x in numpy.arange(0.0, 0.6, 0.1):
            if(temp >= 0):
                temp -= x
    else:
        for x in numpy.arange(0.0, 0.6, 0.1):
            if(temp <= 87):
                temp += x
                
    if(angulo < 15 and abertoPorta == 0):
        abertoPorta = 1
    elif(angulo >= 15 and abertoPorta == 1):
        abertoPorta = 0

    ##############porta direita
    glPushMatrix()
    glTranslate(3.0, -2.5, 0.0)

    glPushMatrix()
    glRotatef(-temp, 0.0, 1.0, 0.0)
    

    glPushMatrix()
    glTranslate(-0.9, 0.7, -0.09)
    pegadorPorta()
    glPopMatrix()

    glColor4f(1, 1, 1 , 0.1)
    glPushMatrix()
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    
    glPushMatrix()
    glScale(1.0, 2.5, 0.05)
    glTranslate(-0.5, 0.5, 0.0)
    glutSolidCube(1)
    glPopMatrix()    

    glDisable(GL_BLEND)
    glPopMatrix()

    glPopMatrix()

    glPopMatrix()

    ############porta esquerda
    glPushMatrix()
    glTranslate(1.0, -2.5, 0.0)

    glPushMatrix()
    glRotatef(temp, 0.0, 1.0, 0.0)
    

    glPushMatrix()
    glTranslate(0.9, 0.7, -0.09)
    pegadorPorta()
    glPopMatrix()

    glColor4f(1, 1, 1 , 0.1)
    glPushMatrix()
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    
    glPushMatrix()
    glScale(1.0, 2.5, 0.05)
    glTranslate(0.5, 0.5, 0.0)
    glutSolidCube(1)
    glPopMatrix()    

    glDisable(GL_BLEND)
    glPopMatrix()

    glPopMatrix()

    glPopMatrix()

    #vidros
    glColor4f(1, 1, 1 , 0.1)
    glPushMatrix()
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    

    #fundo
    glPushMatrix()
    glTranslate(0.0, 0.0, -4.0)

    glPushMatrix()
    glScale(6.0, 2.5, 0.05)
    glTranslate(0.0, -0.5, 0.0)
    glutSolidCube(1)
    glPopMatrix()

    glPopMatrix()

    #direita
    glPushMatrix()
    glTranslate(3.1, 0.0, -2.0)

    glPushMatrix()
    glScale(0.05, 2.5, 4.0)
    glTranslate(0.0, -0.5, 0.0)
    glutSolidCube(1)
    glPopMatrix()

    glPopMatrix()

    #direita
    glPushMatrix()
    glTranslate(-3.1, 0.0, -2.0)

    glPushMatrix()
    glScale(0.05, 2.5, 4.0)
    glTranslate(0.0, -0.5, 0.0)
    glutSolidCube(1)
    glPopMatrix()

    glPopMatrix()

     ###frente
    glPushMatrix()
    glTranslate(1.0, 0.0, 0.0)

    glPushMatrix()
    glScale(4.0, 2.5, 0.05)
    glTranslate(-0.5, -0.5, 0.0)
    glutSolidCube(1)
    glPopMatrix()  

    glPopMatrix()

    glDisable(GL_BLEND)
    glPopMatrix()

    glPopMatrix()



    glutPostRedisplay()

    
def iluminacao_da_cena():

    luzAmbiente0=[0.2,0.2,0.2,0.0]
    luzDifusa0=[0.1,0.1,0.1,0.0]  # ; // "cor"
    luzEspecular0 = [0.0, 0.0, 0.0, 0.0]  #;// "brilho"
    posicaoLuz0=[0.0, 50.0, 5.0, 1.0]

    luzAmbiente1=[0.0,0.0,0.0,1.0]
    luzDifusa1=[1.0,1.0,1.0,1.0]  # ; // "cor"
    luzEspecular1 = [0.0, 0.0, 0.0, 0.0]  #;// "brilho"
    posicaoLuz1=[-1.1, -0.15, 1.7, 1.0]  # Ãºltima coord como 0 pra funcionar como vetor da luz direcional
    direcao1 = [0.0, -3.0, 0.0]


    luzAmbiente2=[0.0,0.0,0.0,1.0]
    luzDifusa2=[1.0, 1.0, 1.0, 1.0]  # ; // "cor"
    luzEspecular2 = [0.0, 0.0, 0.0, 0.0]  #;// "brilho"
    posicaoLuz2=[-0.0, -0.1, 1.7, 1.0]  # Ãºltima coord como 0 pra funcionar como vetor da luz direcional
    direcao2 = [0.0, -3.0, 0.0]  # direÃ§Ã£o do vetor do spot

    luzAmbiente3=[0.0,0.0,0.0,1.0]
    luzDifusa3=[1.0, 1.0, 1.0, 1.0]  # ; // "cor"
    luzEspecular3 = [0.0, 0.0, 0.0, 0.0]  #;// "brilho"
    posicaoLuz3=[-2.2, -0.1, 1.7, 1.0]  # Ãºltima coord como 0 pra funcionar como vetor da luz direcional
    direcao3 = [0.0, -3.0, 0.0]  # direÃ§Ã£o do vetor do spot

    especularidade=[1.0,1.0,1.0,1.0]
    especMaterial = 60;

    glClearColor(0.0, 0.0, 0.0, 0.0)

    glShadeModel(GL_SMOOTH)   # GL_SMOOTH ou GL_FLAT

    glMaterialfv(GL_FRONT,GL_SPECULAR, especularidade)

    glMateriali(GL_FRONT,GL_SHININESS,especMaterial)


    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, luzAmbiente0)

    # Define os parametros da luz ambiente
    glLightfv(GL_LIGHT0, GL_AMBIENT, luzAmbiente0)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, luzDifusa0 )
    glLightfv(GL_LIGHT0, GL_SPECULAR, luzEspecular0 )
    glLightfv(GL_LIGHT0, GL_POSITION, posicaoLuz0 )

    # Define os parametros da luz de numero 1 / bancada
    glLightfv(GL_LIGHT1, GL_AMBIENT, luzAmbiente1)
    glLightfv(GL_LIGHT1, GL_DIFFUSE, luzDifusa1 )
    glLightfv(GL_LIGHT1, GL_SPECULAR, luzEspecular1 )
    glLightfv(GL_LIGHT1, GL_POSITION, posicaoLuz1 )
    glLightfv(GL_LIGHT1, GL_SPOT_DIRECTION, direcao1); #direcao da luz
    glLightf(GL_LIGHT1, GL_SPOT_CUTOFF, 10); # angulo do cone, de 0 a 180.

    # Define os parametros da luz de numero 2 / bancada
    glLightfv(GL_LIGHT2, GL_AMBIENT, luzAmbiente2)
    glLightfv(GL_LIGHT2, GL_DIFFUSE, luzDifusa2 )
    glLightfv(GL_LIGHT2, GL_SPECULAR, luzEspecular2 )
    glLightfv(GL_LIGHT2, GL_POSITION, posicaoLuz2 )
    glLightfv(GL_LIGHT2, GL_SPOT_DIRECTION, direcao2); #direcao da luz
    glLightf(GL_LIGHT2, GL_SPOT_CUTOFF, 10); # angulo do cone, de 0 a 180.

    # Define os parametros da luz de numero 2 / bancada
    glLightfv(GL_LIGHT3, GL_AMBIENT, luzAmbiente3)
    glLightfv(GL_LIGHT3, GL_DIFFUSE, luzDifusa3 )
    glLightfv(GL_LIGHT3, GL_SPECULAR, luzEspecular3 )
    glLightfv(GL_LIGHT3, GL_POSITION, posicaoLuz3 )
    glLightfv(GL_LIGHT3, GL_SPOT_DIRECTION, direcao3); #direcao da luz
    glLightf(GL_LIGHT3, GL_SPOT_CUTOFF, 10); # angulo do cone, de 0 a 180.


    glEnable(GL_COLOR_MATERIAL)
    # Habilita o uso de iluminaÃ§Ã£o
    glEnable(GL_LIGHTING)

    # Habilita a luz de nÃºmero 0
    if estadoluz0 == 1:
        glEnable(GL_LIGHT0)
    else:
        glDisable(GL_LIGHT0)

    # Habilita a luz de nÃºmero 1
    if estadoluz1 == 1:
        glEnable(GL_LIGHT1)
    else:
        glDisable(GL_LIGHT1)

    # Habilita a luz de nÃºmero 2
    if estadoluz2 == 1:
        glEnable(GL_LIGHT2)
        glEnable(GL_LIGHT3)
    else:
        glDisable(GL_LIGHT2)
        glDisable(GL_LIGHT3)

    # Habilita o depth-buffering
    glEnable(GL_DEPTH_TEST)

def tela():
    global angulo
    global distanciamax
    global aux1
    global aux2

# AJUSTE DE APARÊNCIA

    # Especifica que a cor de fundo da janela será branca
    glClearColor(0,0,0,0)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Limpar a tela
    glClearColor(1.0, 1.0, 1.0, 1.0) # Limpa a janela com a cor especificada
    glMatrixMode(GL_PROJECTION) # Muda a matriz de projeçao
    glLoadIdentity()# carrega a matriz identidade

    #gluPerspective(angulo, aspecto , near (perto), far(longe) )
    #  angulo = angulo em graus na direçao y.
    #  aspecto = deformaçao da janela. normalmente e a razao entre a largura e altura
    #  near = a menor distancia desenhada
    #  far = a maior distancia para que o objeto seja desenhado
    gluPerspective(angulo, 1.77, 0.1, distanciamax) # Especifica a projeção perspectiva

    #glOrtho(left,right,bottom, top, near, far)
    #  left,right,bottom, top = limites da projeçao
    #  near = a menor distancia desenhada
    #  far = a maior distancia para que o objeto seja desenhado 
    #glOrtho(-3,3,-2.5,2.5,0.1,500) # Especifica a projeção paralela ortogonal

    glMatrixMode(GL_MODELVIEW) # Especifica sistema de coordenadas do modelo
    glLoadIdentity() # Inicializa sistema de coordenadas do modelo

#CÂMERA

    #Pense na câmera como um vetor que aponta para o alvo da cena. #
    #Cada ponto desse vetor é em 3D (x, y, z)
    # A última coordenada ajusta a posição da câmera (deitada, de pé, invertida etc)

    #gluLookAt(eyex, eyey, eyez, alvox, alvoy, alvoz, upx, upy, upz)
    #    eyex, eyey, eyez = posiçao da camera
    #    alvox, alvoy, alvoz = coordenada para onde a camera olha.
    #    upx, upy, upz = indica a posiçao vertical da camera.
    gluLookAt(sin(esqdir) * 10, 0 + cimabaixo ,cos(esqdir) * 10, aux1,aux2,0, 0,1,0) # Especifica posição do observador e do alvo
    print('Camera: (' + str( sin(esqdir) * 10) + ',' + str(cimabaixo) + "," + str(cos(esqdir) * 10) + ')')
    print('Alvo: (' + str(aux1) +','+str(aux2)+',0)')

   
    
    iluminacao_da_cena()
    #glEnable(GL_DEPTH_TEST) # verifica os pixels que devem ser plotados no desenho 3d

    desenho()                    
    glFlush()                    # Aplica o desenho


# FUNÇÕES DO TECLADO E MOUSE    

# Função callback chamada para gerenciar eventos de teclas normais
# Obs.: maiusculo e minúsculo faz diferença.
def Teclado (tecla, x, y):
    global aux1
    global aux2
    global esqdir
    global cimabaixo
    global estadoluz0, estadoluz1, estadoluz2
    global angulo
    global abertoPorta

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

    if tecla == b'r':
        esqdir = 1.2
        cimabaixo = 3.0

    if tecla == b't':
        esqdir = -1.2
        cimabaixo = -2.75

    if tecla == b'y':
        esqdir = 0
        cimabaixo = 7.44
        aux1 = 0.7

    if tecla == b'p': #porta
        esqdir = 0.2
        cimabaixo = -1.2
        aux1 = 2.0
        aux2 = -1.2
        angulo = 15

    if tecla == b'o': #andar inferior
        esqdir = -0.0
        cimabaixo = -1.2
        aux1 = 0.0
        aux2 = -1.2
        angulo = 21

    if tecla == b'i': #quarto direita
        esqdir = 0.0
        cimabaixo = 2.0
        aux1 = 0.0
        aux2 = 1.8
        angulo = 21

    if tecla == b'u': #quarto esquerda
        esqdir = -0.4
        cimabaixo = 2.05
        aux1 = -3.5
        aux2 = 3.0
        angulo = 38

    if tecla == b'k': 
        abertoPorta += 1
        if(abertoPorta == 2):
            abertoPorta = 0


    if tecla == b'0': # 0
        if estadoluz0 == 0:
            estadoluz0 = 1
            glEnable(GL_LIGHT0)
        else:
            estadoluz0 = 0
            glDisable(GL_LIGHT0)
    if tecla == b'1': # 1
        if estadoluz1 == 0:
            estadoluz1 = 1
            glEnable(GL_LIGHT1)
        else:
            estadoluz1 = 0
            glDisable(GL_LIGHT1)
    if tecla == b'2': # 2
        if estadoluz2 == 0:
            estadoluz2 = 1
            glEnable(GL_LIGHT2)
            glEnable(GL_LIGHT3)
        else:
            estadoluz2 = 0
            glDisable(GL_LIGHT2)
            glDisable(GL_LIGHT3)       


    tela()
    glutPostRedisplay()

# Função callback chamada para gerenciar eventos de teclas especiais
def TeclasEspeciais (tecla, x, y):
    global esqdir
    global cimabaixo
    global angulo
    print("*** Tratamento de teclas especiais")
    print ("tecla: ", tecla)
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
        cimabaixo = cimabaixo + 0.05
    elif tecla == GLUT_KEY_DOWN:
        cimabaixo = cimabaixo - 0.05
    else:
        print ("Apertou... " , tecla)
    tela()
    glutPostRedisplay()   

# Função callback chamada para gerenciar eventos do mouse
def ControleMouse(button, state, x, y):
    global angulo
    if (button == GLUT_LEFT_BUTTON):
        if (state == GLUT_DOWN): 
            if (angulo >= 1):
                angulo -= 2
		
    if (button == GLUT_RIGHT_BUTTON):
        if (state == GLUT_DOWN):   # Zoom-out
            if (angulo <= 130):
                angulo += 2
    tela()
    glutPostRedisplay()


# PROGRAMA PRINCIPAL

glutInit(argv)
glutInitDisplayMode(GLUT_RGBA | GLUT_DEPTH)
glutInitWindowSize(1200, 700)
glutCreateWindow(b"Exercicio CG - RLF")
glutDisplayFunc(tela)
glutMouseFunc(ControleMouse)
glutKeyboardFunc (Teclado)
glutSpecialFunc (TeclasEspeciais)
glutMainLoop()  # Inicia o laço de eventos da GLUT