# coding: utf-8

from math import pi,sin,cos

try :
  from OpenGL.GLUT import *
  from OpenGL.GL import *
  from OpenGL.GLU import *
except:
  print ("Error: PyOpenGL not installed properly !!")
  sys.exit()

from models import create_axes, create_wcs,create_floor,Car,Crane

def gl_init() :
#  glClearColor(1.0,1.0,1.0,0.0);
  glClearColor(0.5,0.5,0.5,0.0)
  glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )
  glEnable(GL_DEPTH_TEST)
  glEnable(GL_CULL_FACE)

def glut_init() :
  glutInit(sys.argv)
  glutInitDisplayMode(GLUT_RGB | GLUT_DEPTH | GLUT_DOUBLE)
  glutInitWindowSize(1200,1000)
  glutInitWindowPosition(100,100)
  glutCreateWindow(sys.argv[0])

def glut_event(scene):
  glutDisplayFunc(scene.display)
  glutReshapeFunc(scene.reshape)
  glutKeyboardFunc(scene.on_keyboard_action)
  glutSpecialFunc(scene.on_special_key_action);
##  glutIdleFunc(scene.animation)

class Scene :
  def __init__(self,size) :
    self.size=size
    self.model=Car(size)
##    self.camera=[0,0,5,0,0,0,0,1,0]    
    self.camera=[2,3,1,0,0,0,0,1,0]    
    self.perspective=[60.0,1.0,0.1,50.0]
    self.rotation_y=0.0
    self.show_axes=True
  def display(self) :
    gl_init()
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    posx,posy,posz=self.camera[0],self.camera[1],self.camera[2]
    dirx,diry,dirz=self.camera[3],self.camera[4],self.camera[5]
    vupx,vupy,vupz=self.camera[6],self.camera[7],self.camera[8]
    gluLookAt(posx,posy,posz,dirx,diry,dirz,vupx,vupy,vupz)
    glRotatef(self.rotation_y,0,1,0)
    # axes
    if(self.show_axes):
      create_axes(self.size*0.01)
    # le sol
    create_floor(10*self.size) 
    # l'objet à saisir
    glPushMatrix()
    glTranslatef(-3,0.5,3)
    glRotatef(45,0,1,0)
    glColor3f(1.0,0.0,1.0)
    glutSolidTeapot(self.size/5.0)
    glPopMatrix()
    # le modele a manipuler
    position=self.model.get_position()
    orientation=self.model.get_orientation()
    glPushMatrix()
    glTranslatef(position[0],position[1],position[2])
    glRotatef(orientation,0,1,0)
    self.model.create()
    glPopMatrix()
    glutSwapBuffers()

  def reshape(self,width,height) :
    glViewport(0,0, width,height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    self.perspective[1]=width*1.0/height
    fovy,ratio,near,far=self.perspective
    gluPerspective(fovy,ratio,near,far)

  def on_keyboard_action(self,key, x, y) :
    if key=='a':
      glutIdleFunc(scene.animation)
    elif key==b'A':
      glutIdleFunc(None)
    elif key==b'h':
      print("----------------------------------------") 
      print("Documentation interaction  : Nom-Prenom ") 
      print("h : afficher cette aide")
      print("e : sortie d'application")
      print("----------------------------------------") 
      print("---------") 
      print("Affichage")
      print("---------") 
      print("a/A : lancer/Stopper l'animation")
      print("c/C : faces CW/CCW")
      print("f/F : faces/Aretes")
      print("s/S : redimensionner la scene")
      print("r/R : revenir à l'etat initial (camera et grue)")
      print("w/W : afficher/cacher le repere de scene")
      print("------") 
      print("Camera")
      print("------") 
      print("n/N : deplacement en Oz")
      print("d/D : modifier le direction de visee de camera dans la plan Oxz")
      print("----") 
      print("Voiture")
      print("----")
      print("fleches up/down : avancer/reculer la voiture sur le plan")
      print("fleches left/right : tourner la voiture dans le plan")
      print("----") 
      print("Grue")
      print("----")
      print("b/B : faire pivoter le bras")
      print("g/G : faire pivoter l'avant-bras")
      print("...: ....")
      print("----") 
      print("...")
      print("----")
      print("...: ....")
     
    elif key==b'b' :
      pass
    elif key==b'B':
      pass
    elif key==b'g' :
      pass
    elif key==b'G':
      pass
    elif key==b'e' :
      exit(0)   
    elif key==b'f':
      glPolygonMode(GL_FRONT_AND_BACK,GL_FILL)
    elif key==b'F':
      glPolygonMode(GL_FRONT_AND_BACK,GL_LINE)
    elif key==b'c' :
      glFrontFace(GL_CW)
    elif key==b'C' :
      glFrontFace(GL_CCW)
    elif key==b's' :
      self.size+=0.1
    elif key==b'S' :
      self.size-=0.1
    elif  key ==b'u' :
      pass
    elif  key ==b'U' :
      pass
    elif  key ==b'v' :
      pass
    elif  key ==b'V' :
      pass
    elif  key ==b'n' :
      self.camera[2]=self.camera[2]-0.1
    elif  key ==b'N' :
      self.camera[2]=self.camera[2]+0.1
    elif key == b'd':
      self.camera[4]+=0.1
    elif key ==b'D':
      self.camera[4]-=0.1  
    elif  key ==b'w' :
      self.show_axes=False
    elif  key ==b'W' :
      self.show_axes=True
    else :
      pass
    glutPostRedisplay()

  def on_special_key_action(self,key, x, y) :
    position=self.model.get_position()
    orientation=self.model.get_orientation()
    if key ==  GLUT_KEY_UP :
        position[0]+=0.1*self.size*sin(orientation*pi/180.0)
        position[2]+=0.1*self.size*cos(orientation*pi/180.0)
        self.model.rot_roue+=10
        self.model.dir_roue=0
    elif  key ==  GLUT_KEY_DOWN :
        position[0]-=0.1*self.size*sin(orientation*pi/180.0)
        position[2]-=0.1*self.size*cos(orientation*pi/180.0)
        self.model.rot_roue-=10
        self.model.dir_roue=0
    elif key ==  GLUT_KEY_LEFT :
        orientation+=5
        self.model.dir_roue=25
    elif  key ==  GLUT_KEY_RIGHT :
        orientation-=5
        self.model.dir_roue=-25
    else :
        pass
    self.model.set_position(position)
    self.model.set_orientation(orientation)
    glutPostRedisplay()

  def animation(self) :
    self.rotation_y+=0.1
    if self.rotation_y > 360.0 :
      self.rotation_y-=360
    glutPostRedisplay()

if __name__ == "__main__" :
   glutInit(sys.argv)
   glutInitDisplayMode (GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
   glutInitWindowSize (500, 500)
   glutInitWindowPosition (100, 100)
   glutCreateWindow ("REV 2223 A : Dupond Dupont ")
   glClearColor(1.0,1.0,1.0,1.0)
   dimension=2.0
   scene=Scene(dimension)
   glut_event(scene)
   glutMainLoop()
