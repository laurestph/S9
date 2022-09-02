/*****************************************************/
/*                     cube.c                        */
/*****************************************************/
/* Premiers pas avec OpenGL.                         */
/* Objectif : afficher, interagir et animer un cube  */
/*****************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <GL/glut.h>
#include "glm.h"

static float size=0.5;
static float theta_y=0.0;
static float theta_x=0.0;
static float theta_z=0.0;
static float theta_y_local=0.0;
static float x0=0.0;

void gl_init(void);
void glut_init(int argc,char **argv);
void glut_event(void);

void display(void);
void keyboard(unsigned char key,int x,int y);
void reshape(int width, int height);

void wcs(float size);
void carre(float size);
void cube(float size);


void glut_init(int argc,char **argv)
{
 glutInit(&argc,argv);
// glutInitDisplayMode(GLUT_RGB);
 glutInitDisplayMode(GLUT_RGB | GLUT_DEPTH | GLUT_DOUBLE);
 glutInitWindowPosition(200,200);
 glutInitWindowSize(250,250);
 glutCreateWindow(argv[0]);
}


void glut_event(void)
{
 glutDisplayFunc(display);
 glutKeyboardFunc(keyboard);
 glutReshapeFunc(reshape);
}

void wcs(float size) {
 glBegin(GL_LINES);
 glColor3f(1.0,1.0,1.0);
 glVertex2f(0.0,0.0);
 glVertex2f(0.0,1.5*size);
 glVertex2f(0.0,0.0);
 glVertex2f(1.5*size,0.0);
 glVertex2f(0.0,0.0);
 glVertex3f(0.0,0.0,1.5*size);
 glEnd();
}
void cube(float size)
{
 glBegin(GL_QUADS);
 glColor3ub(255,0,0);            // face rouge
 glVertex3d(size,size,size);
 glVertex3d(size,size,-size);
 glVertex3d(-size,size,-size);
 glVertex3d(-size,size,size);
 glColor3ub(0,255,0);            // face verte
 glVertex3d(size,-size,size);
 glVertex3d(size,-size,-size);
 glVertex3d(size,size,-size);
 glVertex3d(size,size,size); 
 glColor3ub(0,0,255);            // face bleue
 glVertex3d(-size,-size,size);
 glVertex3d(-size,-size,-size);
 glVertex3d(size,-size,-size);
 glVertex3d(size,-size,size); 
 glColor3ub(255,255,0);          // face jaune
 glVertex3d(-size,size,size);
 glVertex3d(-size,size,-size);
 glVertex3d(-size,-size,-size);
 glVertex3d(-size,-size,size);
 glColor3ub(0,255,255);          // face cyan
 glVertex3d(size,size,-size);
 glVertex3d(size,-size,-size);
 glVertex3d(-size,-size,-size);
 glVertex3d(-size,size,-size);
 glColor3ub(255,0,255);          // face magenta
 glVertex3d(size,-size,size);
 glVertex3d(size,size,size);
 glVertex3d(-size,size,size);
 glVertex3d(-size,-size,size);
 glEnd();
}

void gl_init(void)
{
 glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
 glEnable(GL_CULL_FACE);
 glClearColor(0.0,0.0,0.0,0.0);
 glColor3f(1.0,1.0,1.0);
 glPointSize(2.0);
}

void display() {
 gl_init();
 glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
 glEnable(GL_CULL_FACE);
// glCullFace (GL_BACK);
// glCullFace (GL_FRONT);
// glFrontFace(GL_CCW);
 glMatrixMode(GL_MODELVIEW);
 glLoadIdentity();
// gluLookAt(0,0,2,0,0,0,0,1,0);
 gluLookAt(4,3,2,0,0,0,0,1,0);
// glutWireCube(1);
 wcs(size+1);
 //rotation
 glRotatef(theta_x,1,0,0);

 glRotatef(theta_y,0,1,0);
 glRotatef(theta_z,0,0,1);
 glTranslatef(x0,0,0);
 //glLoadIdentity();
 glRotatef(theta_y_local,0,1,0);

 cube(size);
 glutSwapBuffers();
}

void reshape(int width, int height) {
 glViewport(0,0, (GLsizei) width, (GLsizei) height);
 glMatrixMode(GL_PROJECTION);
 glLoadIdentity();
 gluPerspective(60.0, (GLfloat) width/(GLfloat) height, 1.0, 10.0);
 glEnable(GL_DEPTH_TEST);
}

void animate(void)
{
   theta_y_local+=1;
   theta_y+=1;
   glutPostRedisplay();
}

void keyboard(unsigned char key,int x,int y)
{
 switch (key) 
 {
  case 'h': 
   printf("----------------------------------------\n"); 
   printf("Documentation interaction  : Nom-Prenom \n"); 
   printf("----------------------------------------\n"); 
   printf("h : afficher cette aide \n"); 
   printf("f : afficher les facettes \n"); 
   printf("e : afficher les aretes \n"); 
   printf("v : afficher les sommets \n"); 
   printf("c/C : afficher les faces CW/CCW \n"); 
   printf("s/S : redimensionner l'objet \n"); 
   printf("y/Y : tourner l'objet autour de l'axe Oy\n"); 
   printf("d/g : tourner l'objet autour de l'axe Ox\n"); 
   printf("z/Z : tourner l'objet autour de l'axe Oz\n"); 
   printf("o : faire tourner le cube autour du centre de repere de scène dans le plan (Oxz)\n");
   printf("r : reset les rotations\n");  
   printf("t/T : translater selon l'axe 0x\n");
   printf("m/M : tourner l'objet sur lui même selon l'axe Oy\n");
   printf("a/A : lancer/stopper l'animation\n");
   printf("x : sortie (exit) \n"); 
  case 'f': 
   glPolygonMode(GL_FRONT_AND_BACK,GL_FILL);
   break;
  case 'e':
   glPolygonMode(GL_FRONT_AND_BACK,GL_LINE);
   break;
  case 'v' :
   glPolygonMode(GL_FRONT_AND_BACK,GL_POINT);
   break;
  case 'c' :// glutWireCube(1);

   glFrontFace(GL_CW);
   break;
  case 'C' : 
   glFrontFace(GL_CCW);
   break;
  case 's' : 
   size-=0.01;
   break;
  case 'S' : 
   size+=0.01;
   break;
  case 'y' : 
   theta_y-=1.0;
   break;
  case 'Y' : 
   theta_y+=1.0;
   break;
case 'd' : 
   theta_x+=1.0;
   break;
  case 'g' : 
   theta_x-=1.0;
   break;
   case 'z' : 
   theta_z+=1.0;
   break;
  case 'Z' : 
   theta_z-=1.0;
   break;
  case 't':
   x0+=1.0;
   break;
  case 'T':
   x0-=1.0;
   break;
  case 'o':
  theta_y+=1.0;
   break;
   case 'r':
    theta_x=0;
    theta_y=0;
    theta_z=0;
    x0=0;
    theta_y_local=0;
   break;

  case 'm':
   theta_y_local+=1.0;
   break;
  case 'M':
   theta_y_local-=1.0;
   break;
  case 'x' :
   exit(0);
  case 'a':
   x0=1;
   theta_x=0;
   theta_y=0;
   theta_z=0;
   glutIdleFunc(animate);
   break;

   case 'A':
   glutIdleFunc(NULL);
   break;
  default :
   break;
 }
 glutPostRedisplay();
}

int main(int argc,char **argv)
{
 glut_init(argc,argv);
 glut_event();
 glutMainLoop();
 return 0;
}

