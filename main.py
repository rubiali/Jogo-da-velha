##### Criador: Gabriel Rubiali Gomes #####

from colorama import init, Fore
import os
from time import sleep
import random

#Funções:
def clr():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def empty_struture():
    global line1, line2, line3
    line1 = "  a  |  b  |  c  "
    print(line1)
    print("-"*17)
    line2 = "  d  |  e  |  f  "
    print(line2)
    print("-"*17)
    line3 = "  g  |  h  |  i  "
    print(line3)
    
def time_player(moves_player, moves_bot):
    while True:
        move_player = str(input(f"\n{red}(i){reset} Faça sua jogada: "))
        print("")
        if move_player.lower() in "abcdefghi" and not move_player.lower() in moves_player and not move_player.lower() in moves_bot:
            moves_player.append(move_player.lower())
            return move_player.lower()
            break
        else:
            if move_player.lower() in moves_player:
                print(f"{yellow}(!) {reset}Você já fez esse lance...")
            elif move_player.lower() in moves_bot:
                print(f"{yellow}(!) {reset}PC já fez esse lance...")
            else:
                print(f"{yellow}(!){reset} Por favor selecione uma jogada valida!")

def time_bot(moves_bot, moves_player, difficulty, mode_bot):
    if difficulty == 1:
        return move_random_bot(moves_bot, moves_player, difficulty)

    elif difficulty == 2:
        move_bot = strategy_medium_move(moves_bot, moves_player)

        if move_bot == '': #Caso não tenha nenhum dos dois:
            return move_random_bot(moves_bot, moves_player, difficulty)
        else:
            moves_bot.append(move_bot)
            return move_bot

    elif difficulty == 3: #Defesa
        move_bot = strategy_medium_move(moves_bot, moves_player)
        if move_bot == '':
            if 'O' in mode_bot: 
                if not 'e' in moves_bot and not 'e' in moves_player:
                    move_bot = 'e'

                else: #Estratégia sem o meio
                    corners = ['a', 'g', 'c', 'i']
                    corner_actived = False
                    for move in moves_bot:
                        if move in corners:
                            corner_actived = True

                    if not corner_actived:       
                        move_bot = random.choice(corners)

                if 'e' in moves_bot: #Estratégia do meio
                    if not 'd' in (moves_bot + moves_player): #Quina a
                        if 'a' in moves_player and 'h' in moves_player:
                            move_bot = 'd'

                    if not 'b' in (moves_bot + moves_player):
                        if 'a' in moves_player and 'f' in moves_player:
                            move_bot = 'b'

                    if not 'f' in (moves_bot + moves_player): #Quina c
                        if 'c' in moves_player and 'h' in moves_player:
                            move_bot = 'f'

                    if not 'b' in (moves_bot + moves_player):
                        if 'c' in moves_player and 'b' in moves_player:
                            move_bot = 'b'

                    if not 'h' in (moves_bot + moves_player): #Quina g
                        if 'g' in moves_player and 'f' in moves_player:
                            move_bot = 'h'

                    if not 'd' in (moves_bot + moves_player):
                        if 'g' in moves_player and 'b' in moves_player:
                            move_bot = 'd'

                    if not 'h' in (moves_bot + moves_player): #Quina i
                        if 'i' in moves_player and 'd' in moves_player:
                            move_bot = 'h'

                    if not 'f' in (moves_bot + moves_player):
                        if 'i' in moves_player and 'b' in moves_player:
                            move_bot = 'f'

                    #Diagonal1
                    if not 'b' in (moves_bot + moves_player):
                        if 'a' in moves_player and 'i' in moves_player:
                            move_bot = 'b'

                    #Diagonal2
                    if not 'h' in (moves_bot + moves_player):
                        if 'c' in moves_player and 'g' in moves_player:
                            move_bot = 'h'
                        

            elif 'X' in mode_bot: #Ataque
                possible_start = ['a', 'c', 'g', 'i', 'e']
                start_actived = False
                for move in moves_bot:
                    if move in possible_start:
                        start_actived = True
                
                if start_actived:
                    if 'e' in moves_bot: #Estratégia do meio
                        game_draw = False

                        for move in moves_player:
                            if move in possible_start:
                                game_draw = True
                        if game_draw:
                            move_bot = ''

                        else: #Game win
                            if not 'h' in move_bot and not 'h' in move_player:
                                if 'b' in move_player:
                                    move_bot = 'h'

                            if not 'a' in move_bot and not 'a' in move_player:    
                                if 'f' in move_player:
                                    move_bot = 'a'

                            if not 'c' in move_bot and not 'c' in move_player:
                                if 'h' in move_player:
                                    move_bot = 'c'

                            if not 'i' in move_bot and not 'i' in move_player:
                                if 'd' in move_player:
                                    move_bot = 'i'

                    else: #Estratégia dos cantos
                        corners = ['a', 'c', 'g', 'i']
                        game_win = False
                        for move in moves_player:
                            if move in corners:
                                game_win = True
                        if game_win:
                            while True:
                                random_corner = random.choice(corners)
                                if not random_corner in (moves_player + moves_bot):
                                    move_bot = random_corner
                                    break
                        else:
                            move_bot = ''
                else:
                    move_bot = random.choice(possible_start)

        if move_bot == '':
            return move_random_bot(moves_bot, moves_player, difficulty)
        else:
            moves_bot.append(move_bot)
            return move_bot


