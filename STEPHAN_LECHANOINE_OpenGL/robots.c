#include <stdlib.h>
#include <stdio.h>

#include <GL/glut.h>

void initGL(int, char**);
void initGLEvents(void);
void reshape(int, int);
void display(void);

void processNormalKeys(unsigned char, int, int);
void processSpecialKeys(int, int, int);

void worldCoordinateSystem(int);

void create_sphere(GLfloat radius, GLint longitude,GLint latitude);
void create_cylinder(GLdouble base, GLdouble top, GLdouble height);

void create_base(GLfloat);
void create_joint(GLfloat);
void create_link(GLdouble size);

#define SPEED 2

GLint angle=0;

// Camera
// GLfloat camX = 4.0, camY = 5.0, camZ = 10.0;
GLfloat camX = 4.0, camY = 5.0, camZ = 10.0;

// Robot
GLint armX = 0;

void initGL(int argc, char **argv)
{
  glutInit(&argc, argv); 
  glutInitWindowSize(800, 600); 
  glutInitDisplayMode(GLUT_RGB | GLUT_DEPTH | GLUT_DOUBLE);
  glutCreateWindow(argv[0]);

  glClearColor(1.0,1.0,1.0,1.0);
  glEnable(GL_LIGHTING);
  glEnable(GL_LIGHT0);
  glEnable(GL_COLOR_MATERIAL);
  glEnable(GL_TEXTURE_2D);
  glShadeModel(GL_SMOOTH);
}

void initGLEvents(void)
{
  glutDisplayFunc(display); 
  glutReshapeFunc(reshape); 
  glutKeyboardFunc(processNormalKeys); 
  glutSpecialFunc(processSpecialKeys);
}


void display(void)
{
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
  glEnable(GL_DEPTH_TEST);
  glMatrixMode(GL_MODELVIEW) ;
  glLoadIdentity();
  gluLookAt(camX, camY, camZ, 0, 0, 0, 0, 1,0);
  glColor3ub(0,0,0);
  worldCoordinateSystem(3);
 
  glTranslatef(1,0,1);
  glPushMatrix();
    glScalef(2.0, 1.0, 2.0);
    create_base(1.0);
  glPopMatrix();

  glTranslatef(0,1.0,0);
  create_joint(0.4);

  glPushMatrix();
    glRotatef(armX, 0, 0, 1);
    glTranslatef(0,2.5,0);
   glRotatef(90.0, 1, 0, 0);
    glColor3ub(0,0,128);
    create_link(2);
  glPopMatrix();

  glutSwapBuffers();
}

void create_sphere(GLfloat radius, GLint longitude,GLint latitude)
{
  GLUquadric* params = gluNewQuadric();
  gluQuadricDrawStyle(params,GLU_FILL);
  gluQuadricTexture(params,GL_TRUE);
  gluSphere(params,radius,longitude,latitude);
  gluDeleteQuadric(params);
}

void create_cylinder(GLdouble base, GLdouble top, GLdouble height)
{
  GLint slices=10;
  GLint stacks=1;
  GLUquadric* params = gluNewQuadric();
  gluQuadricDrawStyle(params,GLU_FILL);
  gluQuadricTexture(params,GL_TRUE);
  gluCylinder(params,base,top,height,slices,stacks);
  gluDeleteQuadric(params);
}

void create_base(GLfloat size)
{
  glColor3ub(40, 88, 0);
  glutSolidCube(size);
}

void create_joint(GLfloat size)
{
  glColor3ub(88,0,0);
  GLint latitude=10;
  GLint longitude=20;
  GLfloat radius=0.5;
  create_sphere(radius,longitude,latitude);
}


void create_link(GLdouble size)
{
  GLdouble base=0.3;
  GLdouble top=0.3;
  create_cylinder(base,top,size);
}

void reshape(int width, int height)
{
  glViewport(0, 0, width, height);
  glMatrixMode(GL_PROJECTION);
  glLoadIdentity();
  gluPerspective(60.0, (GLfloat)width/(GLfloat)height, 0.1, 128.0);
  glMatrixMode(GL_MODELVIEW);
  glLoadIdentity();
}

void worldCoordinateSystem(int size)
{
  glBegin(GL_LINES);
  glVertex2i(0,0);
  glVertex2i(0,size);
  glVertex2i(0,0);
  glVertex2i(size,0);
  glVertex2i(0,0);
  glVertex3i(0,0,size);
  glEnd();
}

void processNormalKeys(unsigned char key, int x, int y)
{
  switch(key) {
    case 'a' :
      angle  += SPEED;
      angle= angle % 360;
      if ( (angle  >= 90 and angle  < 180) or ( angle >= 270 and angle < 360) ) {
        armX = 90-angle%90;
      }
      else {
        armX = angle%90;
      }
      glutPostRedisplay();
      break;
    case 'h' :
      printf("#----------------------------------------#\n"); 
      printf("# Manual : Dupond-Dupont --------------- #\n"); 
      printf("#----------------------------------------#\n"); 
      printf("a : rotation du bras \n");
      printf("h : help\n");
      printf("q : exit application\n"); 
      break;
    case 'q' :
      exit(0);
    default :
      break;
  }
}

void processSpecialKeys(int key, int x, int y) {
  switch(key) {
    case GLUT_KEY_UP : 
      break;
    default :
      break;
  }
}

int main(int argc, char **argv) {
 
 	initGL(argc, argv);
	initGLEvents();
	glutMainLoop();
	return EXIT_SUCCESS; 
}

