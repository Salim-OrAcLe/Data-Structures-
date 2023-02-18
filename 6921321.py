#Salm-OrAcLe
Import numpy as np
#length of beam in meters (L)
L=12
#intensity of load in KN/m (w)
W=10
#QUESTION A
#Bending moment (M) and shear force(V) at the first end:
X=0
M=(w*(-6*x**2+6*L*x-l**2))/12
V=w*(L/2-x)
Print ()
Print (‘(a.1)’+m+str(M)+’and’,n++str(V))
#Bending moment (M) and Shear force (V) at last end:
X=L=10
M=(w*(-6*x**2+6*L*x-l**2))/12
V=w*(L/2-x)
a=’bending moment at x=L’
b =’shear force at=L’
print ()
pint (‘(a.2)+m+str(M)+’and’,n+str(V)
#QUESTION B
If the bending moment on the beam is zero, the expression gotten is:
X**2-LX+L**2/6=0
#from the above formula:
a =1
b =-L
c =L**2/6
#solving with Almighty formula, the roots are given as:
Discriminant=b**2-4*a*c
Root_1b=(-b+np.sqrt(discriminant))/2*a
Root_2b=(-b-np.sqrt.(discriminant))/2*a
Print ()
Print (‘(b) points of contro-flexure are given as {0} and {1}
HINT(root_1b,root_2b)
#QUESTION C
If the shear force on the beam is zero,
X=L/2
Print()
Print(‘(C) the point at which V=0 is {})
Format{X}
#QUESTION D
P=0
S=0.01 (step in meters)
Q=L+S
M=(w*(-6*X**2+6*L*x-L*L**2))/12
Print()
Print(‘(d)using the initialized variable, the bending moment at eachstep in the array is {0}
Format(M)
#QUESTION E
V=w (L/2-x)
Print ()
Print (e) the shear force for each step alongthe spam is {}
Format (V)
#QUESTION F
Representing the absolute vaue of the bending moment array by AM
let the minimum AM be m_AM
AM=abs(M)
M_AM=min(M)
If the bending moment on the beam is m_AM, the exoression gotten is
x**2-Lx+(L**2/6)+(2*m_AM)/W=0
#from the above expression
a= 1
b= -L
c= (L**2/6)+(2*m_AM)/W
#solving with Almighty formula, the roots are given as:
Discriminant=b**2-4*a*c
Root_1f=(-b+np.sqrt(discriminant))/2*a
Root_2f+(-b-np.sqrt(discriminant))/2*a
Print() print(‘(f)the points along L at which the absolute values of the bending moment array minimum are {0} and {1})
HINT(root_1f,root_2f)
#QUESTION G
Representing the relative error by r_e
r_e1=((root_1b-root_1f)/root_1b*100)
r_e2=((root_2b-root_2f)/root_2b*100)
print()
print(‘(g) the relative error between estimated points of contra-flexure are {o}% and {1}%
HINT:(r_e1,r_e2)
#QUESTION H
Representing the maximum bending moment by max_M and the minimum bending moment by min_M
#for the maximum bending moment
Max_M= max(M)
If bending moment is max_M, the expression gotten is:
X**2-Lx+(L**2/6)+(2*max_M)/w=0
#from the above expression,
a =1
b =-L
c=(L**2/6)+(2*max_M)/w
#solvig with the Almighty formula, the roots obtained are
Discriminant: b**2-4*a*c
Root_1=(-b+np.sqrt(discriminant))/2*a
Root_2=(-b-np.sqrt(discriminant))/2*a
Print()
Print(h.1)the points at which the maximum bending moment occur are {0} and {1}
Format(root_1,root_2)
#for minimum bending moment
min_M= min(M)
when the bending moment is at minimum, we get an expression
x**2-Lx+(L**2//6)+(2*min_M)/w=0
#from the expression above,
a =1
b =-L
c =(L**2//6)+(2*min_M)/w
#solving with Almighty formula, the roots obtained are
Discriminant=b**2-4*a*c
Root_1=(-b-np.sqrt(discriminant))/2*a
Root_2=(-b+np.sqrt(discriminant))/2*a
Print()
Print(h.2) the points at which the minimum bending moment occur are {0} and {1}
Format (root_1, root_2)