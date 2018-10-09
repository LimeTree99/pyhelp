import math, pygame


def round_int(num):
    if num - int(num) < -(num - int(num + 1)):
        return int(num)
    return int(num + 1)

def line_angle(display, colour, point, length, angle, width = 1):
    'does a weird thing where it returns the end point (was needed that time)'
      
    angle = math.radians(angle + 90)

    x = math.sin(angle) * length
    y = math.cos(angle) * length

    endx = round_int(point[0] + x)
    endy = round_int(point[1] + y)

    pygame.draw.line(display, colour, point, (endx, endy), width)
    return endx,endy
        
