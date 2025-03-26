
'''
FIAP
1TDSPH - 2o semestre de 2024 
Professor: Fernando Luiz de Almeida

Checkpoint 4 I 
Arquivo: AndreLeticia.py

André Rogério Vieira Pavanela Altobelli Antunes
Leticia Cristina dos Santos Passos

01/09/2024
'''

import random

#Exibe o menu principal e gerencia a interação com o usuário.
def imprime_menu_principal():
    print("╔═══════════════════════════╗")
    print("║      Jogo da Velha        ║")
    print("╠═══════════════════════════╣")
    print("║ 1. Jogador x Jogador      ║")
    print("╠═══════════════════════════╣")
    print("║ 2. Jogador x Máquina      ║")
    print("╠═══════════════════════════╣")
    print("║ 3. Jogador x Inteligência ║")
    print("╠═══════════════════════════╣")
    print("║ 4. Sair                   ║")
    print("╚═══════════════════════════╝")

#Inicializa um tabuleiro 3x3 vazio.
def inicializar_tabuleiro():
    return [[' ' for _ in range(3)] for _ in range(3)]

#Imprime o tabuleiro do jogo.
def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        linha_formatada = ''
        for i in range(len(linha)):
            linha_formatada += linha[i]
            if i < len(linha) - 1:
                linha_formatada += ' | '
        print(linha_formatada)
        print('-' * 9)

# Lê e retorna a coordenada da linha inserida pelo usuário, ajustando para índice 0.
def leia_coordenada_linha(): 
    while True:
        linha = input("Digite a linha (1, 2, 3): ")  
        if linha in "123": 
            return int(linha) - 1 
        else:
            print("Entrada inválida. Digite um número entre 1 e 3.")

# Lê e retorna a coordenada da coluna inserida pelo usuário, ajustando para índice 0.
def leia_coordenada_coluna():
    while True:
        coluna = input("Digite a coluna (1, 2, 3): ")  
        if coluna in "123":  
            return int(coluna) - 1  
        else:
            print("Entrada inválida. Digite um número entre 1 e 3.")

#Imprime a pontuação dos jogadores.
def imprime_pontuacao(jogador1, jogador2, pts1, pts2):
    print(f"Pontuação:\n{jogador1}: {pts1}\n{jogador2}: {pts2}")

#Verifica se a posição no tabuleiro é válida e está vazia.
def posicao_valida(tabuleiro, linha, coluna):
    return tabuleiro[linha][coluna] == ' '

#Verifica se há um vencedor no tabuleiro.
def verifica_vencedor(tabuleiro, simbolo):

    for i in range(3):
        vencedor_linha = True
        for j in range(3):
            if tabuleiro[i][j] != simbolo:
                vencedor_linha = False
                break
        if vencedor_linha:
            return True

    for i in range(3):
        vencedor_coluna = True
        for j in range(3):
            if tabuleiro[j][i] != simbolo:
                vencedor_coluna = False
                break
        if vencedor_coluna:
            return True

    vencedor_diagonal_1 = True
    for i in range(3):
        if tabuleiro[i][i] != simbolo:
            vencedor_diagonal_1 = False
            break
    if vencedor_diagonal_1:
        return True

    vencedor_diagonal_2 = True
    for i in range(3):
        if tabuleiro[i][2 - i] != simbolo:
            vencedor_diagonal_2 = False
            break
    if vencedor_diagonal_2:
        return True

    return False

#Verifica se o jogo deu velha (empate).
def verifica_velha(tabuleiro):
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == ' ':  
                return False  
    return True  

#Modo de jogo Jogador vs Jogador.
def modo_jogador():
    jogador1, jogador2 = 'X', 'O'
    pontos_jogador1 = 0
    pontos_jogador2 = 0
    rodadas = 1

    while pontos_jogador1 < 3 and pontos_jogador2 < 3:
        print(f"Rodada: {rodadas}")
        tabuleiro = inicializar_tabuleiro()
        imprimir_tabuleiro(tabuleiro)
        turno = 0

        while True:
            simbolo = jogador1 if turno % 2 == 0 else jogador2
            print(f"Turno do jogador {simbolo}")

            if jogada_usuario(tabuleiro, simbolo):
                imprimir_tabuleiro(tabuleiro)

                if verifica_vencedor(tabuleiro, simbolo):
                    print(f"Jogador {simbolo} venceu esta rodada!")
                    if simbolo == jogador1:
                        pontos_jogador1 += 1
                    else:
                        pontos_jogador2 += 1
                    break
                elif verifica_velha(tabuleiro):
                    print("O jogo deu velha nesta rodada!")
                    break

                turno += 1  

        imprime_pontuacao("Jogador 1", "Jogador 2", pontos_jogador1, pontos_jogador2)
        rodadas += 1

    if pontos_jogador1 == 3:
        print("Jogador 1, venceu o jogo!")
    else:
        print("Jogador 2, venceu o jogo!")

