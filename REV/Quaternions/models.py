# -*- coding: utf-8 -*-
from sys import argv, exit
from time import sleep
from math import pi,sin,cos,sqrt
from quaternions import Quaternion

try:
  from OpenGL.GLUT import *
  from OpenGL.GL import *
  from OpenGL.GLU import *
  import math
except:
  print ("Error: PyOpenGL not installed properly !!")
  sys.exit()

def square_colored(size) :
# face avant : sommets de couleurs RGBW
  glBegin(GL_POLYGON)
  glColor3f(1.0,0.0,0.0)   # Red 
  glVertex2f(-size,-size)
  glColor3f(0.0,1.0,0.0)   # Green
  glVertex2f(size,-size)
  glColor3f(0.0,0.0,1.0)   # Blue
  glVertex2f(size,size)
  glColor3f(1.0,1.0,1.0)   #  White
  glVertex2f(-size,size)
  glEnd();
#face arriere : couleur uniforme White
  glBegin(GL_POLYGON)
  glVertex2f(-size,-size)
  glVertex2f(-size,size)
  glVertex2f(size,size)
  glVertex2f(size,-size)
  glEnd()

def square_sized(size) :
# face avant 
  glBegin(GL_POLYGON)
  glVertex2f(-size,-size)
  glVertex2f(size,-size)
  glVertex2f(size,size)
  glVertex2f(-size,size)
  glEnd();
#face arriere 
  glBegin(GL_POLYGON)
  glVertex2f(-size,-size)
  glVertex2f(-size,size)
  glVertex2f(size,size)
  glVertex2f(size,-size)
  glEnd()

def square(p1,p2,p3,p4) :
# face avant 
  glBegin(GL_POLYGON)
  glVertex3f(p1[0],p1[1],p1[2])
  glVertex3f(p2[0],p2[1],p2[2])
  glVertex3f(p3[0],p3[1],p3[2])
  glVertex3f(p4[0],p4[1],p4[2])
  glEnd();
#face arriere 
  glBegin(GL_POLYGON)
  glVertex3f(p1[0],p1[1],p1[2])
  glVertex3f(p4[0],p4[1],p4[2])
  glVertex3f(p3[0],p3[1],p3[2])
  glVertex3f(p2[0],p2[1],p2[2])
  glEnd()

def wcs_lines(size) :
  glBegin(GL_LINES)
  glColor3ub(255,255,255)
  glVertex2f(0,0)
  glVertex2f(0,size)
  glVertex2f(0,0)
  glVertex2f(size,0)
  glVertex2f(0,0)
  glVertex3f(0,0,size)
  glEnd()

def create_sphere(radius,longitude=10,latitude=5) :
  params = gluNewQuadric()
  gluQuadricDrawStyle(params,GLU_FILL)
  gluQuadricTexture(params,GL_TRUE)
  gluSphere(params,radius,longitude,latitude)
  gluDeleteQuadric(params)

def create_cylinder(base,top,height,slices=10,stacks=5) :
  params=gluNewQuadric()
  gluQuadricDrawStyle(params,GLU_FILL)
  gluQuadricTexture(params,GL_TRUE)
  gluCylinder(params,base,top,height,slices,stacks)
  gluDeleteQuadric(params)

def create_disk(inner,outer,slices=10,loops=5) :
  params=gluNewQuadric()
  gluQuadricDrawStyle(params,GLU_FILL)
  gluQuadricTexture(params,GL_TRUE)
  gluDisk(params,inner,outer,slices,loops)
  gluDeleteQuadric(params)

def create_stick(base,top,height,slices=10,stacks=5) :
  glPushMatrix()
  glRotatef(180,0,1,0)
  create_disk(0,base,slices,stacks)
  glPopMatrix()
  create_cylinder(base,top,height,slices,stacks)
  glPushMatrix()
  glTranslatef(0,0,height)
  create_disk(0,base,slices,stacks)
  glPopMatrix()

def create_cone(base,height,slices=10,stacks=5) :
  glPushMatrix()
  glRotatef(180,0,1,0)
  create_disk(0,base,slices,stacks)
  glPopMatrix()
  create_cylinder(base,0,height,slices,stacks)

def create_arrow(base,top,height,slices=10,stacks=5) :
  create_stick(base,top,height,slices,stacks)
  glPushMatrix()
  glTranslatef(0,0,height)
  create_cone(base*1.5,height/5.)
  glPopMatrix()

def create_wcs(base,top,height,slices=10,stacks=5) :
  glColor3f(0.0,0.0,1.0)  
  create_arrow(base,top,height,slices,stacks)   # Z axis
  glPushMatrix()
  glRotatef(90,0,1,0) # X axis
  glColor3f(1.0,0.0,0.0)  
  create_arrow(base,top,height,slices,stacks)
  glPopMatrix()
  glPushMatrix()
  glRotatef(-90,1,0,0) # X axis
  glColor3f(0.0,1.0,0.0)  
  create_arrow(base,top,height,slices,stacks)
  glPopMatrix()
  
  create_stick(base,top,height,slices,stacks)
  glPushMatrix()
  glTranslatef(0,0,height)
  create_cone(base*1.05,height/5.)
  glPopMatrix()
