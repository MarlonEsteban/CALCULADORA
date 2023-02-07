import cmath as cm
import math
def suma_comp(comp_num):
    real_sum = 0
    imag_sum = 0
    for real, imag in comp_num:
        real_sum += real
        imag_sum += imag
    return (real_sum, imag_sum)

def res_comp(com_num):
    real_res = com_num[0][0]
    imag_res = com_num[0][1]
    for real, imag in com_num[1:]:
        real_res -= real
        imag_res -= imag
    return (real_res, imag_res)

