import cmath as cm
import math

def impedan(f, C):
    j = complex(0, 1)
    Zc = 1 / (j * 2 * math.pi * f * C)
    magnitude = round(abs(Zc),5)
    phase = cm.phase(Zc)
    angulo= -90
    print("")
    print(f"El valor del capacitor en fasor es:",magnitude,",", angulo,"º")
    print("")
    print(f"El valor del capacitor en coordenadas rectangulares es:",cm.rect(magnitude, angulo))
    print("")



