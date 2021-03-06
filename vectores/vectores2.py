#  Prereqquisites
#    pip3 install sympy
#  Runner
#  python3 vectores.py
import math
import sympy
from sympy import *
init_printing(use_unicode=True)

rho,theta,z = symbols('rho,theta,z')
x,y,z = symbols('x,y,z')

Arho = 3 * cos(theta)
Atheta = -2 * rho
Az = z

Ax = cos(theta) * Arho - sin(theta) * Atheta
Ay = sin(theta) * Arho + cos(theta) * Atheta


Ay = Ay.subs(rho, sqrt(x*x + y*y))
Ay = Ay.subs(theta, atan(y/x))

Ax = Ax.subs(rho, sqrt(x*x + y*y))
Ax = Ax.subs(theta, atan(y/x))

print(Ax)
print(Ay)
print(Az )

rho,theta,z = symbols('rho,theta,z')
x,y,z = symbols('x,y,z')

Arho = 3 * cos(theta)
Atheta = -2 * rho
Az = z

Ax = cos(theta) * Arho - sin(theta) * Atheta
Ay = sin(theta) * Arho + cos(theta) * Atheta


Ay = Ay.subs(rho, sqrt(x*x + y*y))
Ay = Ay.subs(theta, atan(y/x))
Ay = Ay.subs(y,2*sqrt(3))

Ax = Ax.subs(rho, sqrt(x*x + y*y))
Ax = Ax.subs(theta, atan(y/x))


print(Ax)
print(Ay)
print(Az)


Ay = Ay.subs(x,2)
Ay = Ay.subs(y,2*sqrt(3))

Ax = Ax.subs(x,2)
Ax = Ax.subs(y,2*sqrt(3))

Az = Az.subs(z,5)

print(Ax)
print(Ay)
print(Az)
