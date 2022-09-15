# from math import pi,sin,cos
try :
  from OpenGL.GLUT import *
  from OpenGL.GL import *
  from OpenGL.GLU import *
except:
  print ("Error: PyOpenGL not installed properly !!")
  sys.exit()

from models import *


def roues_avant(size):
    base_cylindre = size*0.05
    height_cylindre= size*0.25
    #roues
    glPushMatrix()
    glTranslatef(base_cylindre,-base_cylindre*0.2,height_cylindre-size*0.05)
    glRotatef(90,0,1,0)
    create_roue(size*0.5)
    glTranslatef(height_cylindre-size*0.1,0,0)
    #create_roue(size*0.5)
    glTranslatef(0,0,-2*base_cylindre)
    #create_roue(size*0.5)
    glTranslatef(-height_cylindre+size*0.1,0,0)
    create_roue(size*0.5)
    glPopMatrix()

def roues_arriere(size):
    base_cylindre = size*0.05
    height_cylindre= size*0.25
    #roues arriere
    glPushMatrix()
    glTranslatef(base_cylindre,-base_cylindre*0.2,height_cylindre-size*0.05)
    glRotatef(90,0,1,0)
    #create_roue(size*0.5)
    glTranslatef(height_cylindre-size*0.1,0,0)
    create_roue(size*0.5)
    glTranslatef(0,0,-2*base_cylindre)
    create_roue(size*0.5)
    glTranslatef(-height_cylindre+size*0.1,0,0)
    #create_roue(size*0.5)
    glPopMatrix()

def carrosserie(size,slices=10,stacks=5):

    base_cylindre = size*0.05
    height_cylindre= size*0.25
    
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
  

def create_roue(size):
    sizeroue = size*0.6
    create_boulons(size)
    create_jante(sizeroue*0.1)
    glColor3f(0.0,0.0,0.0)
    glutSolidTorus(sizeroue*0.025,sizeroue*0.1,int(sizeroue*100),int(sizeroue*100))

def create_boulons(size):
    boulons = 4 
    angle = 360./boulons

   
    # glColor3f(0.2,0.6,0.0)
    glColor3f(0.4,0.2,0.0)
    for i in range(boulons):
      glPushMatrix()
      glRotate(angle*i,0,0,1)
      glPushMatrix()
      glRotatef(180,0,1,0)
      glTranslatef(0.05*(size/2),0,size*0.005)
      create_disk(0,size*0.01)
      glPopMatrix()
      glPushMatrix()
      glTranslatef(0.05*(size/2),0,size*0.005)
      create_disk(0,size*0.01)
      glPopMatrix()
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