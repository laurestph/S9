from math import pi,sin,cos

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

def create_joint(radius) :
  longitude,latitude=10,20
  create_sphere(radius,longitude,latitude)

def create_arrow(base,top,height,slices=10,stacks=5) :
  create_stick(base,top,height,slices,stacks)
  glPushMatrix()
  glTranslatef(0,0,height)
  create_cone(base*1.5,height/5.)
  glPopMatrix()

def create_wcs(base,top,height,slices=10,stacks=5) :
  glColor3f(0.0,0.0,1.0)
  create_arrow(base,top,height,slices,stacks)
  
def create_floor(size,tiles=10) :
  tile_size=size/tiles
  for i in range(10+1) :
    for j in range(10+1) :
        glPushMatrix()
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

class Model :
  def __init__(self,size=.01) :
    self.size=size
    self.orientation=0.0
    self.position=[0.0,0.0,0.0]
    self.rot_roue=0
  def set_size(self,size) :
    self.size=size
  def get_size(self) :
    return self.size
  def set_orientation(self,orientation) :
    self.orientation=orientation
  def get_orientation(self) :
    return self.orientation
  def set_position(self,position) :
    self.position=position
  def get_position(self) :
    return self.position

class Car(Model) :
  def __init__(self,size=10) :
    Model.__init__(self,size)
  def create(self) :
    glPushMatrix()
    #glScalef(1,1,2)
    # glutWireCube(self.size)
    # create_arrow(self.size/6.0,self.size/6.0,self.size)
    glPopMatrix()
    
    # roue av droite
    glPushMatrix()
    glRotatef(90,0,1,0)
    glTranslatef(-1.2,0,-1)
    glRotatef(self.rot_roue,0,0,1)
    self.create_wheel()
    glPopMatrix()
    # roue av gauche
    glPushMatrix()
    glRotatef(90,0,1,0)
    glTranslatef(-1.2,0,1)
    glRotatef(self.rot_roue,0,0,1)
    self.create_wheel()
    glPopMatrix()


    # roue ar droite
    glPushMatrix()
    glRotatef(90,0,1,0)
    glTranslatef(1.2,0,-1)
    glRotatef(self.rot_roue,0,0,1)
    self.create_wheel()
    glPopMatrix()
    # roue ar gauche
    glPushMatrix()
    glRotatef(90,0,1,0)
    glTranslatef(1.2,0,1)
    glRotatef(self.rot_roue,0,0,1)
    self.create_wheel()
    glPopMatrix()

  def create_wheel(self,boulons=5) :
    glutWireCube(0.2*self.size)
    angle=360.0/boulons
    for i in range(boulons) :
      glPushMatrix()
      glRotatef(angle*i,0.0,0.0,1.0)
      glTranslatef(0.70*(self.size/2.0),0.0,0.0)
      glutWireCube(0.20*self.size)
      glPopMatrix()

  def create_carrosserie(self):
    base_cylindre = self.size*0.05
    height_cylindre= self.size*0.25
    slices=10
    stacks=5
    glColor3f(0.5,0.2,0.6)
    glPushMatrix()
    glRotatef(180,0,1,0)
    create_disk(0,base_cylindre,slices,stacks)
    glPopMatrix()
    create_cylinder(base_cylindre,base_cylindre,height_cylindre,slices,stacks)
    glPushMatrix()
    glTranslatef(0,0,height_cylindre)
    create_cone(self.size*0.07,2*base_cylindre,slices,stacks)
    glPopMatrix()



class Crane(Model) :
  def __init__(self,size=1.0) :
    Model.__init__(self,size)
    self.arm=30.0               # arm angle rotation
    self.forarm=30.0            # forarm angle rotation
  def set_orientation_arm(self,arm) :
    self.arm=arm
  def get_orientation_arm(self) :
    return self.arm
  def set_orientation_forarm(self,forarm) :
    self.forarm=forarm
  def get_orientation_forarm(self) :
    return self.forarm

  def create(self) :
    # TO DO : crane (une grue) creation
    # Cockpit : a red cube
    # forarm : a green cylinder
    # joint : a red sphere
    # arm :  a green cylinder
##        glColorMaterial (GL_FRONT_AND_BACK,GL_EMISSION)
##        glEnable (GL_COLOR_MATERIAL)
##    glTranslatef(self.position[0],self.position[1],self.position[2])
##    glRotatef(self.orientation,0,1,0)
    glColor3f(1.0,0.0,0.0)
    create_base(self.size)

