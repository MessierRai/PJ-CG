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
global angulo
global distanciamax
global aux
global estadoluz0, estadoluz1, estadoluz2, estadoluz3
global abertoPorta
global temp
global angulo1

global angPartes
global transPartes
global statusPortRet

global camX
global camY
global camZ
global alvoCamX
global alvoCamY
global alvoCamZ

esqdir = 0
cimabaixo = 0
angulo = 60
distanciamax = 100
aux = 0 
estadoluz0 = 1
estadoluz1 = 0
estadoluz2 = 0
estadoluz3 = 0
abertoPorta = 0
temp = 0
angulo1 = 0

angPartes = 0
transPartes = 0.1
statusPortRet = 0

camX = 0
camY = -1
camZ = 5
alvoCamX = 0
alvoCamY = -1
alvoCamZ = -1

movMan = [-0.2, -2.9, 1.9]

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
    glTranslate(-0.1, -1.96, 0.0)
    #glutSolidTeapot(0.2)
    bolsa()
    glPopMatrix()

    #suporte
    glColor3f(1.0, 0.0, 0.0)
    glPushMatrix()
    glRotatef(90, 1.0, 0.0, 0.0)
    glTranslate(0.0, 0.0, 1.84)
    glutSolidCylinder(0.3, 0.06, 20, 20)
    glPopMatrix()

    #eixo
    glPushMatrix()
    glRotatef(90, 1.0, 0.0, 0.0)
    glTranslate(0.0, 0.0, 1.84)
    glutSolidCylinder(0.07, 0.5, 20, 20)
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
    glScale(1.0,0.3,1.0)
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
    cabo(0, 0.5, -2, 0, 0, 1)
    camisa(0, 0, -1.8, 0, 0, 0.6, 0.7, 0.7, 0.7)
    camisa(0, 0, -1.6, 0, 0, 0.6, 0.2, 1, 0.3)
    camisa(0, 0, -1.4, 0, 0, 0.6, 0.6, 0.2, 1)
    camisa(0, 0, -1.2, 0, 0, 0.6, 0.6, 0, 0)
    camisa(0, 0, -1.0, 0, 0, 0.6, 1, 0.1, 0.9)
    camisa(0, 0, -0.8, 0, 0, 0.6, 0.4, 0, 1)
    camisa(0, 0, -0.6, 0, 0, 1.5, 0, 1, 1)
    cabide(0, -0.25, -1.8, 0, 0, 2)
    cabide(0, -0.25, -1.6, 0, 0, 2)
    cabide(0, -0.25, -1.4, 0, 0, 2)
    cabide(0, -0.25, -1.2, 0, 0, 2)
    cabide(0, -0.25, -1.0, 0, 0, 2)
    cabide(0, -0.25, -0.8, 0, 0, 2)
    cabide(0, -0.25, -0.6, 0, 0, 2)

def chamaTudo2ORetorno():
    cabo(0, 0.5, -2, 0, 0, 1)
    cabide(0, -0.25, -1.8, 0, 0, 2)
    cabide(0, -0.25, -1.6, 0, 0, 2)
    cabide(0, -0.25, -1.4, 0, 0, 2)
    cabide(0, -0.25, -1.2, 0, 0, 2)
    cabide(0, -0.25, -1.0, 0, 0, 2)
    cabide(0, -0.25, -0.8, 0, 0, 2)
    cabide(0, -0.25, -0.6, 0, 0, 2)
    calca(-0.25, -0.45, -1.8)
    calca(-0.25, -0.45, -1.6)
    calca(-0.25, -0.45, -1.4)
    calca(-0.25, -0.45, -1.2)
    calca(-0.25, -0.45, -1.0)
    calca(-0.25, -0.45, -0.8)
    calca(-0.25, -0.45, -0.6)


