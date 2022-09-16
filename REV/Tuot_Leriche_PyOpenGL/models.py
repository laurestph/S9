# from math import pi,sin,cos
try :
  from OpenGL.GLUT import *
  from OpenGL.GL import *
  from OpenGL.GLU import *
except:
  print ("Error: PyOpenGL not installed properly !!")
  sys.exit()

def create_base(size) :
  glutSolidCube(size)

def create_sphere(radius) :
  longitude,latitude=10,20
  params=gluNewQuadric()
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

def create_axe(size) :
    create_disk(0,0.1)
    create_cylinder(0.05,0.05,0.4)
    glPushMatrix()
    glTranslatef(0,0,0.4)
    create_cone(0.07,0.2)
    glPopMatrix()
    
def world_coordinate_system(size) :
  glBegin(GL_LINES)
  glColor3ub(255,255,255)
  glVertex2f(0,0)
  glVertex2f(0,size)
  glVertex2f(0,0)
  glVertex2f(size,0)
  glVertex2f(0,0)
  glVertex3f(0,0,size)
  glEnd()

def create_floor(size,tiles=10) :
  tile_size=size/tiles
  for i in range(10+1) :
    for j in range(10+1) :
        glPushMatrix()
#        glTranslatef(-size/2.0+tile_size*i,-1.0,-size/2.0+tile_size*j)
        glTranslatef(-size/2.0+tile_size*i,0.0,-size/2.0+tile_size*j)
        if (i+j)%2 == 0 :
            glColor3f(1.0,1.0,1.0)
            glRotatef(-90,1,0,0)
            glRectf(-tile_size/2.0, -tile_size/2.0, tile_size/2.0, tile_size/2.0)
        else :
            glColor3f(0.0,0.0,0.0)
            glRotatef(90,1,0,0)
            glRectf(-tile_size/2.0, -tile_size/2.0, tile_size/2.0, tile_size/2.0)
        glPopMatrix()

def square(size) :
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
  glEnd()
#face arriere : couleur uniforme White
  glBegin(GL_POLYGON)
  glVertex2f(-size,-size)
  glVertex2f(-size,size)
  glVertex2f(size,size)
  glVertex2f(size,-size)
  glEnd()

def wheels(theta_x, theta_y):
  glPushMatrix()
  glRotatef(theta_y,0,1,0)
  glRotatef(theta_x,0,0,1)
  glColor3f(0,0,0)
  create_disk(0,0.1)
  glColor3f(0.5,0.5,0.5)
  glTranslatef(0.0,0.0,0.001) 
  create_disk(0,0.05)
  glColor3f(0.2,0.2,0.2) 
  glTranslatef(0.0,0.03,0.001) 
  
  
  create_disk(0,0.01)
  glTranslatef(0.03,-0.03,0.001) 
  create_disk(0,0.01)
  glTranslatef(-0.03,-0.03,0.0) 
  create_disk(0,0.01)
  glTranslatef(-0.03,0.03,0.0) 
  create_disk(0,0.01)
  glPopMatrix()


def create_articulation() :

 glPushMatrix()
 glColor3f(0,0,0)
 glTranslatef(0,0,0)
 create_sphere(0.04)
 glPopMatrix()

 glPushMatrix()
 glTranslatef(0,0.18,0)
 glRotatef(90,1,0,0)
 glColor3f(0,1,1)
 create_cylinder(0.03,0.03,0.15)
 glPopMatrix()
 glColor3f(1,1,0)

def create_pince() :

 glPushMatrix()
 glColor3f(0.6,0.2,0.8)
 glTranslatef(0,0.62,0.6)
 create_cone(0.05,0.1)
 glPopMatrix()


def create_crane():
 
 glPushMatrix()
 glTranslatef(0,0.27,0.275)
 create_articulation()
 glPopMatrix()

 glPushMatrix()
 glTranslatef(0,0.47,0.275)
 glRotatef(45,1,0,0)
 create_articulation()
 glPopMatrix()

 glPushMatrix()
 glTranslatef(0,0.62,0.42)
 glRotatef(90,1,0,0)
 create_articulation()
 glPopMatrix()

 create_pince()
 

def car(size,rotation_wheels,rotation_boulon) :

  glTranslatef(0,0.2,0)
  create_disk(1,0.1)
  glColor3f(0,0.5,0)
  create_cylinder(0.1,0.1,0.7)
  glPushMatrix()
  glTranslatef(0,0.11,0.15)
  glColor3f(0,0,1)
  create_cylinder(0.05,0.05,0.25)
  glPopMatrix()
  glColor3f(1,0,1)
  glPushMatrix()
  glTranslatef(0,0,0.7)
  glColor3f(0,0,0)
  create_cone(0.15,0.2)
  glPopMatrix()
  glTranslatef(0,-0.1,0)
  
  #roue côté par defaut
  glPushMatrix()
  glTranslatef(0.1,0,0.1)
  wheels(rotation_boulon,90)
  glTranslatef(0,0,0.4)
  #devant
  wheels(rotation_boulon,90+rotation_wheels)
  glPopMatrix()

  #grue 
  create_crane()
 
  #roue autre côté 
  glPushMatrix()
  glTranslatef(-0.1,0,0.1)
  wheels(rotation_boulon,-90)
  glTranslatef(0,0,0.4)
  #devant
  wheels(rotation_boulon,-90+rotation_wheels)
  glPopMatrix()

  glTranslatef(rotation_boulon,-0.1,0)

