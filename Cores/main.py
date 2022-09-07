# Manuela Bertanha | TIA 32152851

import pygame
import random

SCREEN_SIZE = (700, 500)

RED = (255, 51, 51)
BEIGE = (255, 255, 230)
BLACK = (20, 20, 20)
GREY = (153, 153, 153)
GREEN = (0, 208, 161)
PURPLE = (153, 51, 255)
PINK = (255, 102, 153)
ORANGE = (255, 133, 51)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('JOGO DAS CORES')
pygame.time.delay(500)

fonte1 = pygame.font.SysFont('rockwellcondensed', 40, bold=False, italic=True)  # Guarda a fonte escolhida em uma variável
fonte2 = pygame.font.SysFont('arial', 40, bold=True, italic=True)
fonte3 = pygame.font.SysFont('rockwellcondensed', 26, bold=False, italic=False)
fonte4 = pygame.font.SysFont('arial', 16, bold=True, italic=False)

img_nivel_02 = pygame.image.load('shuffle.png')
img_nivel_02_click = pygame.image.load('shuffle-click.png')


def start():
    start = True
    texto1 = fonte1.render('Pressione uma tecla para iniciar', True, RED)  # Aplica a fonte a um determinado texto e com uma dada cor
    screen.blit(texto1, (135, 210))
    pygame.display.update()
    while start:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                start = False
            if evento.type == pygame.KEYDOWN:
                start = False
                nivel_01()


def nivel_01():
    screen.fill((0, 0, 0))
    texto2 = fonte2.render('NÍVEL 01', True, RED)
    screen.blit(texto2, (260, 210))
    pygame.display.update()
    pygame.time.delay(1100)
    screen.fill(BEIGE)
    pygame.display.update()
    level_1 = True
    texto3 = fonte3.render('Escolha a cor para pintar:', True, BLACK)
    screen.blit(texto3, (50, 25))
    texto4 = fonte4.render('próximo >>', True, BLACK)
    screen.blit(texto4, (555, 450))
    while level_1:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                level_1 = False
            pygame.draw.rect(screen, GREEN, (50, 90, 45, 45))
            pygame.draw.rect(screen, PURPLE, (50, 145, 45, 45))
            pygame.draw.rect(screen, PINK, (50, 200, 45, 45))
            pygame.draw.rect(screen, ORANGE, (50, 255, 45, 45))
            desenha_forma()
            pygame.display.update()
            if evento.type == pygame.MOUSEBUTTONDOWN and 50 <= evento.pos[0] <= 95 and 90 <= evento.pos[1] <= 135:
                preenche_forma(GREEN)
            if evento.type == pygame.MOUSEBUTTONDOWN and 50 <= evento.pos[0] <= 95 and 145 <= evento.pos[1] <= 190:
                preenche_forma(PURPLE)
            if evento.type == pygame.MOUSEBUTTONDOWN and 50 <= evento.pos[0] <= 95 and 200 <= evento.pos[1] <= 245:
                preenche_forma(PINK)
            if evento.type == pygame.MOUSEBUTTONDOWN and 50 <= evento.pos[0] <= 95 and 255 <= evento.pos[1] <= 300:
                preenche_forma(ORANGE)
            if evento.type == pygame.MOUSEBUTTONDOWN and 555 <= evento.pos[0] <= 639 and 450 <= evento.pos[1] <= 468:
                texto_click = fonte4.render('próximo >>', True, BEIGE)
                screen.blit(texto_click, (555, 450))
                pygame.display.update()
                pygame.time.delay(150)
                screen.blit(texto4, (555, 450))
                pygame.display.update()
                pygame.time.delay(150)
                level_1 = False
                nivel_02()


def desenha_forma():
    pygame.draw.circle(screen, GREY, (400, 200), 90, 2)
    pygame.draw.circle(screen, GREY, (200, 190), 30, 2)
    pygame.draw.circle(screen, GREY, (560, 320), 70, 2)
    pygame.draw.circle(screen, GREY, (580, 120), 45, 2)
    pygame.draw.rect(screen, GREY, (190, 270, 80, 80), 2)
    pygame.draw.rect(screen, GREY, (330, 340, 110, 40), 2)


