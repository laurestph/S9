# from math import pi,sin,cos
try :
  from OpenGL.GLUT import *
  from OpenGL.GL import *
  from OpenGL.GLU import *
except:
  print ("Error: PyOpenGL not installed properly !!")
  sys.exit()

from models import *


def car(size,rot_roue=0,dir_roue=0,rot_grue=0,slices=10,stacks=5):
    base_cylindre = size*0.05
    height_cylindre= size*0.25
    theta = rot_grue
    
    glPushMatrix()
    glTranslatef(0,0,-height_cylindre/2)  #pour avoir la voiture au milieu du repère

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
    
    glPushMatrix()
    glTranslatef(base_cylindre,-base_cylindre*0.2,height_cylindre-size*0.05)
    glRotatef(90,0,1,0)

    #essieu avant
    glPushMatrix()
    glRotatef(rot_roue,0,0,1)
    glRotatef(dir_roue,0,1,0)
    create_roue(size*0.5)
    glTranslatef(0,0,-2*base_cylindre)
    create_roue(size*0.5)
    glPopMatrix()
    
    #essieu arriere
    glPushMatrix()
    glTranslatef(height_cylindre-size*0.1,0,0)
    glRotatef(rot_roue,0,0,1)
    create_roue(size*0.5)
    glTranslatef(0,0,-2*base_cylindre)
    create_roue(size*0.5)
    glPopMatrix()

    glPopMatrix()
    grue(size, theta)
    glPopMatrix()

   

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


def grue(size,theta,slices=10,stacks=5):

  base_cylindre = size*0.025
  height_cylindre= size*0.25/2 #cylindre carrosserie
  size_sphere = size*0.03
  glPushMatrix()
  glColor3f(0.2,0.5,0.7)
  glTranslatef(0,size*0.05,height_cylindre/2)
  create_cylinder(base_cylindre,base_cylindre,height_cylindre,slices,stacks)
  glPushMatrix()

  glRotatef(theta,0,0,1)

  # #articulation 3
  # glPushMatrix()
  # glTranslatef(0,height_cylindre*2+size_sphere,height_cylindre/2)
  # articulation(size_sphere,base_cylindre,height_cylindre,-90)
  # glPopMatrix()

  #articulation 2
  glPushMatrix()
  glTranslatef(0,height_cylindre+size_sphere+base_cylindre,height_cylindre/2)
  articulation(size_sphere,base_cylindre,height_cylindre,-90+theta)
  glPopMatrix()

  #articulation 1
  glPushMatrix()
  glTranslatef(0,base_cylindre*2,height_cylindre/2)
  articulation(size_sphere,base_cylindre,height_cylindre,-90)
  glPopMatrix()

  glPopMatrix()

  glPopMatrix()

def articulation(size,base_cylindre,height_cylindre,rotate=-90):
  glPushMatrix()
  glColor3f(0.9,0.5,0)
  glPushMatrix()
  glRotatef(rotate,1,0,0)
  create_cylinder(base_cylindre*0.8,base_cylindre*0.8,height_cylindre)
  glColor3f(0.1,0.9,0)
  glPopMatrix()
  create_sphere(size)

  glPopMatrix()

