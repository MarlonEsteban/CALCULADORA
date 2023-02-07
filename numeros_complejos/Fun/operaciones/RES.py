import cmath as cm
import math

def res_equ_pa(resistencias):
    total = 0
    for resistencia in resistencias:
        total += 1/resistencia
    return 1/total
