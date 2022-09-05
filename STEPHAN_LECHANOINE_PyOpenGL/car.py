# from math import pi,sin,cos
try :
  from OpenGL.GLUT import *
  from OpenGL.GL import *
  from OpenGL.GLU import *
except:
  print ("Error: PyOpenGL not installed properly !!")
  sys.exit()

from models import *

def car(size):
    # glColor3f(0.1,0.8,0.6)
    # create_stick(0.2,0.5,0.5)
    # glTranslatef(0,0,12*size)
    # glColor3f(0.0,1.0,0.5)
    # create_stick(0.5,0.5,0.5)
    create_roue(size)

def create_roue(size):
    glColor3f(0.0,0.0,0.0)
    glTranslatef(size*0.2,size*0.5,0)
    glutSolidTorus(size*0.05,size*0.1,size*100,size*100)
    print("create_roue")

def create_boulons(size):
    glColor3f(0.2,0.6,0.0)
    create_cylinder(size*0.1,size*0.1,size*0.3) 
    print("create_boulons")

