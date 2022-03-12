bloks = {1: '░', 2: '▒', 3: '▓'}

def draw_carpet(w, h):
    line= ''
    for i in range(h):
        line += bloks[3]
        if i == 0 or i == h - 1:
            for j in range(w - 2): 
                line += bloks[1]
        else:
            for k in range(w - 2):
                if k == 0 or k == w - 3:
                    line += bloks[1]
                else:
                    line += bloks[2]
        line += bloks[3] + '\n'
    print(line)
    return line

draw_carpet(11, 4)