def strategy_medium_move(moves_bot, moves_player):
    #Estratégia ataque
    move_bot = ''
    #Primeira linha
    if not "c" in moves_player:
        if "a" in moves_bot and "b" in moves_bot:
            move_bot = 'c'

    if not "a" in moves_player:
        if "b" in moves_bot and "c" in moves_bot:
            move_bot = 'a'

    if not "b" in moves_player:
        if "a" in moves_bot and "c" in moves_bot:
            move_bot = 'b'

    #Segunda linha
    if not "f" in moves_player:
        if "d" in moves_bot and "e" in moves_bot:
            move_bot = 'f'

    if not "d" in moves_player:
        if "e" in moves_bot and "f" in moves_bot:
            move_bot = 'd'

    if not "e" in moves_player:
        if "d" in moves_bot and "f" in moves_bot:
            move_bot = 'e'

    #Terceira linha:
    if not "i" in moves_player:
        if "g" in moves_bot and "h" in moves_bot:
            move_bot = 'i'

    if not "g" in moves_player:
        if "h" in moves_bot and "i" in moves_bot:
            move_bot = 'g'

    if not "h" in moves_player:
        if "g" in moves_bot and "i" in moves_bot:
            move_bot = 'h'

    #Primeira coluna:
    if not "g" in moves_player:
        if "a" in moves_bot and "d" in moves_bot:
            move_bot = 'g'
    
    if not "a" in moves_player:
        if "g" in moves_bot and "d" in moves_bot:
            move_bot = 'a'

    if not "d" in moves_player:
        if "a" in moves_bot and "g" in moves_bot:
            move_bot = 'd'

    #Segunda coluna:
    if not "h" in moves_player:
        if "b" in moves_bot and "e" in moves_bot:
            move_bot = 'h'
    
    if not "b" in moves_player:
        if "h" in moves_bot and "e" in moves_bot:
            move_bot = 'b'

    if not "e" in moves_player:
        if "b" in moves_bot and "h" in moves_bot:
            move_bot = 'e'

    #Terceira coluna:
    if not "i" in moves_player:
        if "c" in moves_bot and "f" in moves_bot:
            move_bot = 'i'
    
    if not "c" in moves_player:
        if "i" in moves_bot and "f" in moves_bot:
            move_bot = 'c'

    if not "f" in moves_player:
        if "c" in moves_bot and "i" in moves_bot:
            move_bot = 'f'

    #Primeira diagonal:
    if not "c" in moves_player:
        if "g" in moves_bot and "e" in moves_bot:
            move_bot = 'c'
    
    if not "g" in moves_player:
        if "e" in moves_bot and "c" in moves_bot:
            move_bot = 'g'

    if not "e" in moves_player:
        if "g" in moves_bot and "c" in moves_bot:
            move_bot = 'e'

    #Segunda diagonal:
    if not "i" in moves_player:
        if "a" in moves_bot and "e" in moves_bot:
            move_bot = 'i'
    
    if not "a" in moves_player:
        if "e" in moves_bot and "i" in moves_bot:
            move_bot = 'a'

    if not "e" in moves_player:
        if "a" in moves_bot and "i" in moves_bot:
            move_bot = 'e'

    if move_bot == '': #Estratégia defesa
        #Primeira linha
        if not "c" in moves_bot:
            if "a" in moves_player and "b" in moves_player:
                move_bot = 'c'
        if not "a" in moves_bot:
            if "b" in moves_player and "c" in moves_player:
                move_bot = 'a'
        if not "b" in moves_bot:
            if "a" in moves_player and "c" in moves_player:
                move_bot = 'b'

        #Segunda linha
        if not "f" in moves_bot:
            if "d" in moves_player and "e" in moves_player:
                move_bot = 'f'
        if not "d" in moves_bot:
            if "e" in moves_player and "f" in moves_player:
                move_bot = 'd'
        if not "e" in moves_bot:
            if "d" in moves_player and "f" in moves_player:
                move_bot = 'e'

        #Terceira linha:
        if not "i" in moves_bot:
            if "g" in moves_player and "h" in moves_player:
                move_bot = 'i'
        if not "g" in moves_bot:
            if "h" in moves_player and "i" in moves_player:
                move_bot = 'g'
        if not "h" in moves_bot:
            if "g" in moves_player and "i" in moves_player:
                move_bot = 'h'

        #Primeira coluna:
        if not "g" in moves_bot:
            if "a" in moves_player and "d" in moves_player:
                move_bot = 'g'
        
        if not "a" in moves_bot:
            if "g" in moves_player and "d" in moves_player:
                move_bot = 'a'

        if not "d" in moves_bot:
            if "a" in moves_player and "g" in moves_player:
                move_bot = 'd'

        #Segunda coluna:
        if not "h" in moves_bot:
            if "b" in moves_player and "e" in moves_player:
                move_bot = 'h'
        
        if not "b" in moves_bot:
            if "h" in moves_player and "e" in moves_player:
                move_bot = 'b'

        if not "e" in moves_bot:
            if "b" in moves_player and "h" in moves_player:
                move_bot = 'e'

        #Terceira coluna:
        if not "i" in moves_bot:
            if "c" in moves_player and "f" in moves_player:
                move_bot = 'i'
        
        if not "c" in moves_bot:
            if "i" in moves_player and "f" in moves_player:
                move_bot = 'c'

        if not "f" in moves_bot:
            if "c" in moves_player and "i" in moves_player:
                move_bot = 'f'

        #Primeira diagonal:
        if not "c" in moves_bot:
            if "g" in moves_player and "e" in moves_player:
                move_bot = 'c'
        
        if not "g" in moves_bot:
            if "e" in moves_player and "c" in moves_player:
                move_bot = 'g'

        if not "e" in moves_bot:
            if "g" in moves_player and "c" in moves_player:
                move_bot = 'e'

        #Segunda diagonal:
        if not "i" in moves_bot:
            if "a" in moves_player and "e" in moves_player:
                move_bot = 'i'
        
        if not "a" in moves_bot:
            if "e" in moves_player and "i" in moves_player:
                move_bot = 'a'

        if not "e" in moves_bot:
            if "a" in moves_player and "i" in moves_player:
                move_bot = 'e'

    return move_bot

