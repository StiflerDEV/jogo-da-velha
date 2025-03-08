import pygame
import random

# Inicializa o pygame
pygame.init()

# Definições básicas
largura, altura = 500, 500
tamanho_quadrado = 20
preto = (0, 0, 0)
verde = (0, 255, 0)
vermelho = (255, 0, 0)

# Criando a tela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo da Cobrinha")

# Função principal do jogo
def jogo():
    cobra = [(100, 100)]
    direcao = (tamanho_quadrado, 0)
    comida = (random.randrange(0, largura, tamanho_quadrado), random.randrange(0, altura, tamanho_quadrado))
    rodando = True
    clock = pygame.time.Clock()

    while rodando:
        tela.fill(preto)

        # Verifica eventos do teclado
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    direcao = (0, -tamanho_quadrado)
                elif event.key == pygame.K_DOWN:
                    direcao = (0, tamanho_quadrado)
                elif event.key == pygame.K_LEFT:
                    direcao = (-tamanho_quadrado, 0)
                elif event.key == pygame.K_RIGHT:
                    direcao = (tamanho_quadrado, 0)

        # Move a cobra
        nova_cabeca = (cobra[0][0] + direcao[0], cobra[0][1] + direcao[1])
        cobra.insert(0, nova_cabeca)

        # Se a cobra comer a comida
        if nova_cabeca == comida:
            comida = (random.randrange(0, largura, tamanho_quadrado), random.randrange(0, altura, tamanho_quadrado))
        else:
            cobra.pop()

        # Fim de jogo se bater na parede ou nela mesma
        if nova_cabeca in cobra[1:] or nova_cabeca[0] < 0 or nova_cabeca[1] < 0 or nova_cabeca[0] >= largura or nova_cabeca[1] >= altura:
            rodando = False

        # Desenha a cobra
        for parte in cobra:
            pygame.draw.rect(tela, verde, (*parte, tamanho_quadrado, tamanho_quadrado))

        # Desenha a comida
        pygame.draw.rect(tela, vermelho, (*comida, tamanho_quadrado, tamanho_quadrado))

        pygame.display.flip()
        clock.tick(10)

    pygame.quit()

jogo()
