# Manuela Bertanha | TIA 32152851

import pygame

SCREEN_SIZE = (680, 380)

pygame.init()  # Inicializa os módulos da biblioteca
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("PELA ESTRADA")
screen.fill((255, 241, 230))
pygame.display.flip()
pygame.time.delay(500)

imgEstrada = "fundoEstrada.png"  # Guarda o nome do arquivo na variável 'imgEstrada'
imgCarro1 = "ferrari_1.png"
imgCarro2 = "ferrari_2.png"

estrada = pygame.image.load(imgEstrada)  # Carrega a imagem para a área de memória
carro = pygame.image.load(imgCarro1)

fonte = pygame.font.SysFont("stencil", 90, bold=False, italic=False)
textoFinal = fonte.render("Game Over", True, (255,255,153), (128,128,255))

jogoAtivo = True
x = 0
y = 80
vel = 10
while jogoAtivo:
    for evento in pygame.event.get():
        if (evento.type == pygame.QUIT):
            jogoAtivo = False
    screen.blit(estrada, (0,0))
    screen.blit(carro, (x, y))
    x += vel
    pygame.time.delay(35)
    if (x == 680 and y == 80):
        x = 640
        y = 190
        carro = pygame.image.load(imgCarro2)
        screen.blit(carro, (x,y))
        vel = -vel
    if (x < -100):
        x = 0
        y = 305
        carro = pygame.image.load(imgCarro1)
        screen.blit(carro, (x,y))
        vel = -vel
    if (x > 680):
        #screen.fill((128,128,255))
        #pygame.display.flip()  # Preenche a tela com o Game Over
        screen.blit(textoFinal, (95,152))
        jogoAtivo = False
    pygame.display.update()

pygame.time.delay(3000)
pygame.quit()