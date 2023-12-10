from common import *
a = get_input()
g = a.grid

seen = set()
def findloop():
    while True:
        for p in g:
            if p not in seen and g[p] not in "S.":
                theloop = [p]
                seen.add(p)
                match g[p]:
                    case "-" | "F" | "L":
                        dir = (1,0)
                    case "|" | "7":
                        dir = (0,1)
                    case "J":
                        dir = (-1, 0)
                break
        while True:
            n = offset(theloop[-1], dir)
            seen.add(n)
            if n == theloop[0]:
                return theloop
            match (g[n], dir):
                case ("-", (1,0) | (-1,0)):
                    pass
                case ("|", (0,1) | (0,-1)):
                    pass
                case ("L", (0,1)):
                    dir = (1,0)
                case ("L", (-1,0)):
                    dir = (0,-1)
                case ("J", (0,1)):
                    dir = (-1,0)
                case ("J", (1,0)):
                    dir = (0,-1)
                case ("7", (1,0)):
                    dir = (0,1)
                case ("7", (0,-1)):
                    dir = (-1,0)
                case ("F", (0,-1)):
                    dir = (1,0)
                case ("F", (-1,0)):
                    dir = (0,1)
                case ("S", _):
                    for t in g.orthagonals(n):
                        dir = (t[0]-n[0], t[1]-n[1])
                        if t in seen:
                            continue
                        match g[t], (t[0]-n[0], t[1]-n[1]):
                            case ("-" | "7" | "J", (1,0)):
                                pass
                            case ("|" | "J" | "L", (0,1)):
                                pass
                            case ("|" | "F" | "7", (0,-1)):
                                pass
                            case ("-" | "L" | "F", (-1,0)):
                                pass
                            case _:
                                continue    
                        break
                case _:
                    break
            theloop.append(n)

loop = findloop()
print(len(loop) // 2)
