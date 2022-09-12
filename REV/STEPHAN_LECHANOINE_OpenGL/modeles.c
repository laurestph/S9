/*************************************************************************************/
/*  D'après un  cours de Xavier Michelon                                             */
/* http://download.tuxfamily.org/linuxgraphic/archives/section3d/openGL/didacticiels */
/* et un turoriel d'Openclassroom sur OpenGL                                                           */
/* https://openclassrooms.com/courses/creez-des-programmes-en-3d-avec-opengl/enfin-de-la-3d-partie-2-2 */
/*************************************************************************************/
/*                     cube.c                        */
/*****************************************************/
/*  Premiers pas avec OpenGL.                        */
/* Objectif : afficher a l'ecran un carre en couleur */
/*****************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <GL/glut.h>
#include "glm.h"

static float size=0.5;
static float theta_y=0.0;

GLMmodel* pmodel = NULL;

void gl_init(void);
void glut_init(int argc,char **argv);
void glut_event(void);

void display(void);
void keyboard(unsigned char key,int x,int y);
void reshape(int width, int height);

void wcs(int size);
void carre(float size);
void cube(float size);
void model_load(void);

int main(int argc,char **argv)
{
 gl_init();
 glut_init(argc,argv);
 glut_event();
 glutMainLoop();
 return 0;
}
void gl_init(void)
{
 glClearColor(0.0,0.0,0.0,0.0);
 glColor3f(1.0,1.0,1.0);
 glPointSize(2.0);
}
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

void wcs(int size) {
 glBegin(GL_LINES);
 glColor3f(1.0,1.0,1.0);  // White
 if (size > 1.0)
 {
  glVertex2i(0,0);
  glVertex2i(0,1.5*size);
  glVertex2i(0,0);
  glVertex2i(1.5*size,0);
  glVertex2i(0,0);
  glVertex3i(0,0,1.5*size);
 }
 else
 {
  glVertex2i(0,0);
  glVertex2i(0,1);
  glVertex2i(0,0);
  glVertex2i(1,0);
  glVertex2i(0,0);
  glVertex3i(0,0,1);
 }
 glEnd();
}
void reshape(int width, int height) {
 glViewport(0,0, (GLsizei) width, (GLsizei) height);
 glMatrixMode(GL_PROJECTION);
 glLoadIdentity();
 gluPerspective(60.0, (GLfloat) width/(GLfloat) height, 1.0, 10.0);
 glEnable(GL_DEPTH_TEST);
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

void model_load(void)
{
 if (!pmodel) {
  char * model="dolphins.obj";
  pmodel = glmReadOBJ(model);
  if (!pmodel) exit(0);
  glmUnitize(pmodel);
  glmFacetNormals(pmodel);
  glmVertexNormals(pmodel, 90.0);
 }
 glmDraw(pmodel, GLM_SMOOTH | GLM_MATERIAL);
}

void display() {
 glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
 glEnable(GL_CULL_FACE);
// glCullFace (GL_BACK);
// glCullFace (GL_FRONT);
// glFrontFace(GL_CCW);

 static float blanc[] = { 1.0F,1.0F,1.0F,1.0F };
 static float rouge[] = { 1.0F,0.0F,0.0F,1.0F };
 static float vert[] = { 0.0F,1.0F,0.0F,1.0F };
 static float bleu[] = { 0.0F,0.0F,1.0F,1.0F };
 static float gris[] = { 0.25F,0.25F,0.25F,1.0F };
 static float noir[] = { 0.0F,0.0F,0.0F,1.0F };

 glEnable(GL_LIGHT0);
 glEnable(GL_LIGHTING);
 GLfloat pos[4] = {-0.5,0.0,3.0,0.0};
 glLightfv (GL_LIGHT0, GL_AMBIENT, noir);
 glLightfv (GL_LIGHT0, GL_DIFFUSE, blanc);
 glLightfv (GL_LIGHT0, GL_SPECULAR, blanc);
 glLightfv (GL_LIGHT0, GL_POSITION, pos);

 glMatrixMode(GL_MODELVIEW);
 glLoadIdentity();
 gluLookAt(4,3,2,0,0,0,0,1,0);
// gluLookAt(0,0,2,0,0,0,0,1,0);
 glRotatef(theta_y,0,1,0);
// glutWireCube(1);
// wcs(size);
// carre(size);
 glScalef(size,size,size);
 model_load();
 glutSwapBuffers();
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
   size-=0.01;
   break;
  case 'S' : 
   size+=0.01;
   break;
  case 'y' : 
   theta_y-=1.0;   // CW rotation
   break;
  case 'Y' : 
   theta_y+=1.0;  // CCW rotation
   break;
  case 'x' :
   exit(0);
  default :
   break;
 }
 glutPostRedisplay();
}