#Modo de jogo Jogador vs Máquina
def modo_facil():
    jogador, bot = 'X', 'O'
    pontos_jogador = 0
    pontos_bot = 0
    rodadas = 1

    while pontos_jogador < 3 and pontos_bot < 3:
        print(f"Rodada: {rodadas}")
        tabuleiro = inicializar_tabuleiro()
        imprimir_tabuleiro(tabuleiro)
        turno = 0

        while True:
            if turno % 2 == 0:
                print("Turno do jogador")
                linha = leia_coordenada_linha()
                coluna = leia_coordenada_coluna()

                if posicao_valida(tabuleiro, linha, coluna):
                    tabuleiro[linha][coluna] = jogador
                    imprimir_tabuleiro(tabuleiro)

                    if verifica_vencedor(tabuleiro, jogador):
                        print("Você venceu esta rodada!")
                        pontos_jogador += 1
                        break
                    elif verifica_velha(tabuleiro):
                        print("O jogo deu velha nesta rodada!")
                        break
                    else:
                        turno += 1
                else:
                    print("Posição inválida, tente novamente.")
            else:
                print("Turno do Bot")
                jogada_maquina_facil(tabuleiro, bot)
                imprimir_tabuleiro(tabuleiro)

                if verifica_vencedor(tabuleiro, bot):
                    print("O Bot venceu esta rodada!")
                    pontos_bot += 1
                    break
                elif verifica_velha(tabuleiro):
                    print("O jogo deu velha nesta rodada!")
                    break
                else:
                    turno += 1

        imprime_pontuacao(f"Jogador", "Bot", pontos_jogador, pontos_bot)
        rodadas += 1

    if pontos_jogador == 3:
        print("Parabéns! Você venceu o jogo!")
    else:
        print("O Bot venceu o jogo. Tente novamente!")

#Função principal para iniciar o jogo.
def jogar():
    
    while True:
        imprime_menu_principal()
        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            modo_jogador()
        elif escolha == '2':
            modo_facil()
        elif escolha == '3':
            modo_dificil()
        elif escolha == '4':
            print("Fim de Jogo!")
            break
        else:
            print("Opção inválida.")

#Função para obter as coordenadas do jogador e validar a posição.
def jogada_usuario(tabuleiro, simbolo):
    while True:
        linha = leia_coordenada_linha()
        coluna = leia_coordenada_coluna()

        if posicao_valida(tabuleiro, linha, coluna):
            tabuleiro[linha][coluna] = simbolo
            return True
        else:
            print("Posição inválida, tente novamente.")
            return False

#Realiza a jogada da máquina de forma aleatória).
def jogada_maquina_facil(tabuleiro, simbolo):
    while True:
        linha = random.randint(0, 2)
        coluna = random.randint(0, 2)
        if posicao_valida(tabuleiro, linha, coluna):
            tabuleiro[linha][coluna] = simbolo
            break

def jogada_maquina_dificil(tabuleiro, simbolo):

    #a maquina vai verificar quando ganhou
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == ' ':
                tabuleiro[i][j] = simbolo
                if verifica_vencedor(tabuleiro, simbolo):
                    return
                tabuleiro[i][j] = ' '
    
    # Tenta bloquear o jogador
    oponente = 'X' if simbolo == 'O' else 'O'
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == ' ':
                tabuleiro[i][j] = oponente
                if verifica_vencedor(tabuleiro, oponente):
                    tabuleiro[i][j] = simbolo
                    return
                tabuleiro[i][j] = ' '
    
    # Joga no centro se estiver disponível
    if tabuleiro[1][1] == ' ':
        tabuleiro[1][1] = simbolo
        return
    
    # Tenta jogar nos cantos
    cantos = [(0, 0), (0, 2), (2, 0), (2, 2)]
    for canto in cantos:
        if tabuleiro[canto[0]][canto[1]] == ' ':
            tabuleiro[canto[0]][canto[1]] = simbolo
            return
    
    # Tenta jogar nas bordas
    bordas = [(0, 1), (1, 0), (1, 2), (2, 1)]
    for borda in bordas:
        if tabuleiro[borda[0]][borda[1]] == ' ':
            tabuleiro[borda[0]][borda[1]] = simbolo
            return

def modo_dificil():
    jogador, inteligencia = 'X', 'O'
    pontos_jogador = 0
    pontos_inteligencia = 0
    rodadas = 1

    while pontos_jogador < 3 and pontos_inteligencia < 3:
        print(f"Rodada: {rodadas}")
        tabuleiro = inicializar_tabuleiro()
        imprimir_tabuleiro(tabuleiro)
        turno = 0

        while True:
            if turno % 2 == 0:
                print("Turno do jogador")
                linha = leia_coordenada_linha()
                coluna = leia_coordenada_coluna()

                if posicao_valida(tabuleiro, linha, coluna):
                    tabuleiro[linha][coluna] = jogador
                    imprimir_tabuleiro(tabuleiro)

                    if verifica_vencedor(tabuleiro, jogador):
                        print("Você venceu esta rodada!")
                        pontos_jogador += 1
                        break
                    elif verifica_velha(tabuleiro):
                        print("O jogo deu velha nesta rodada!")
                        break
                    else:
                        turno += 1
                else:
                    print("Posição inválida, tente novamente.")
            else:
                print("Turno do Inteligência")
                jogada_maquina_dificil(tabuleiro, inteligencia)
                imprimir_tabuleiro(tabuleiro)

                if verifica_vencedor(tabuleiro, inteligencia):
                    print("A inteligência venceu esta rodada!")
                    pontos_inteligencia += 1
                    break
                elif verifica_velha(tabuleiro):
                    print("O jogo deu velha nesta rodada!")
                    break
                else:
                    turno += 1

        imprime_pontuacao(f"Jogador", "Inteligência", pontos_jogador, pontos_inteligencia)
        rodadas += 1

    if pontos_jogador == 3:
        print("Parabéns! Você venceu o jogo!")
    else:
        print("A Intêligencia venceu o jogo. Tente novamente!")



# principal

jogar()