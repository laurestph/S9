# -*- coding: utf-8 -*-
from sys import argv, exit
from time import sleep
from math import pi,sin,cos,sqrt
from quaternions import Quaternion
from models import *
try:
  from OpenGL.GLUT import *
  from OpenGL.GL import *
  from OpenGL.GLU import *
  import math
except:
  print ("Error: PyOpenGL not installed properly !!")
  sys.exit()

size=0.5
theta=0
to_translate=1,1,1
length=5
y_angle=0.0
camera=[length*sin(y_angle*pi/180.0),0,length*cos(y_angle*pi/180.0),
        0,0,0,
        0,1,0]
wcs=False
sphere=False
q1_to_translate=0.0,0.0,0.0
y_plane=False

def glut_init() :
  glutInit(sys.argv)
  glutInitDisplayMode(GLUT_RGB | GLUT_DEPTH | GLUT_DOUBLE)
  glutInitWindowSize(1200,1000)
  glutInitWindowPosition(100,100)
  glutCreateWindow(sys.argv[0])

def glut_event():
  glutDisplayFunc(display)
  glutReshapeFunc(reshape)
  glutKeyboardFunc(on_normal_key_action)
  glutSpecialFunc(on_special_key_action)
  # glutIdleFunc(animation)
 
def gl_init() :
#  glClearColor(1.0,1.0,1.0,0.0);
  glClearColor(0.0,0.0,0.0,0.0)
  glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )
  glEnable(GL_DEPTH_TEST)
  glEnable(GL_CULL_FACE)


def display() :
  global wcs,sphere
  global q1_to_translate
  gl_init()
  glMatrixMode(GL_MODELVIEW)
  glLoadIdentity()
#  camera=[4,3,2,0,0,0,0,1,0]
  gluLookAt(camera[0],camera[1],camera[2], 
            camera[3],camera[4],camera[5],
            camera[6],camera[7],camera[8])
##  gluLookAt(0,0,length, 
##            0,0,0,
##            0,1,0)
##https://openclassrooms.com/fr/courses/167717-creez-des-programmes-en-3d-avec-opengl/167148-controle-avance-de-la-camera-partie-2-2
  if wcs :
    create_wcs(0.05*size,0.05*size,size)
 ##  create_sphere(0.8)
  glColor3f(1.0,1.0,0.0)  
  glutWireCube(1)
  if sphere :
    glPushMatrix()
    glRotatef(90.0,1,0,0)  
    glColor3f(0.0,1.0,1.0)  
    glutWireSphere(sqrt(3)/2.,10,10)
    glPopMatrix()

  if y_plane :
    glPushMatrix()
    glRotatef(-45.0,0,1,0)  
    glColor3f(0.0,1.0,0.0)  
    square_sized(size*sqrt(2))
    glColor3f(0.0,0.0,1.0)  
    glColor3f(0.0,1.0,1.0)  
    create_arrow(0.1*size,0.1*size,size)
    glPopMatrix()
  
  glPushMatrix()                #  sphere at (0.5,0.5,0.5)
  glTranslatef(0.5,0.5,0.5)
  glColor3f(1.0,1.0,1.0)  
  create_sphere(size/5.,10,20)
  glPopMatrix()

  glPushMatrix()
  glTranslatef(-0.5,-0.5,-0.5)  #  sphere at (-0.5,-0.5,-0.5)
  glColor3f(1.0,1.0,1.0)  
  create_sphere(size/5.,10,20)
  glPopMatrix()

  glPushMatrix()                #  sphere to animate
  x,y,z=q1_to_translate
  glColor3f(0.0,1.0,0.0)  
  glTranslatef(x,y,z)
  latitude,longitude=10,10
  create_sphere(size/5.,latitude,longitude)
  glPopMatrix()
  glutSwapBuffers()

def reshape(width,height) :
  glViewport(0,0, width,height)
  glMatrixMode(GL_PROJECTION)
  glLoadIdentity()
  gluPerspective(60.0,width*1.0/height, 1.0, 10.0)


