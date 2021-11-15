import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

barulho_colisao = pygame.mixer.Sound('colisão.wav')

largura = 640
altura = 480
x = largura/2
y = altura/2
velocidade = 10

x_vermelho = randint(40, 600)
y_vermelho = randint(50, 430)

pontos = 0
fonte = pygame.font.SysFont('arial', 40, True, True)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Joguinho by Davi Dantas')
clock = pygame.time.Clock()

while True:
    clock.tick(60)
    tela.fill((0,0,0))
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (255,255,255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    
    keys = pygame.key.get_pressed()
    if keys[K_a]:
         x -= velocidade
    if keys[K_d]:
         x += velocidade
    if keys[K_w]:
         y -= velocidade
    if keys[K_s]:
         y += velocidade

    ret_azul = pygame.draw.rect(tela, (0,0,255), (x,y,40,50))
    ret_vermelho = pygame.draw.rect(tela, (255,0,0), (x_vermelho,y_vermelho,40,50))

    if ret_vermelho.colliderect(ret_azul):
         x_vermelho = randint(40, 600)
         y_vermelho = randint(50, 430)
         pontos += 1
         barulho_colisao.play()
    
    tela.blit(texto_formatado, (430,10))
    pygame.display.update()