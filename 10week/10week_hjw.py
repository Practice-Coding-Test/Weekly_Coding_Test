from itertools import combinations

def get_dot(eq1, eq2):
    if eq1[0] * eq2[1] - eq1[1] * eq2[0] == 0:
        return None
    x = (eq1[1] * eq2[2] - eq1[2] * eq2[1]) / (eq1[0] * eq2[1] - eq1[1] * eq2[0])
    y = (eq1[2] * eq2[0] - eq1[0] * eq2[2]) / (eq1[0] * eq2[1] - eq1[1] * eq2[0])
    return x, y

def solution(line):
    eq = list(combinations(line, 2))
    dots = list(set([dot for dot in [get_dot(l[0], l[1]) for l in eq if get_dot(l[0], l[1])] if
                     dot[0].is_integer() == True and dot[1].is_integer() == True]))
    max_x, min_x, max_y, min_y = int(max([d[0] for d in dots])), int(min([d[0] for d in dots])), int(
        max([d[1] for d in dots])), int(min([d[1] for d in dots]))
    answer = [['.' for x in range(max_x - min_x + 1)] for y in range(max_y - min_y + 1)]
    for dot_x, dot_y in dots:
        answer[max_y - int(dot_y)][int(dot_x) - min_x] = "*"
    return ["".join(a) for a in answer]