def point_to_quaternion(point) :
  q0,q1,q2,q3=point
  a=complex(q0,q1)
  b=complex(q2,q3)
  q=Quaternion(a,b)
  return q

def rotation_to_quaternion(theta,axe) :
  q0=cos(theta/2.)
  q1,q2,q3=axe
  q1,q2,q3=sin(theta/2.)*q1,sin(theta/2.)*q2,sin(theta/2.)*q3
  a=complex(q0,q1)
  b=complex(q2,q3)
  q=Quaternion(a,b)
  return q  

# OPenGL WCS point conversion 
def xyz_to_zxy(point) :
  x,y,z=point
  z,x,y=x,y,z
  return x,y,z

def animation() :
  global theta
  global q1_to_translate
  theta=theta+0.01
  delta=0.5
  point=[0,delta,delta,delta]
  p=point_to_quaternion(point)

  axe=[sqrt(2)/2,-sqrt(2)/2,0.0]
  q1=rotation_to_quaternion(theta,axe)
  resultat=(q1*p)*q1.inverse()
  q1_to_translate=resultat.get_point()
  q1_to_translate=xyz_to_zxy(q1_to_translate)
  glutPostRedisplay()
    
def on_normal_key_action(key, x, y) :
  global wcs,sphere
  global size,camera,theta
  global x_plane,y_plane,z_plane
  if key==b'h':
    print("a/A : lancer/stopper l'animation \n")
    print("----------------------------------------\n")
    print("Documentation interaction  : Nom-Prenom \n") 
    print("----------------------------------------\n") 
    print("h : afficher cette aide \n");
    print("f : afficher les facettes \n")
    print("e : afficher les aretes \n")
    print("s : afficher les sommets \n")
    print("c/C : afficher les faces CW/CCW \n")
    print("p  : afficher/rendre invisible  la sphere \n")
    print("r/R : redimensionner les objets \n")
    # print("x/X : afficher l'axe de rotation [0.0,-sqrt(2)/2,sqrt(2)/2] \n")
    print("y : afficher/rendre invisible l'axe de rotation [-sqrt(2)/2,0.0,sqrt(2)/2] \n")
    # print("z/Z : afficher l'axe de rotation [-sqrt(2)/2,sqrt(2)/2.],0.0\n")
    print("w : afficher/rendre invisible le repère de scène \n")
    print("e : sortie (exit) \n")
  elif key== b'a':
    glutIdleFunc(animation)
  elif key== b'A':
    glutIdleFunc(None)
  elif key== b'f':
    glPolygonMode(GL_FRONT_AND_BACK,GL_FILL)
  elif key== b'e':
    glPolygonMode(GL_FRONT_AND_BACK,GL_LINE)
  elif key== b'v' :
    glPolygonMode(GL_FRONT_AND_BACK,GL_POINT)
  elif key== b'c' :
    glFrontFace(GL_CW)
  elif key== b'C' :
    glFrontFace(GL_CCW)
  elif  key == b'p' :
    sphere=not(sphere)
  elif key== b'r' :
    size-=0.1
  elif key== b'R' :
    size+=0.1
  elif key== b'y' :
    y_plane=not(y_plane)
  elif key== b'w' :
    wcs=not(wcs)
  elif  key == b't' :
    theta=theta-0.1
  elif  key == b'T' :
    theta=theta+0.1
  elif key== b'e' :
    exit(0)
  else :
    pass
  glutPostRedisplay()

def on_special_key_action(key, x, y) :
    global length, y_angle,x_position,z_position
    if key ==  GLUT_KEY_UP :
        length-=0.1
    elif  key ==  GLUT_KEY_DOWN :
        length+=0.1
    elif key ==  GLUT_KEY_LEFT :
        if  y_angle > 360.0:
          y_angle=0.0
        y_angle+=1
    elif  key ==  GLUT_KEY_RIGHT :
        if  y_angle < -360.0  :
          y_angle=0
        y_angle-=1
    camera[0]=length*sin(y_angle*pi/180.0)
    camera[2]=length*cos(y_angle*pi/180.0)
    glutPostRedisplay()

    

if __name__ == "__main__" :
    glut_init()
    glut_event() 
    glutMainLoop()