def bolsa():
    #base da bolsa
    glColor3f(0, 1, 0)
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformacoes no objeto
    glTranslate(0.12, 0.25, 0)  #Transtacao do objeto
    glScalef(1, 0.5, 0.5)
    glutSolidCube(0.5)
    glPopMatrix()

    glColor3f(1, 0, 0)
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformacoes no objeto
    glTranslate(0.13, 0.37, 0)  #Transtacao do objeto
    glScalef(1, 0.5, 0.5)
    glutSolidCube(0.1)
    glPopMatrix()

def calca(translate_x, translate_y, translate_z):
    glPushMatrix()
    glTranslate(translate_x, translate_y, translate_z)
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

    glPopMatrix()

def balcao():

    glPushMatrix()
    glTranslate(-2.5, -2.1, 0.55)

    glColor3f(1.0, 1.0, 1.0)
    glPushMatrix()
    glScale(0.5, 0.7, 1.5)
    glutSolidCube(1)
    glPopMatrix()

    glPopMatrix()

    glPushMatrix()
    glTranslate(-2.5, -1.75, 0.55)

    glColor3f(1.0, 0.0, 0.0)
    glPushMatrix()
    glScale(0.6, 0.05, 1.6)
    glutSolidCube(1)
    glPopMatrix()

    glPopMatrix()

def paredesProvador():
    #parede provador direita

    glPushMatrix()
    glTranslate(1.4, 0.0, 0.75)

    glPushMatrix()
    glColor3f(1.0, 0.0, 0.0)
    glScale(1.2, 2.43, 0.06)
    glTranslate(1.0, 0.52, 0.0)
    glutSolidCube(1)
    glPopMatrix()

    glPopMatrix()

    #parede provador esquerda
    glPushMatrix()
    glTranslate(1.4, 0.0, -0.75)

    glPushMatrix()
    glScale(1.2, 2.43, 0.06)
    glTranslate(1.0, 0.52, 0.0)
    glutSolidCube(1)
    glPopMatrix()

    glPopMatrix()

def portaRetratil():
    global angPartes
    global transPartes
    global statusPortRet

    if(statusPortRet == 0):
        for x in numpy.arange(0.1, 0.6, 0.1):
            if(transPartes >= 0.1 and  angPartes >= 0):
                angPartes -= x
            if(transPartes <= 0.1):
                transPartes = transPartes + 0.0001
    elif(statusPortRet == 1):
        for x in numpy.arange(0.1, 0.6, 0.1):
            if(angPartes >= 90 and transPartes > 0):
                transPartes = transPartes - 0.0001
            if(angPartes <= 90):
                angPartes += x


    glPushMatrix()
    glColor3f(1.0, 1.0, 1.0)
    glScale(1.5, 2.4, 1.0)

    #parte 1
    glPushMatrix()
    glTranslate(transPartes, 0.0, 0.0)

    glPushMatrix()
    glRotate(angPartes, 0.0, 1.0, 0.0)

    glPushMatrix()
    glScale(0.2, 1.0, 0.03)
    glTranslate(0.0, 0.5, 0.0)
    glutSolidCube(1)
    glPopMatrix()

    glPopMatrix()

    glPopMatrix()


    #parte 2
    glPushMatrix()
    glTranslate(transPartes * 3, 0.0, 0.0)

    glPushMatrix()
    glRotate(angPartes, 0.0, 1.0, 0.0)

    glPushMatrix()
    glScale(0.2, 1.0, 0.03)
    glTranslate(0.0, 0.5, 0.0)
    glutSolidCube(1)
    glPopMatrix()

    glPopMatrix()

    glPopMatrix()

    #parte 3
    glPushMatrix()
    glTranslate(transPartes * 5, 0.0, 0.0)

    glPushMatrix()
    glRotate(angPartes, 0.0, 1.0, 0.0)

    glPushMatrix()
    glScale(0.2, 1.0, 0.03)
    glTranslate(0.0, 0.5, 0.0)
    glutSolidCube(1)
    glPopMatrix()

    glPopMatrix()

    glPopMatrix()

    #parte 4
    glPushMatrix()
    glTranslate(transPartes * 7, 0.0, 0.0)

    glPushMatrix()
    glRotate(angPartes, 0.0, 1.0, 0.0)

    glPushMatrix()
    glScale(0.2, 1.0, 0.03)
    glTranslate(0.0, 0.5, 0.0)
    glutSolidCube(1)
    glPopMatrix()

    glPopMatrix()

    glPopMatrix()

    #parte 5
    glPushMatrix()
    glTranslate(transPartes * 9, 0.0, 0.0)

    glPushMatrix()
    glRotate(angPartes, 0.0, 1.0, 0.0)

    glPushMatrix()

    
    glScale(0.2, 1.0, 0.03)
    glTranslate(0.0, 0.5, 0.0)
    glutSolidCube(1)
    glPopMatrix()

    glPopMatrix()

    glPopMatrix()

    glPopMatrix()

    glutPostRedisplay()

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

