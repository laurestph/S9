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
    xcar = 0.5
    ycar = 0.2
    # create_roue(size)
    glPushMatrix()
    glTranslatef(xcar,ycar,0)
    glPushMatrix()
    glRotatef(90,0,1,0)
    glTranslatef(xcar*size*0.05,0,0)
    create_roue(size*0.5)
    #voiture
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
    glColor3f(0.2,0.6,0.0)
    create_cylinder(size*0.1,size*0.1,size*0.3)
    #print("create_boulons")

