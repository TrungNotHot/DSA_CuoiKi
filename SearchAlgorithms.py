from Space import *
from Constants import *
from pygame.locals import *
def wait():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN and event.key == K_f:
                return
def DFS(g:Graph, sc:pygame.Surface):
    print('Implement DFS algorithm')

    open_set = [g.start.value] #stack
    closed_set = []
    father = [-1]*g.get_len()

    for indx in range(0,len(father)):
        father[indx]=open_set.pop(-1)
        while father[indx] in closed_set:
            father[indx]=open_set.pop(-1)

        if g.grid_cells[father[indx]].color not in [orange,purple]:
            g.grid_cells[father[indx]].set_color(yellow)
            g.draw(sc)

        if g.is_goal(g.grid_cells[father[indx]]):
            for i in range(indx):
                pygame.draw.line(sc,green,(g.grid_cells[father[i]].x,g.grid_cells[father[i]].y),(g.grid_cells[father[i+1]].x,g.grid_cells[father[i+1]].y))
                if g.grid_cells[father[i]].color not in [orange,purple]:
                    g.grid_cells[father[i]].set_color(grey)
                g.draw(sc)
            wait()

        for neighbor in g.get_neighbors(g.grid_cells[father[indx]]):
            if neighbor.value not in closed_set:
                open_set.append(neighbor.value) #Thứ tự ưu tiên tăng dần từ up, down, left, right, up_left, up_right, down_left, down_right
                if neighbor.color==green:
                    neighbor.set_color(red)
                    g.draw(sc)

        closed_set.append(father[indx])

        if g.grid_cells[father[indx]].color not in [orange,purple]:
            g.grid_cells[father[indx]].set_color(blue)
            g.draw(sc)

    raise NotImplementedError('Not implemented')

def BFS(g:Graph, sc:pygame.Surface):
    print('Implement BFS algorithm')

    open_set = [g.start.value] #queue
    closed_set = []
    father = [-1]*g.get_len()

    for indx in range(0,len(father)):
        father[indx]=open_set.pop(0)

        if g.grid_cells[father[indx]].color not in [orange,purple]:
            g.grid_cells[father[indx]].set_color(yellow)
            g.draw(sc)

        if g.is_goal(g.grid_cells[father[indx]]):
            for i in range(indx):
                pygame.draw.line(sc,green,(g.grid_cells[father[i]].x,g.grid_cells[father[i]].y),(g.grid_cells[father[i+1]].x,g.grid_cells[father[i+1]].y))
                if g.grid_cells[father[i]].color not in [orange,purple]:
                    g.grid_cells[father[i]].set_color(grey)
                g.draw(sc)
            wait()

        for neighbor in g.get_neighbors(g.grid_cells[father[indx]]):
            if neighbor.value not in closed_set:
                if neighbor.color==green:
                    open_set.append(neighbor.value) #Thứ tự thêm là: up, down, left, right, up_left, up_right, down_left, down_right
                    neighbor.set_color(red)
                    g.draw(sc)
                if neighbor.color==purple:
                    open_set.append(neighbor.value)

        closed_set.append(father[indx])

        if g.grid_cells[father[indx]].color not in [orange,purple]:
            g.grid_cells[father[indx]].set_color(blue)
            g.draw(sc)

    raise NotImplementedError('Not implemented')

def UCS(g:Graph, sc:pygame.Surface):
    print('Implement UCS algorithm')

    open_set = {}
    open_set[g.start.value] = 0
    closed_set:list[int] = []
    father = [-1]*g.get_len()
    cost = [100_000]*g.get_len()
    cost[g.start.value] = 0

    #TODO: Implement UCS algorithm using open_set, closed_set, and father
    raise NotImplementedError('Not implemented')