def puff():
    glPushMatrix()
    glColor3f(0.0, 0.0, 0.0)
    glRotate(-90, 1.0, 0.0, 0.0)
    glScale(1.0, 1.0, 0.8)

    glPushMatrix()
    glutSolidCylinder(0.5, 1.2, 8, 2)
    glPopMatrix()

    
    glPushMatrix()
    glColor3f(1.0, 0.0, 0.0)
    glTranslate(0.0, 0.0, 1.2)
    glutSolidTorus(0.1, 0.4, 20, 20)
    glPopMatrix()

    glPushMatrix()
    glColor3f(1.0, 0.0, 0.0)
    glTranslate(0.0, 0.0, 1.28)
    glutSolidCylinder(0.4, 0.01, 8, 2)
    glPopMatrix()

    glPopMatrix()

def desenho():
    global abertoPorta
    global temp
    global angulo
    global angulo1
    global movMan
    global camX
    global camZ
    
    #eixos()

    #puff tv
    glPushMatrix()
    glTranslate(1.0, 0.1, -1.2)

    glPushMatrix()
    glScale(0.5, 0.5, 0.5)
    puff()
    glPopMatrix()

    glPopMatrix()

    #puff entrada escadas
    glPushMatrix()
    glTranslate(-2.8, 0.1, 0.6)

    glPushMatrix()
    glScale(0.5, 0.5, 0.5)
    puff()
    glPopMatrix()

    glPopMatrix()

    #puff oposto tv
    glPushMatrix()
    glTranslate(1.1, 0.1, 1.4)

    glPushMatrix()
    glScale(0.5, 0.5, 0.5)
    puff()
    glPopMatrix()

    glPopMatrix()


    #puff terreo fundo
    glPushMatrix()
    glTranslate(2.8, -2.4, -1.0)

    glPushMatrix()
    glScale(0.5, 0.5, 0.5)
    puff()
    glPopMatrix()

    glPopMatrix()

    #puff terreo meio
    glPushMatrix()
    glTranslate(2.8, -2.4, -0.2)

    glPushMatrix()
    glScale(0.5, 0.5, 0.5)
    puff()
    glPopMatrix()

    glPopMatrix()

    #puff terreo meio
    glPushMatrix()
    glTranslate(2.8, -2.4, 0.6)
    glPushMatrix()
    glScale(0.5, 0.5, 0.5)
    puff()
    glPopMatrix()

    glPopMatrix()

    ####manequim
    glPushMatrix()
    glScale(0.8, 0.8, 0.8)
    glTranslate(movMan[0], -2.9, movMan[2])
    manequim()
    glPopMatrix()

    balcao()

    #porta provador meio
    glPushMatrix()
    glTranslate(2.0, 0.05, 0.75)

    glPushMatrix()
    glRotate(90, 0.0, 1.0, 0.0)
    portaRetratil()
    glPopMatrix()

    glPopMatrix()

    #porta provador direita
    glPushMatrix()
    glTranslate(2.0, 0.05, 2.0)

    glPushMatrix()
    glRotate(90, 0.0, 1.0, 0.0)
    portaRetratil()
    glPopMatrix()

    glPopMatrix()

    #porta provador esquerda
    glPushMatrix()
    glTranslate(2.0, 0.05, -0.75)

    glPushMatrix()
    glRotate(90, 0.0, 1.0, 0.0)
    glScale(0.8, 1.0, 1.0)
    portaRetratil()
    glPopMatrix()

    glPopMatrix()

    paredesProvador()

    ######## calcas andar superior frente TV
    glPushMatrix()
    glTranslate(0.0, 0.8, 0.2)
    glScale(0.9, 0.9, 0.9)
    chamaTudo2ORetorno()
    glPopMatrix()

    # na parede frente
    glPushMatrix()
    glTranslate(-3.5, 0.0, 1.6)

    glPushMatrix()
    glRotate(90, 0.0, 1.0, 0.0)

    glPushMatrix()
    glTranslate(0.0, 0.8, 2.2)
    glScale(0.9, 0.9, 0.9)
    chamaTudo2ORetorno()
    glPopMatrix()

    glPopMatrix()

    glPopMatrix()

    #camisas
    glPushMatrix()
    glTranslate(-0.4, 0.3, 0.1)

    glPushMatrix()
    glRotate(90, 0.0, 1.0, 0.0)

    glPushMatrix()
    glTranslate(-1.4, 0.5, 0.4)
    glScale(0.9, 0.9, 0.9)
    chamaTudo()
    glPopMatrix()

    glPopMatrix()

    glPopMatrix()

    # na parede frente - perto do provador
    glPushMatrix()
    glTranslate(-0.95, 0.0, 1.6)

    glPushMatrix()
    glRotate(90, 0.0, 1.0, 0.0)

    glPushMatrix()
    glTranslate(0.0, 0.8, 2.2)
    glScale(0.9, 0.9, 0.9)
    chamaTudo2ORetorno()
    glPopMatrix()

    glPopMatrix()

    glPopMatrix()

    ######## camisas - andar baixo
    glPushMatrix()
    glRotatef(90, 0.0, 1.0, 0.0)
    glTranslate(1.5, -1.9, 0.4)
    glScale(0.9, 0.9, 0.9)
    chamaTudo()
    glPopMatrix()

    glPushMatrix()
    glRotatef(90, 0.0, 1.0, 0.0)
    glTranslate(1.5, -1.9, 1.6)
    glScale(0.9, 0.9, 0.9)
    chamaTudo()
    glPopMatrix()

    glPushMatrix()
    glRotatef(90, 0.0, 1.0, 0.0)
    glTranslate(1.5, -1.9, 2.8)
    glScale(0.9, 0.9, 0.9)
    chamaTudo()
    glPopMatrix()

    ##camisas andar superior frente tv
    glPushMatrix()
    glTranslate(-1.4, 0.5, 0.4)
    glScale(0.9, 0.9, 0.9)
    chamaTudo()
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
    glScale(0.7, 0.5, 0.7)
    glTranslate(0.0, -0.1, 0.0)
    luminaria_central()
    glPopMatrix()

    ##luminaria centro - andar superior
    glPushMatrix()
    glScale(0.7, 0.5, 0.7)
    glTranslate(0.0, 4.8, 0.0)
    luminaria_central()
    glPopMatrix()


    glPushMatrix()
    glTranslate(0.0, 0.0, 2.0)
