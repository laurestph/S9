/*************************************************************************************/
/*  D'après un  cours de Xavier Michelon                                             */
/* http://download.tuxfamily.org/linuxgraphic/archives/section3d/openGL/didacticiels */
/*************************************************************************************/
/*                     carre.c                        */
/********************************************************/
/*  Premiers pas avec OpenGL.                         */
/* Objectif : afficher a l'ecran un carre en couleur  */
/******************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <GL/glut.h>
#include "glm.h"

float size=0.5;
float theta_y=0.0;
float spin=0.0;
float pos_z=2.0;

void gl_init(void);
void glut_init(int argc,char **argv);
void glut_event(void);

void display(void);
void keyboard(unsigned char key,int x,int y);
void reshape(int width, int height);
void animation(void);


void wcs(int size);
void carre(float size);

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
 // glutIdleFunc(animation);
}

void animation(void)
{
 printf("idle %f\n",spin);
 spin = spin + 0.5;
 if (spin > 360.0) spin = spin -360.0;
 glutPostRedisplay();
}

void wcs(float size) {
 glBegin(GL_LINES);
 glColor3ub(255,255,255);
 glVertex2f(0.0,0.0);
 glVertex2f(0.0,size);
 glVertex2f(0.0,0.0);
 glVertex2f(size,0.0);
 glVertex2f(0.0,0.0);
 glVertex3f(0.0,0.0,size);
 glEnd();
}

void carre(float size)
{
 // face avant : sommets de couleurs RGBW
 glBegin(GL_POLYGON);
 glColor3f(1.0,0.0,0.0);  // Red 
 glVertex2f(-size,-size);
 glColor3f(0.0,1.0,0.0);  // Green
 glVertex2f(size,-size);
 glColor3f(0.0,0.0,1.0);  // Blue
 glVertex2f(size,size);
 glColor3f(1.0,1.0,1.0);  // White
 glVertex2f(-size,size);
 glEnd();
 // face arriere : couleur uniforme White
 glBegin(GL_POLYGON);
 glVertex2f(-size,-size);
 glVertex2f(-size,size);
 glVertex2f(size,size);
 glVertex2f(size,-size);
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
 glMatrixMode(GL_MODELVIEW);
 glLoadIdentity();
// gluLookAt(0,0,2,0,0,0,0,1,0);
 gluLookAt(4,3,2,0,0,0,0,1,0);
// glutWireCube(1);
 wcs(size+1);
 //glRotatef(spin,1,0,0);
 glRotatef(theta_y,0,1,0);
 carre(size);
 glutSwapBuffers();
}

void reshape(int width, int height) {
 glViewport(0,0, (GLsizei) width, (GLsizei) height);
 glMatrixMode(GL_PROJECTION);
 glLoadIdentity();
 gluPerspective(60.0, (GLfloat) width/(GLfloat) height, 1.0, 10.0);
 glEnable(GL_DEPTH_TEST);
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
  case 'c' :
   glFrontFace(GL_CW);
   break;
  case 'C' : 
   glFrontFace(GL_CCW);
   break;
  case 's' : 
   size-=0.1;
   break;
  case 'S' : 
   size+=0.1;		
   break;
  case 'y' : 
   theta_y-=1.0;
   break;
  case 'Y' : 
   theta_y+=1.0;
   break;
  case 'x' :
   exit(0);
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


