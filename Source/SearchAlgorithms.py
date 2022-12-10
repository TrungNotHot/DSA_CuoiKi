from Space import *
from Constants import *
from pygame.locals import *
import math

def findFather(g: Graph, cur: Node, father, sc: pygame.Surface):
    if cur == g.start:
        wait()
    pygame.draw.line(sc, green, (cur.x, cur.y), (
        g.grid_cells[father[cur.value]].x, g.grid_cells[father[cur.value]].y))
    if cur.color not in [orange, purple]:
        cur.set_color(grey)
    g.draw(sc)
    return findFather(g, g.grid_cells[father[cur.value]], father, sc)


def wait():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN and event.key == K_f:
                return


def findDistance(a:Node,b:Node):
    return math.sqrt( (a.x-b.x)**2+(a.y-b.y)**2 )


def DFS(g: Graph, sc: pygame.Surface):
    print('Implement DFS algorithm')

    open_set = [g.start.value]  # stack
    closed_set = []
    father = [-1]*g.get_len()

    for indx in range(0, len(father)):
        if (len(open_set) == 0):
            break
        if (open_set[-1] in father):
            open_set.pop(-1)
            continue

        father[indx] = open_set.pop(-1)
        if g.grid_cells[father[indx]].color not in [orange, purple]:
            g.grid_cells[father[indx]].set_color(yellow)
            g.draw(sc)

        if g.is_goal(g.grid_cells[father[indx]]):
            for i in range(indx):
                pygame.draw.line(sc, green, (g.grid_cells[father[i]].x, g.grid_cells[father[i]].y), (
                    g.grid_cells[father[i+1]].x, g.grid_cells[father[i+1]].y))
                if g.grid_cells[father[i]].color not in [orange, purple]:
                    g.grid_cells[father[i]].set_color(grey)
                g.draw(sc)
            wait()

        for neighbor in g.get_neighbors(g.grid_cells[father[indx]]):
            if neighbor.value not in closed_set:
                # Thứ tự ưu tiên tăng dần từ up, down, left, right, up_left, up_right, down_left, down_right
                open_set.append(neighbor.value)
                if neighbor.color == green:
                    neighbor.set_color(red)
                    g.draw(sc)

        closed_set.append(father[indx])

        if g.grid_cells[father[indx]].color not in [orange, purple]:
            g.grid_cells[father[indx]].set_color(blue)
            g.draw(sc)

    raise NotImplementedError('Not implemented')


def BFS(g: Graph, sc: pygame.Surface):
    print('Implement BFS algorithm')

    open_set = [g.start.value]  # queue
    closed_set = []
    father = [-1]*g.get_len()

    for indx in range(0, len(father)):
        if (len(open_set) == 0):
            break
        current = open_set.pop(0)

        if g.grid_cells[current].color not in [orange, purple]:
            g.grid_cells[current].set_color(yellow)
            g.draw(sc)

        if g.is_goal(g.grid_cells[current]):
            findFather(g, g.grid_cells[current], father, sc)

        for neighbor in g.get_neighbors(g.grid_cells[current]):
            if neighbor.value not in closed_set:
                if neighbor.color == green:
                    # Thứ tự thêm là: up, down, left, right, up_left, up_right, down_left, down_right
                    open_set.append(neighbor.value)
                    neighbor.set_color(red)
                    father[neighbor.value] = current
                    g.draw(sc)
                if neighbor.color == purple:
                    open_set.append(neighbor.value)
                    father[neighbor.value] = current

        closed_set.append(current)

        if g.grid_cells[current].color not in [orange, purple]:
            g.grid_cells[current].set_color(blue)
            g.draw(sc)

    raise NotImplementedError('Not implemented')


def UCS(g: Graph, sc: pygame.Surface):
    print('Implement UCS algorithm')

    open_set = {}
    open_set[g.start.value] = 0
    closed_set: list[int] = []
    father = [-1]*g.get_len()
    cost = [100_000]*g.get_len()
    cost[g.start.value] = 0


    for indx in range(0, len(father)):
        if (len(open_set) == 0):
            break
        current = min(open_set, key=open_set.get)
        open_set.pop(current)

        if g.grid_cells[current].color not in [orange, purple]:
            g.grid_cells[current].set_color(yellow)
            g.draw(sc)

        if g.is_goal(g.grid_cells[current]):
            findFather(g, g.grid_cells[current], father, sc)

        for neighbor in g.get_neighbors(g.grid_cells[current]):
            if neighbor.value not in closed_set:
                distance=findDistance(neighbor,g.grid_cells[current])
                if cost[current]+distance<cost[neighbor.value]:
                    cost[neighbor.value]=cost[current]+distance
                    open_set[neighbor.value]=cost[neighbor.value]
                    father[neighbor.value] = current
                if neighbor.color==green:
                    neighbor.set_color(red)
                    g.draw(sc)

        closed_set.append(current)

        if g.grid_cells[current].color not in [orange, purple]:
            g.grid_cells[current].set_color(blue)
            g.draw(sc)
    raise NotImplementedError('Not implemented')
