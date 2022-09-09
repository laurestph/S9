## https://fr.wikibooks.org/wiki/Math%C3%A9matiques_avec_Python_et_Ruby/Quaternions_et_octonions_en_Python

from math import hypot,pi,sin,cos,sqrt

class Quaternion:
  def __init__(self,a,b) :
    self.a=a
    self.b=b
    
  def __str__(self):
    aff='('
    aff+=str(self.a.real)+')+('
    aff+=str(self.a.imag)+')i+('
    aff+=str(self.b.real)+')j+('
    aff+=str(self.b.imag)+')k'
    return aff
    
  def __repr__(self):
    aff='('
    aff+=str(self.a.real)+')+('
    aff+=str(self.a.imag)+')i+('
    aff+=str(self.b.real)+')j+('
    aff+=str(self.b.imag)+')k'
    return aff
    
  def __neg__(self):
    return Quaternion(-self.a,-self.b)
    
  def __add__(self,other):
    return Quaternion(self.a+other.a,self.b+other.b)
    
  def __sub__(self,other):
    return Quaternion(self.a-other.a,self.b-other.b)
    
  def __mul__(self,other):
    c=self.a*other.a-self.b*other.b.conjugate()
    d=self.a*other.b+self.b*other.a.conjugate()
    return Quaternion(c,d)
    
  def __rmul__(self,k):
    return Quaternion(self.a*k,self.b*k)
    
  def __abs__(self):
    return hypot(abs(self.a),abs(self.b))
    
  def conjugate(self):
    return Quaternion(self.a.conjugate(),-self.b)

  def inverse(self):
    q=self.conjugate()
    q.set_a(q.get_a()/abs(self)**2)
    q.set_b(q.get_b()/abs(self)**2)
    return q
    
  def __div__(self,other):
    return self*(1./abs(other)**2*other.conjugate())
    
  def __pow__(self,n):
    r=1
    for i in range(n):
      r=r*self
    return r

  def get_a(self) :
    return self.a
  def set_a(self,a) :
    self.a=a
  def get_b(self) :
    return self.b
  def set_b(self,b) :
    self.b=b
  
  def get_point(self) :
    return self.a.imag,self.b.real,self.b.imag

if __name__ == "__main__" :
  p0,p1,p2,p3=0,1,1,1                 
  a=complex(p0,p1)
  b=complex(p2,p3)
  p=Quaternion(a,b)

  print("Quaternion : ",p)
  print("conjugate : ",p.conjugate())
  print("module : ",abs(p))
  inverse=(1/abs(p)**2)*p.conjugate()
  print("inverse : ",inverse)
  print("q*inverse : ",p*inverse)

  # p=Quaternion(a,b)         # p : point a mettre en rotation
  print("point p to quaternion (P): ",p)

  theta=pi
  q0=cos(theta/2.)                  
  q1,q2,q3=0.0,-sqrt(2)/2,sqrt(2)/2
  q1,q2,q3=sin(theta/2.)*q1,sin(theta/2.)*q2,sin(theta/2.)*q3
  a=complex(q0,q1)
  b=complex(q2,q3)
  q=Quaternion(a,b)        # q : axe de rotation    
  print("axe q to quaternion  (Q) : ",q)
  qp=q*p
  print("Q*P : ",qp)
  result=qp*q.inverse()
  print("Q*P*Q^1 : ",result)
  print("result : ",result.get_point())

