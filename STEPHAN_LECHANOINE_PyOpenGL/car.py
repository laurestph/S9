# from math import pi,sin,cos
try :
  from OpenGL.GLUT import *
  from OpenGL.GL import *
  from OpenGL.GLU import *
except:
  print ("Error: PyOpenGL not installed properly !!")
  sys.exit()

from models import *

def car(size,slices=10,stacks=5):
  # create_roue(size)
    glPushMatrix()
    glTranslatef(0.5,0.2,0)
    glPushMatrix()
    glTranslatef(0,0.1,0)
    create_jante(size*0.25)
    create_roue(size*0.5)
    glPopMatrix()
    glColor3f(0.5,0.2,0.6)
    glPushMatrix()
    glRotatef(180,0,1,0)
    create_disk(0,size*0.05,slices,stacks)
    glPopMatrix()
    create_cylinder(size*0.05,size*0.05,size*0.25,slices,stacks)
    glPushMatrix()
    glTranslatef(0,0,size*0.25)
    create_cone(size*0.07,2*size*0.05,slices,stacks)
    glPopMatrix()

    glPopMatrix()

def create_roue(size):
    sizeroue = size*0.6
    glColor3f(0.0,0.0,0.0)
    glutSolidTorus(sizeroue*0.05,sizeroue*0.1,int(sizeroue*100),int(sizeroue*100))
    #print("create_roue")

def create_boulons(size):
    glPushMatrix()
    glColor3f(0.2,0.6,0.0)
    create_cylinder(size*0.01,size*0.01,size*0.001)
    glTranslatef(0,0,size*0.01)
    create_disk(0,size*0.01)
    glPopMatrix()
    #print("create_boulons")

def create_jante(size):
    glPushMatrix()
    glColor3f(1,1,1)
    glPushMatrix()
    create_boulons(size)
    glPopMatrix()
    glPushMatrix()
    glTranslatef(0,0,size*0.05)
    create_disk(0,size*0.1)
    glPopMatrix()
    glPopMatrix()