########################
    #suporte giratorio
    glPushMatrix()
    glTranslate(-1.1, -0.1, -0.3)
    suporteGiratorio()
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
    glTranslate(-0.5, 1.7, -3.9)

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
    glBindTexture(GL_TEXTURE_2D, texture_id)
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

    ############ teto
    glColor3f(1.0, 1.0, 1.0)
    glPushMatrix()
    glTranslate(0.0, 4.45, 0.0)

    #piso
    glPushMatrix()
    glRotatef(90, 1.0, 0.0, 0.0)

    glPushMatrix()
    glTranslate(0.0, -2.0, 2.0)
    glScale(2.1, 1.38, 0.009)
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

    #######vidros
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

    luzAmbiente4=[0.0,0.0,0.0,1.0]
    luzDifusa4=[0.1, 0.1, 0.1, 0.0]  # ; // "cor"
    luzEspecular4 = [0.0, 0.0, 0.0, 0.0]  #;// "brilho"
    posicaoLuz4=[0.18, -0.1, 0.0, 1.0]  # Ãºltima coord como 0 pra funcionar como vetor da luz direcional
    direcao4 = [2.0, -3.0, 0.0]  # direÃ§Ã£o do vetor do spot

    luzAmbiente5=[0.0,0.0,0.0,1.0]
    luzDifusa5=[0.1, 0.1, 0.1, 0.0]  # ; // "cor"
    luzEspecular5 = [0.0, 0.0, 0.0, 0.0]  #;// "brilho"
    posicaoLuz5=[-0.18, -0.1, 0.0, 1.0]  # Ãºltima coord como 0 pra funcionar como vetor da luz direcional
    direcao5 = [-2.0, -3.0, 0.0]  # direÃ§Ã£o do vetor do spot

    luzAmbiente6=[0.0,0.0,0.0,1.0]
    luzDifusa6=[0.1, 0.1, 0.1, 0.0]  # ; // "cor"
    luzEspecular6 = [0.0, 0.0, 0.0, 0.0]  #;// "brilho"
    posicaoLuz6=[0.18, 2.2, 0.0, 1.0]  # Ãºltima coord como 0 pra funcionar como vetor da luz direcional
    direcao6 = [2.0, 0.2, 0.0]  # direÃ§Ã£o do vetor do spot

    luzAmbiente7=[0.0,0.0,0.0,1.0]
    luzDifusa7=[0.1, 0.1, 0.1, 0.0]  # ; // "cor"
    luzEspecular7 = [0.0, 0.0, 0.0, 0.0]  #;// "brilho"
    posicaoLuz7=[-0.18, 2.2, 0.0, 1.0]  # Ãºltima coord como 0 pra funcionar como vetor da luz direcional
    direcao7 = [-2.0, 0.2, 0.0]  # direÃ§Ã£o do vetor do spot



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

    # luminaria central - terreo
    glLightfv(GL_LIGHT4, GL_AMBIENT, luzAmbiente4)
    glLightfv(GL_LIGHT4, GL_DIFFUSE, luzDifusa4 )
    glLightfv(GL_LIGHT4, GL_SPECULAR, luzEspecular4 )
    glLightfv(GL_LIGHT4, GL_POSITION, posicaoLuz4 )
    glLightfv(GL_LIGHT4, GL_SPOT_DIRECTION, direcao4); #direcao da luz
    glLightf(GL_LIGHT4, GL_SPOT_CUTOFF, 60); # angulo do cone, de 0 a 180.

    glLightfv(GL_LIGHT5, GL_AMBIENT, luzAmbiente5)
    glLightfv(GL_LIGHT5, GL_DIFFUSE, luzDifusa5 )
    glLightfv(GL_LIGHT5, GL_SPECULAR, luzEspecular5 )
    glLightfv(GL_LIGHT5, GL_POSITION, posicaoLuz5 )
    glLightfv(GL_LIGHT5, GL_SPOT_DIRECTION, direcao5); #direcao da luz
    glLightf(GL_LIGHT5, GL_SPOT_CUTOFF, 60); # angulo do cone, de 0 a 180.

    # luminaria central - superior
    glLightfv(GL_LIGHT6, GL_AMBIENT, luzAmbiente6)
    glLightfv(GL_LIGHT6, GL_DIFFUSE, luzDifusa6 )
    glLightfv(GL_LIGHT6, GL_SPECULAR, luzEspecular6 )
    glLightfv(GL_LIGHT6, GL_POSITION, posicaoLuz6 )
    glLightfv(GL_LIGHT6, GL_SPOT_DIRECTION, direcao6); #direcao da luz
    glLightf(GL_LIGHT6, GL_SPOT_CUTOFF, 50); # angulo do cone, de 0 a 180.

    glLightfv(GL_LIGHT7, GL_AMBIENT, luzAmbiente7)
    glLightfv(GL_LIGHT7, GL_DIFFUSE, luzDifusa7 )
    glLightfv(GL_LIGHT7, GL_SPECULAR, luzEspecular7 )
    glLightfv(GL_LIGHT7, GL_POSITION, posicaoLuz7 )
    glLightfv(GL_LIGHT7, GL_SPOT_DIRECTION, direcao7); #direcao da luz
    glLightf(GL_LIGHT7, GL_SPOT_CUTOFF, 50); # angulo do cone, de 0 a 180.

    


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
        glEnable(GL_LIGHT2)
        glEnable(GL_LIGHT3)
    else:
        glDisable(GL_LIGHT1)
        glDisable(GL_LIGHT2)
        glDisable(GL_LIGHT3)

    if estadoluz2 == 1:
        glEnable(GL_LIGHT4)
        glEnable(GL_LIGHT5)
        
    else:
        glDisable(GL_LIGHT4)
        glDisable(GL_LIGHT5)
        

    if estadoluz3 == 1:
        glEnable(GL_LIGHT6)
        glEnable(GL_LIGHT7)
    else:
        glDisable(GL_LIGHT6)
        glDisable(GL_LIGHT7)

    # Habilita o depth-buffering
    glEnable(GL_DEPTH_TEST)

