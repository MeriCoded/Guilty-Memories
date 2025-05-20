import pygame
import random

pygame.init()

WITDH, HEIGHT = 780, 500

SCREEN = pygame.display.set_mode((WITDH, HEIGHT))
pygame.display.set_caption("Skibidi Juego")

active_box = None
boxes = []
targets = []
for i in range(9):
    x = random.randint(0, WITDH - 50)
    y = random.randint(0, HEIGHT - 50)
    box = pygame.Rect(x, y, 100, 100)
    boxes.append(box)
    target_x = (0, WITDH - 50)
    target_y = (0, HEIGHT - 50)
    targets.append((target_x, target_y))

run = True
while run:
    for target in targets:
        pygame.draw.rect(SCREEN, (0, 255, 128), target)
    for box in boxes:
        pygame.draw.rect(SCREEN, (128, 0, 128), box)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for box in boxes:
                    for num, box in enumerate(boxes):
                        if box.collidepoint(event.pos):
                            active_box = num
        if event.type == pygame.MOUSEMOTION:
            if active_box is not None:
                boxes[active_box].center = event.pos
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                active_box = None
                if active_box is not None:
                    target_x, target_y = targets[active_box]
                    if abs(boxes[active_box].centerx - target_x) < 20 and abs(boxes[active_box].centery - target_y) < 20:
                        boxes[active_box].center = (target_x, target_y)
                    else:
                        boxes[active_box].center = (boxes[active_box].x, boxes[active_box].y)
                                            
        if event.type == pygame.QUIT:
            run = False
    SCREEN.fill((0, 0, 30))
    for box in boxes:
        pygame.draw.rect(SCREEN, "purple", box)
    pygame.display.update()
pygame.display.flip()
pygame.quit()