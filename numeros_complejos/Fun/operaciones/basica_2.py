import math

def multiply_polar_coordinates(r, theta):
    r_result = r[0]
    theta_result = theta[0]
    for i in range(1, len(r)):
        r_result *= r[i]
        theta_result += theta[i]
    return (r_result, math.degrees(math.radians(theta_result) % 360))

