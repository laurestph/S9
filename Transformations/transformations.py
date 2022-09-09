#https://stackoverflow.com/questions/14926798/python-transformation-matrix

from math import sqrt,pi,cos,sin,radians
import numpy as np

def trigo(angle):
  r = radians(angle)
  return cos(r), sin(r)

def matrix(rotation=(0,0,0), translation=(0,0,0)):
  cx, sx = trigo(rotation[0])
  cy, sy = trigo(rotation[1])
  cz, sz = trigo(rotation[2])
  dx = translation[0]
  dy = translation[1]
  dz = translation[2]
  T = np.array([[1, 0, 0, dx],
                [0, 1, 0, dy],
                [0, 0, 1, dz],
                [0, 0, 0,  1]])
  R_X = np.array([[1, 0,  0, 0],
                  [0,cx,-sx, 0],
                  [0,sx, cx, 0],
                  [0, 0,  0, 1]])
  R_Y = np.array([[ cy, 0, sy, 0],
                  [  0, 1,  0, 0],
                  [-sy, 0, cy, 0],
                  [  0, 0,  0, 1]])
  R_Z= np.array([[cz,-sz, 0, 0],
                 [sz, cz, 0, 0],
                 [ 0, 0,  1, 0],
                 [ 0, 0,  0, 1]])
  return np.dot(R_Z,np.dot(R_Y,np.dot(R_X,T))) #  R_Z*(R_Y*(R_X*T))


def transform(point=[0,0,0], matrix=[[1,0,0],[0,1,0],[0,0,1]]):
  p = [0,0,0]
  for r in range(3):
    p[r] += matrix[r][3]
    for c in range(3):
      p[r] += point[c] * matrix[r][c]
  return p

# def transform(point, TransformArray):
#   p = np.array([0,0,0,1])
#   for i in range (0,len(point)-1):
#       p[i] = point[i]
#   p=np.dot(TransformArray,np.transpose(p))
#   for i in range (0,len(point)-1):
#       point[i]=p[i]
#   return point
  
def rotating(r1=(0,0,0),r2=(0,0,0),point=[1,1,1]) :
  print ("p :",point)
  print ("r1 :",r1)
  print ("r2 :",r2)
  m = matrix(r1)
  p = transform(point, m)
  m = matrix(r2) 
  p = transform(p,m)
  print ("resultat : ",p)
  
if __name__ == '__main__':
  print("M identity :")
  print(matrix())
  tr=[0,1,0]
  m_tr=matrix(translation=tr)
  print("M : Oy translation (0,1,0) :")  
  print(m_tr)
  rot=(90,0,0)
  m_rot=matrix(rotation=rot)
  print("M : Ox rotation (90,0,0)  :")
  print(m_rot)
  rotating()
  r1=(180,0,0)
  r2=(0,0,90)
  rotating(r1,r2) 

  r1=(0,0,180)
  r2=(0,90,0)
  rotating(r1,r2) 

  r1=(0,180,0)
  r2=(0,0,90)
  rotating(r1,r2)
  
  r1=(0,0,180)
  r2=(90,0,0)
  rotating(r1,r2) 
  r1=(180,0,0)
  r2=(0,90,0)
  rotating(r1,r2) 

  
##  point=[0,1,0]
##  p=transform(point,m_tr)
##  p=transform(p,m_rot)
##  print("p : ", p)
##  p=transform(point,m_rot)
##  p=transform(p,m_tr)
##  print("p : ", p)

  # r1=(0,0,-90)
  # r2=(180,0,0)
  # rotating(r1,r2) 

##
##
###" OK "
##  r1=(90,0,0)
##  r2=(0,180,0)
##  rotating(r1,r2) 
##
##  r1=(0,90,0)
##  r2=(0,0,180)
##  rotating(r1,r2) 
##
##  r1=(0,0,90)
##  r2=(180,0,0)
##  rotating(r1,r2) 
##
##  r1=(180,0,0)
##  r2=(0,90,0)
##  rotating(r1,r2) 
##
##  r1=(0,180,0)
##  r2=(0,0,90)
##  rotating(r1,r2) 
##
##  r1=(0,0,180)
##  r2=(90,0,0)
##  rotating(r1,r2) 
##
###" KO "
##  r1=(90,0,0)
##  r2=(0,0,180)
##  rotating(r1,r2) 
##
##  r1=(0,90,0)
##  r2=(180,0,0)
##  rotating(r1,r2) 
##
##  r2=(0,0,90)
##  r1=(0,180,0)
##  rotating(r1,r2) 
##
##  r1=(180,0,0)
##  r2=(0,0,90)
##  rotating(r1,r2) 
##
##  r1=(0,180,0)
##  r2=(90,0,0)
##  rotating(r1,r2) 
##
##  r1=(0,0,180)
##  r2=(0,90,0)
##  rotating(r1,r2) 