def move_random_bot(moves_bot, moves_player, difficulty):
    while True:
        move_bot = random.randint(0,8)
        order_plays = "abcdefghi"
        
        for c in range(0, 9):
            if move_bot == c:
                move_bot = str(order_plays[c])

                if not move_bot in moves_bot and not move_bot in moves_player:
                    moves_bot.append(move_bot)
                    return move_bot
                    break

def content_struture(moves_bot, moves_player, mode_bot, mode_player, turn):
    global line1, line2, line3

    #Atualizar tabuleiro
    for move in moves_player:
        if move in line1:
            line1 = line1.replace(move, mode_player)
        elif move in line2:
            line2 = line2.replace(move, mode_player)
        elif move in line3:
            line3 = line3.replace(move, mode_player)
    
    for move in moves_bot:
        if move in line1:
            line1 = line1.replace(move, mode_bot)
        elif move in line2:
            line2 = line2.replace(move, mode_bot)
        elif move in line3:
            line3 = line3.replace(move, mode_bot)

    #Mostrar tabuleiro
    print(line1)
    print("-" * 17)
    print(line2)
    print("-" * 17)
    print(line3)
    
def result_player(moves_player, moves_bot):
    s_player = ('').join(sorted(moves_player))
    s_bot = ('').join(sorted(moves_bot))

    #Vitorias
    if "abc" in s_player: #Linha1
        result = 'win' 
    elif "def" in s_player: #Linha2
        result = 'win'
    elif "ghi" in s_player: #Linha3
        result = 'win'
    elif "a" in moves_player and "e" in moves_player and "i" in moves_player: #Diagonal1
        result = 'win'
    elif "c" in moves_player and "e" in moves_player and "g" in moves_player: #Diagonal2
        result = 'win'
    elif "a" in moves_player and "d" in moves_player and "g" in moves_player: #Coluna1
        result = 'win'
    elif "b" in moves_player and "e" in moves_player and "h" in moves_player: #Coluna2
        result = 'win'
    elif "c" in moves_player and "f" in moves_player and "i" in moves_player: #Coluna3
        result = 'win'
    else:
        #Derrotas
        if "abc" in s_bot:
            result = 'loss'
        elif "def" in s_bot:
            result = 'loss'
        elif "ghi" in s_bot:
            result = 'loss'
        elif "a" in moves_bot and "e" in moves_bot and "i" in moves_bot:
            result = 'loss'
        elif "c" in moves_bot and "e" in moves_bot and "g" in moves_bot:
            result = 'loss'
        elif "a" in moves_bot and "d" in moves_bot and "g" in moves_bot:
            result = 'loss'
        elif "b" in moves_bot and "e" in moves_bot and "h" in moves_bot:
            result = 'loss'
        elif "c" in moves_bot and "f" in moves_bot and "i" in moves_bot:
            result = 'loss'
        else:
            result = ''
    return result
    