def tela():
    global angulo
    global distanciamax

    global camX
    global camY
    global camZ
    global alvoCamX
    global alvoCamY
    global alvoCamZ


    glClearColor(0,0,0,0)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Limpar a tela
    glClearColor(1.0, 1.0, 1.0, 1.0) # Limpa a janela com a cor especificada
    glMatrixMode(GL_PROJECTION) # Muda a matriz de projeçao
    glLoadIdentity()# carrega a matriz identidade

    gluPerspective(angulo, 1.77, 0.1, distanciamax) # Especifica a projeção perspectiva

    glMatrixMode(GL_MODELVIEW) # Especifica sistema de coordenadas do modelo
    glLoadIdentity() # Inicializa sistema de coordenadas do modelo

    gluLookAt(camX, camY , camZ,  camX + alvoCamX, alvoCamY, camZ + alvoCamZ, 0, 1, 0)
    print('Camera: (' + str(camX) + ',' + str(camY) + "," + str(camZ) + ')')
    print('Alvo: (' + str(alvoCamX) +','+str(alvoCamY)+',' + str(alvoCamZ) + ')')

   
    
    iluminacao_da_cena()
    #glEnable(GL_DEPTH_TEST) # verifica os pixels que devem ser plotados no desenho 3d

    desenho()                    
    glFlush()                    # Aplica o desenho


