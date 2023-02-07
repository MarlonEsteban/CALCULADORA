import cmath as cm
import math 
def impedancia(f, L):
    j = complex(0, 1)
    Zl = j * 2 * math.pi * f * L
    magnitude =round(abs(Zl),5)
    phase = cm.phase(Zl)
    angulo= 90
    print("")
    print(f"El valor del inductor en fasor es:",magnitude,",", angulo,"º")
    print("")
    print(f"El valor del inductor en coordenadas rectangulares es:",cm.rect(magnitude, angulo))