def final_score(c_win, c_loss):
    print("=-" * 5 + f"{light_blue}PLACAR FINAL{reset}" + "=-" * 5)
    print(f"   Jogador: {green}{c_win}{reset} | Computador: {red}{c_loss}{reset}")
    print("=-" * 16)

#Cores:
red = Fore.RED
blue = Fore.BLUE
light_blue = Fore.LIGHTBLUE_EX
light_green = Fore.LIGHTGREEN_EX
light_red = Fore.LIGHTRED_EX
green = Fore.GREEN
yellow = Fore.YELLOW
reset = Fore.RESET

#Inicio
init()
clr()
while True:
    print(f"{blue}(~){reset} Vamos jogar jogo da velha?\n")
    difficulty = int(input(f"{green}(~){reset} Selecione a dificuldade: \n\n(1) - {light_green}Fácil{reset}\n(2) - {blue}Médio{reset}\n(3) - {red}Difícil{reset}\n\n{blue}(i){reset} Sua escolha: "))
    if difficulty > 0 and difficulty <= 3:
        sleep(0.5)
        break
    else:
        print(f"\n{red}[ERRO]{reset} Por favor, selecione uma opção válida...")
        sleep(2)
        clr()

#Globais
line1 = line2 = line3 = ""
c_loss = c_win = 0
clr()
print(f"{light_blue}(#){reset} Jogo da velha {light_blue}(#){reset} - Placar: {c_win}x{c_loss}\n")
empty_struture()
moves_player = []
moves_bot = []
mode = random.randint(0, 1)

if mode == 0: # Jogador ser X ou O aleatoriamente
    mode_player = f'{red}X{reset}'
    mode_bot = f'{blue}O{reset}'
    turn = True
else:
    mode_player = f'{red}O{reset}'
    mode_bot = f'{blue}X{reset}'
    turn = False
    
#Programa
if __name__ == '__main__':
    while True:
        while True:
            if turn:  
                #Meu turno  
                move_player = time_player(moves_player, moves_bot)
                turn = False
            else:
                #Turno do bot
                print(f"\n{blue}(~){reset} Vez do computador...")
                move_bot = time_bot(moves_bot, moves_player, difficulty, mode_bot)
                turn = True
                sleep(1)

            clr()
            print(f"{light_blue}(#){reset} Jogo da velha {light_blue}(#){reset} - Placar: {c_win}x{c_loss}\n")
            content_struture(moves_bot, moves_player, mode_bot, mode_player, turn)

            if len(moves_player) >= 3 or len(moves_bot) >= 3:
                result = result_player(moves_player, moves_bot)
                if result == 'win':
                    print(f"\n{green}(+){reset} Parabéns você venceu!!!")
                    c_win += 1
                    break
                elif result == 'loss':
                    print(f"\n{red}(-){reset} Infelizmente você perdeu...")
                    c_loss += 1
                    break
            if len(moves_player) + len(moves_bot) == 9:
                print(f"\n{yellow}(!) {reset}Partida empatada!")
                break

        sleep(0.5)
        restart = str(input(f"\n{light_blue}(i){reset} Deseja jogar mais?[s/n]: "))

        if restart == 's':
            line1 = line2 = line3 = ""
            moves_player = []
            moves_bot = []
            mode = random.randint(0, 1)

            if mode == 0:
                mode_player = f'{red}X{reset}'
                mode_bot = f'{blue}O{reset}'
                turn = True
            else:
                mode_player = f'{red}O{reset}'
                mode_bot = f'{blue}X{reset}'
                turn = False

            clr()
            print(f"{light_blue}(#){reset} Jogo da velha {light_blue}(#){reset} - Placar: {c_win}x{c_loss}\n")
            empty_struture()

        else:
            clr()
            final_score(c_win, c_loss)
            break