def Teclado (tecla, x, y):
    global estadoluz0, estadoluz1, estadoluz2, estadoluz3
    global angulo
    global abertoPorta
    global statusPortRet

    global camX
    global camY
    global camZ
    global alvoCamX
    global alvoCamY
    global alvoCamZ

    print("*** Tratamento de teclas comuns")
    print(">>> Tecla: ",tecla)

    if tecla == b'f':  # A
        camX = -2.5
        camY = 1
        camZ = 0.5
        alvoCamX = 1
        alvoCamY = 1
        alvoCamZ = 0

    if tecla == b'g':
        camX = 0
        camY = -1
        camZ = 5
        alvoCamX = 0
        alvoCamY = -1
        alvoCamZ = -1

    if tecla == b'h':
        camX = 0
        camY = 5
        camZ = 0
        alvoCamX = 0
        alvoCamY = 4
        alvoCamZ = -1
	
    if tecla==chr(27): # ESC ?
        sys.exit(0)

    if tecla == b'k': 
        abertoPorta += 1
        if(abertoPorta == 2):
            abertoPorta = 0

    if tecla == b'm': #portas dos provadores
        statusPortRet += 1
        if(statusPortRet == 2):
            statusPortRet = 0


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
            glEnable(GL_LIGHT2)
            glEnable(GL_LIGHT3)
        else:
            estadoluz1 = 0
            glDisable(GL_LIGHT1)
            glDisable(GL_LIGHT2)
            glDisable(GL_LIGHT3)

    if tecla == b'2': # 1
        if estadoluz2 == 0:
            estadoluz2 = 1
            glEnable(GL_LIGHT4)
            glEnable(GL_LIGHT5)
            
        else:
            estadoluz2 = 0
            glDisable(GL_LIGHT4)
            glDisable(GL_LIGHT5)
            
    if tecla == b'3': # 1
        if estadoluz3 == 0:
            estadoluz3 = 1
            glEnable(GL_LIGHT6)
            glEnable(GL_LIGHT7)
        else:
            estadoluz3 = 0
            glDisable(GL_LIGHT6)
            glDisable(GL_LIGHT7)


    tela()
    glutPostRedisplay()

