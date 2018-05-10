

# 1. Draw an English Ruler

def draw_ruler(num_inches, major_length):
    draw_line(major_length,'0')
    for i in range(1, 1+num_inches):
        draw_interval(major_length-1)
        draw_line(major_length,str(i))


def draw_line(major_length,tick_lable):
    line = '-' * major_length
    if tick_lable:
        line += ' '+ tick_lable
    print(line)


def draw_interval(center_length):
    if center_length>0:
        draw_interval(center_length - 1)
        draw_line(center_length, '')
        draw_interval(center_length - 1)


draw_ruler(3, 5)

# binary search
