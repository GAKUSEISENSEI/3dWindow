
import pygame
run = True
pygame.init()
dx = 0
dy = 0
win = pygame.display.set_mode((1250, 675))
x = 625
y = 338
d1 = [550, 300]
d2 = [550, 410]
d3 = [660, 300]
d4 = [660, 410]
f = False
while run:
    
    dx += 0.2
    if dy < 22:
        dy += 0.1
        dy1 = dy
    dx1 = dx
        
    if 604.9 < d1[0] + dx < 605.1:
        f = True
    while f:
        
        dx1+=0.2
        
        dx -= 0.2
        
        dy -= 0.1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        win.fill((92, 177, 230))
        pygame.draw.line(win, (0, 0, 0), (d1[0] + dx1, d1[1]), (d2[0] + dx1, d2[1]), 20)
        pygame.draw.line(win, (0, 0, 0), (d1[0] + dx1, d1[1]), (d3[0] - dx1, d3[1] + dy), 20)
        pygame.draw.line(win, (0, 0, 0), (d2[0] + dx1, d2[1]), (d4[0] - dx1, d4[1] - dy), 20)
        pygame.draw.line(win, (0, 0, 0), (d3[0] - dx1, d3[1] + dy), (d4[0] - dx1, d4[1] - dy), 20)
        pygame.display.update()
        if -0.001<dy<0.001:
            f = False
        

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    win.fill((92, 177, 230))
    pygame.draw.line(win, (0, 0, 0), (d1[0] + dx, d1[1]), (d2[0] + dx, d2[1]), 20)
    pygame.draw.line(win, (0, 0, 0), (d1[0] + dx, d1[1]), (d3[0] - dx, d3[1] + dy), 20)
    pygame.draw.line(win, (0, 0, 0), (d2[0] + dx, d2[1]), (d4[0] - dx, d4[1] - dy), 20)
    pygame.draw.line(win, (0, 0, 0), (d3[0] - dx, d3[1] + dy), (d4[0] - dx, d4[1] - dy), 20)
    pygame.display.update()