# Função callback chamada para gerenciar eventos de teclas especiais
def TeclasEspeciais (tecla, x, y):
    global esqdir
    global cimabaixo

    global camX
    global camY
    global camZ
    global alvoCamX
    global alvoCamY
    global alvoCamZ

    print("*** Tratamento de teclas especiais")
    print ("tecla: ", tecla)
    if tecla == GLUT_KEY_F1:
        print(">>> Tecla F1 pressionada")
    elif tecla == GLUT_KEY_F2:
        print(">>> Tecla F2 pressionada")
    elif tecla == GLUT_KEY_F3:
        print(">>> Tecla F3 pressionada")
    elif tecla == GLUT_KEY_LEFT:
        esqdir += 0.1
        alvoCamX = sin(esqdir)
        alvoCamZ = cos(esqdir)
    elif tecla == GLUT_KEY_RIGHT:
        esqdir -= 0.1
        alvoCamX = sin(esqdir)
        alvoCamZ = cos(esqdir)
    elif tecla == GLUT_KEY_UP:
        camX += 0.1 * alvoCamX
        camZ += 0.1 * alvoCamZ
    elif tecla == GLUT_KEY_DOWN:
        camX -= 0.1 * alvoCamX
        camZ -= 0.1 * alvoCamZ
    else:
        print ("Apertou... " , tecla)
    tela()
    glutPostRedisplay()  

def nmX(valor):
	if valor > 3.0:
		valor = 3.0
	elif valor < -3.5:
		valor = -3.5

	return valor

def nmZ(valor):
	if valor > 2.3:
		valor = 2.3
	elif valor < -2.2:
		valor = -2.2

	return valor

def mouseSegurado(x, y):
	global movMan

	movMan = [nmX(x * 0.05), -2.9, nmZ(y * 0.05)]

	glutPostRedisplay()


# PROGRAMA PRINCIPAL

glutInit(argv)
glutInitDisplayMode(GLUT_RGBA | GLUT_DEPTH)
glutInitWindowSize(1200, 700)
glutCreateWindow(b"Projeto CG 2017.2 - Loja")
glutDisplayFunc(tela)
glutMotionFunc(mouseSegurado)
glutKeyboardFunc (Teclado)
glutSpecialFunc (TeclasEspeciais)
glutMainLoop()  # Inicia o laço de eventos da GLUT