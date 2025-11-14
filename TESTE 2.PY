import pygame
import sys
import random
sys.init()
# Inicializando o Pygame
pygame.init()

# Definindo as dimensões da tela
LARGURA = 500
ALTURA = 500
screen = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Ping Pong')

# Variáveis de tela cheia
tela_cheia = False

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
AMARELO = (255, 255, 0)
AZUL = (0, 0, 255)
VERMELHO = (255, 0, 0)

# Variáveis de raquete
raquete_largura = 20
raquete_altura = 100
raquete1_x, raquete1_y = 50, 225
raquete2_x, raquete2_y = 430, 225
velocidade_raquete = 5

# Variáveis de bola
bola_x, bola_y = 250, 250
bola_largura, bola_altura = 20, 20
velocidade_bola_x, velocidade_bola_y = 3, 3

# Variáveis de placar
placar1 = 0
placar2 = 0
pontuacao_vitoria = 10  # Pontuação para vitória
fonte = pygame.font.SysFont(None, 55)

# Função para desenhar os elementos na tela
def desenhar():
    # Limpar a tela
    screen.fill(PRETO)

    # Desenhando as raquetes
    pygame.draw.rect(screen, BRANCO, (raquete1_x, raquete1_y, raquete_largura, raquete_altura))
    pygame.draw.rect(screen, BRANCO, (raquete2_x, raquete2_y, raquete_largura, raquete_altura))

    # Desenhando a bola
    pygame.draw.ellipse(screen, BRANCO, (bola_x, bola_y, bola_largura, bola_altura))

    # Desenhando a linha central
    pygame.draw.aaline(screen, BRANCO, (LARGURA // 2, 0), (LARGURA // 2, ALTURA))

    # Exibindo o placar
    placar = fonte.render(f"{placar1}  -  {placar2}", True, BRANCO)
    screen.blit(placar, (LARGURA // 2 - placar.get_width() // 2, 20))

# Função de animação de vitória
def animacao_vitoria(vencedor):
    cores = [AMARELO, AZUL, VERMELHO]
    clock = pygame.time.Clock()

    for _ in range(20):  # 20 quadros para a animação
        screen.fill(random.choice(cores))  # Mudança de cor de fundo aleatória
        pygame.display.flip()
        pygame.time.delay(100)  # Pausa rápida entre as mudanças de cor

    # Exibir o texto "Vencedor"
    font_vitoria = pygame.font.SysFont(None, 100)
    vencedor_texto = font_vitoria.render(f"{vencedor} Vencedor!", True, BRANCO)
    screen.fill(PRETO)  # Limpa a tela antes de mostrar o texto
    screen.blit(vencedor_texto, (LARGURA // 2 - vencedor_texto.get_width() // 2, ALTURA // 2 - vencedor_texto.get_height() // 2))
    pygame.display.flip()
    pygame.time.delay(2000)  # Espera 2 segundos para exibir o texto

# Loop principal do jogo
run = True
while run:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            run = False

        # Alternar para tela cheia ou janela normal com F11
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_F11:
                tela_cheia = not tela_cheia
                if tela_cheia:
                    # Alterna para tela cheia
                    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                else:
                    # Volta para o tamanho original da tela
                    screen = pygame.display.set_mode((LARGURA, ALTURA))

    # Movimentação das raquetes
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and raquete1_y > 0:
        raquete1_y -= velocidade_raquete
    if keys[pygame.K_s] and raquete1_y < ALTURA - raquete_altura:
        raquete1_y += velocidade_raquete
    if keys[pygame.K_UP] and raquete2_y > 0:
        raquete2_y -= velocidade_raquete
    if keys[pygame.K_DOWN] and raquete2_y < ALTURA - raquete_altura:
        raquete2_y += velocidade_raquete

    # Movimentação da bola
    bola_x += velocidade_bola_x
    bola_y += velocidade_bola_y

    # Colisão com o topo e fundo da tela
    if bola_y <= 0 or bola_y >= ALTURA - bola_altura:
        velocidade_bola_y = -velocidade_bola_y

    # Colisão com as raquetes
    if (raquete1_x < bola_x < raquete1_x + raquete_largura) and (raquete1_y < bola_y < raquete1_y + raquete_altura):
        velocidade_bola_x = -velocidade_bola_x
    if (raquete2_x < bola_x < raquete2_x + raquete_largura) and (raquete2_y < bola_y < raquete2_y + raquete_altura):
        velocidade_bola_x = -velocidade_bola_x

    # Se a bola sair pela esquerda ou pela direita
    if bola_x <= 0:  # Pontuação do jogador 2
        placar2 += 1
        bola_x, bola_y = 250, 250  # Reinicia a bola no centro
        velocidade_bola_x = -velocidade_bola_x  # Inverte a direção da bola
    if bola_x >= LARGURA - bola_largura:  # Pontuação do jogador 1
        placar1 += 1
        bola_x, bola_y = 250, 250  # Reinicia a bola no centro
        velocidade_bola_x = -velocidade_bola_x  # Inverte a direção da bola

    # Verifica se algum jogador venceu
    if placar1 >= pontuacao_vitoria:
        animacao_vitoria("Jogador 1")
        placar1, placar2 = 0, 0  # Reinicia o placar após a vitória
    elif placar2 >= pontuacao_vitoria:
        animacao_vitoria("Jogador 2")
        placar1, placar2 = 0, 0  # Reinicia o placar após a vitória

    # Desenho de todos os elementos
    desenhar()

    # Atualiza a tela
    pygame.display.flip()

    # Controla a taxa de atualização do jogo (FPS)
    pygame.time.Clock().tick(60)

# Finaliza o Pygame
pygame.quit()
