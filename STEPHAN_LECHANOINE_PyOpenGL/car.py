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
    xcar = 0.
    ycar = 0.

    test = True

    base_cylindre = size*0.05
    height_cylindre= size*0.25

    #voiture
    glPushMatrix()
    glTranslatef(xcar,ycar,0)

    #roues
    glPushMatrix()

    glTranslatef(base_cylindre,-base_cylindre*0.2,height_cylindre-size*0.05)
    glRotatef(90,0,1,0)
    create_roue(size*0.5)
    glTranslatef(height_cylindre-size*0.1,0,0)
    create_roue(size*0.5)
    glTranslatef(0,0,-2*base_cylindre)
    create_roue(size*0.5)
    glTranslatef(-height_cylindre+size*0.1,0,0)
    create_roue(size*0.5)
    glPopMatrix()

    #carrosserie
    glColor3f(0.5,0.2,0.6)
    glPushMatrix()
    glRotatef(180,0,1,0)
    create_disk(0,base_cylindre,slices,stacks)
    glPopMatrix()
    create_cylinder(base_cylindre,base_cylindre,height_cylindre,slices,stacks)
    glPushMatrix()
    glTranslatef(0,0,height_cylindre)
    create_cone(size*0.07,2*base_cylindre,slices,stacks)
    glPopMatrix()
    glPopMatrix()
    if (test):
      glTranslatef(0.2,0.3,0)
      create_roue(4)

def create_roue(size):
    sizeroue = size*0.6
    create_boulons(size)
    create_jante(sizeroue*0.1)
    glColor3f(0.0,0.0,0.0)
    glutSolidTorus(sizeroue*0.025,sizeroue*0.1,int(sizeroue*100),int(sizeroue*100))

def create_boulons(size):
    glPushMatrix()

    # glColor3f(0.2,0.6,0.0)
    # create_cylinder(size*0.01,size*0.01,size*0.001)
    glColor3f(0.4,0.2,0.0)
    glTranslatef(size*0.02,size*0.02,0.01)
    create_disk(0,size*0.01)
    glPopMatrix()
    #print("create_boulons")

def create_jante(size):
    glPushMatrix()
    glColor3f(0,0.7,0.2)
    create_disk(0,size)
    glRotatef(180,0,1,0)
    glTranslatef(0,0,size*0.05)
    create_disk(0,size)
    glPopMatrix()