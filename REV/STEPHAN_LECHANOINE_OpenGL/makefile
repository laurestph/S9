APPLI= glm.o carre cube quadric modeles robots
all : $(APPLI)

glm.o : glm.h glm.c
	g++ -c glm.c -I. 

carre: carre.c
	g++ carre.c  -o carre glm.o  -I.  -L/usr/X11R6/lib -lGL -lGLU -lglut -lX11 -lXi -lm
cube : cube.c
	g++ cube.c  -o cube  glm.o   -I.  -L/usr/X11R6/lib -lGL -lGLU -lglut -lX11 -lXi -lm
quadric : quadric.c
	g++ quadric.c  -o quadric  glm.o   -I.  -L/usr/X11R6/lib -lGL -lGLU -lglut -lX11 -lXi -lm
modeles : modeles.c
	g++ modeles.c  -o modeles  glm.o   -I.  -L/usr/X11R6/lib -lGL -lGLU -lglut -lX11  -lXi -lm
robots : robots.c
	g++ robots.c  -o robots  glm.o   -I.  -L/usr/X11R6/lib -lGL -lGLU -lglut -lX11 -lXi -lm
clean :
	rm -rf $(APPLI) \#* *. *~
