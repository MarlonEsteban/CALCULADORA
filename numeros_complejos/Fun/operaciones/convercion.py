import cmath as cm
import math as m
def polar_a_rectangular(valor,angulo):
   rect=cm.rect(valor,m.radians(angulo))
   print("Sus soordenadas rectagulares son:",round(rect.real,3),",",round(rect.imag,3),"j")

def rectangular_a_polar(x, y):
  polar = cm.polar(complex(x, y))
  return (polar[0], m.degrees(polar[1]))

def convercion(x, y):
  coordenadas = rectangular_a_polar(x, y)
  print("Coordenadas polares: r =", round(coordenadas[0],3), "θ =", round(coordenadas[1],3), "°")






   

  
