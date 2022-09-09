# -*- coding: utf-8 -*-
from sys import argv, exit
from time import sleep
from math import pi,cos,sin

from models import *
from car import *


try:
  from OpenGL.GLUT import *
  from OpenGL.GL import *
  from OpenGL.GLU import *
  import math
except:
  print ("Error: PyOpenGL not installed properly !!")
  sys.exit()

size=0.5
theta_y=0.0

position=[0,0,0]
orientation=0
showAxes=True
xC=1
yC=1
zC=1
r=math.sqrt(xC**2+zC**2)
angleCam=math.pi/4.               #pour avoir une position par défault à 1,1,1 avec la caméra regardant le milieu de la scène

def display() :
#  glClearColor(1.0,1.0,1.0,0.0);
  glClearColor(0.5,0.5,0.5,0.0)
  glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )
  glEnable(GL_DEPTH_TEST)
  glEnable(GL_CULL_FACE)
  glMatrixMode(GL_MODELVIEW)
  glLoadIdentity()
  camera=[xC,yC,zC,0,0,0,0,1,0]
#  camera=[0,0,2,0,0,0,0,1,0]
  gluLookAt(camera[0],camera[1],camera[2], 
            camera[3],camera[4],camera[5],
            camera[6],camera[7],camera[8])
#   #glutWireCube(1)
  # world_coordinate_system(2*size)
  glRotatef(theta_y,0,1,0)
  glPushMatrix()
  if(showAxes):
    create_axes(0.05)
  create_floor(2,12)
  
  glTranslatef(position[0],position[1],position[2])
  glRotatef(orientation,0,1,0)
  car(1)
  #square(size)
  glPopMatrix()
  glutSwapBuffers()

def reshape(width,height) :
  print("reshape width : {}, height : {}".format(width,height))
  glViewport(0,0,width,height)
  glMatrixMode(GL_PROJECTION)
  glLoadIdentity()
  gluPerspective(60.0,width*1.0/height, 1.0, 10.0)

def on_keyboard_action(key,x,y) :
  global size,theta_y, showAxes,xC,yC,zC, angleCam, r
  if key==b'h':
    print("----------------------------------------\n")
    print("Documentation interaction  : Nom-Prenom \n") 
    print("----------------------------------------\n") 
    print("h : afficher cette aide \n")
    print("a : afficher les aretes \n")
    print("f : afficher les facettes \n")
    print("p : afficher les sommets \n")
    print("c/C : afficher les faces CW/CCW \n")
    print("r/R : redimensionner l'objet \n")
    print("y/Y : tourner l'objet autour de l'axe Oy\n")
    print("w/W : cacher/afficher axes\n")
    print("z/s : zoom/dé-zoom ")
    print("q/d : rotation de la caméra")
    print("e : sortie (exit) \n")
  elif key==b'a':
    glPolygonMode(GL_FRONT_AND_BACK,GL_LINE)
  elif key==b'f':
    glPolygonMode(GL_FRONT_AND_BACK,GL_FILL)
  elif key==b'p' :
    glPolygonMode(GL_FRONT_AND_BACK,GL_POINT)
  elif key==b'c' :
    glFrontFace(GL_CW)
  elif key==b'C' :
    glFrontFace(GL_CCW)
  elif key==b'r' :
    size-=0.1
  elif key==b'R' :
    size+=0.1
  elif key==b'y' :
    theta_y-=1.0
  elif key==b'Y' :
    theta_y+=1.0
  elif key==b'e' :
    exit(0)
  elif key==b'w':
    showAxes=False
  elif key==b'W':
    showAxes=True
  elif key==b'z':
    r-=.1
    calculRotation()
  elif key==b's':
    r+=.1
    calculRotation()
  elif key==b'q':
    angleCam+=.1
    calculRotation()
  elif key==b'd':
    angleCam-=.1
    calculRotation()
  else :
    pass
  glutPostRedisplay()


def calculRotation():
  global xC,zC,r  
  xC=r*math.cos(angleCam)
  zC=r*math.sin(angleCam)
  
def on_special_key_action(key,x,y) :
  print("on_special_key_action(key,x,y)")

def on_special_key_action(key,x,y) :
    global position,orientation
    if key ==  GLUT_KEY_UP :
        position[0]+=0.1*size*sin(orientation*pi/180.0)
        position[2]+=0.1*size*cos(orientation*pi/180.0)
    elif  key ==  GLUT_KEY_DOWN :
        position[0]-=0.1*size*sin(orientation*pi/180.0)
        position[2]-=0.1*size*cos(orientation*pi/180.0)
    elif key ==  GLUT_KEY_LEFT :
        orientation+=5
    elif  key ==  GLUT_KEY_RIGHT :
        orientation-=5
    else :
        pass
    glutPostRedisplay()

def animation() :
   print("animation()")

if __name__ == "__main__" :
  glutInit(sys.argv)
  glutInitDisplayMode(GLUT_RGB | GLUT_DEPTH | GLUT_DOUBLE)
  glutInitWindowSize(600,400)
  glutInitWindowPosition(600,300)
  glutCreateWindow("PyOpenGL : Carre")
  glutDisplayFunc(display)
  glutReshapeFunc(reshape)
  glutKeyboardFunc(on_keyboard_action)
  glutSpecialFunc(on_special_key_action)
#   glutIdleFunc(animation)
  glutMainLoop()