def preenche_forma(cor):
    for x in range(5, 90):
        pygame.draw.circle(screen, cor, (400, 200), x)
        pygame.time.delay(6)
        pygame.display.update()
    for x in range(5, 30):
        pygame.draw.circle(screen, cor, (200, 190), x)
        pygame.time.delay(6)
        pygame.display.update()
    for x in range(5, 70):
        pygame.draw.circle(screen, cor, (560, 320), x)
        pygame.time.delay(6)
        pygame.display.update()
    for x in range(5, 45):
        pygame.draw.circle(screen, cor, (580, 120), x)
        pygame.time.delay(6)
        pygame.display.update()
    for x in range(5, 80):
        pygame.draw.rect(screen, cor, (190, 270, x, x))
        pygame.time.delay(6)
        pygame.display.update()
    for x in range(5, 40):
        pygame.draw.rect(screen, cor, (330, 340, x + 70, x))
        pygame.time.delay(6)
        pygame.display.update()


def nivel_02():
    screen.fill((0, 0, 0))
    texto2 = fonte2.render('NÍVEL 02', True, RED)
    screen.blit(texto2, (260, 210))
    pygame.display.update()
    pygame.time.delay(1100)
    screen.fill(BEIGE)
    pygame.display.update()
    level_2 = True
    texto3 = fonte3.render('Pinte com cores aleatórias:', True, BLACK)
    screen.blit(texto3, (50, 25))
    texto4 = fonte4.render('<< anterior', True, BLACK)
    screen.blit(texto4, (50, 450))
    while level_2:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                level_2 = False
            screen.blit(img_nivel_02, (50, 90))
            desenha_forma()
            pygame.display.update()
            if evento.type == pygame.MOUSEBUTTONDOWN and 50 <= evento.pos[0] <= 103 and 90 <= evento.pos[1] <= 144:
                screen.blit(img_nivel_02_click, (50, 90))
                pygame.display.update()
                pygame.time.delay(100)
                screen.blit(img_nivel_02, (50, 90))
                pygame.display.update()
                preenche_forma_random()
            if evento.type == pygame.MOUSEBUTTONDOWN and 50 <= evento.pos[0] <= 130 and 450 <= evento.pos[1] <= 467:
                texto_click = fonte4.render('<< anterior', True, BEIGE)
                screen.blit(texto_click, (50, 450))
                pygame.display.update()
                pygame.time.delay(150)
                screen.blit(texto4, (50, 450))
                pygame.display.update()
                pygame.time.delay(150)
                level_2 = False
                nivel_01()


def preenche_forma_random():
    a = random.randint(0, 255)
    b = random.randint(0, 255)
    c = random.randint(0, 255)
    for x in range(5, 90):
        pygame.draw.circle(screen, (a, b, c), (400, 200), x)
        pygame.time.delay(6)
        pygame.display.update()
    for x in range(5, 30):
        pygame.draw.circle(screen, (a, c, b), (200, 190), x)
        pygame.time.delay(6)
        pygame.display.update()
    for x in range(5, 70):
        pygame.draw.circle(screen, (c, a, b), (560, 320), x)
        pygame.time.delay(6)
        pygame.display.update()
    for x in range(5, 45):
        pygame.draw.circle(screen, (c, b, a), (580, 120), x)
        pygame.time.delay(6)
        pygame.display.update()
    for x in range(5, 80):
        pygame.draw.rect(screen, (b, a, c), (190, 270, x, 80))  # Preenche o quadrado da esquerda p/ direita
        pygame.time.delay(6)
        pygame.display.update()
    for x in range(5, 40):
        pygame.draw.rect(screen, (b, c, a), (330, 340, 110, x))  # Preenche o retângulo de cima p/ baixo
        pygame.time.delay(6)
        pygame.display.update()


start()
pygame.time.delay(500)
pygame.quit()
