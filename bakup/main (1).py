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
            else:
                print(f"{yellow}(!){reset} Por favor selecione uma jogada valida!")

def time_bot(moves_bot, moves_player):
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
    if "abc" in s_player:
        result = 'win'
    elif "def" in s_player:
        result = 'win'
    elif "ghi" in s_player:
        result = 'win'
    elif "a" in moves_player and "e" in moves_player and "i" in moves_player:
        result = 'win'
    elif "c" in moves_player and "e" in moves_player and "g" in moves_player:
        result = 'win'
    elif "a" in moves_player and "d" in moves_player and "g" in moves_player:
        result = 'win'
    elif "b" in moves_player and "e" in moves_player and "h" in moves_player:
        result = 'win'
    elif "c" in moves_player and "f" in moves_player and "i" in moves_player:
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
green = Fore.GREEN
yellow = Fore.YELLOW
reset = Fore.RESET

#Inicio
init()
clr()
print(f"{blue}(~){reset} Vamos jogar jogo da velha...\n")

#Globais
line1 = line2 = line3 = ""
empty_struture()
moves_player = []
moves_bot = []
mode = random.randint(0, 1)
c_loss = c_win = 0

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
                move_bot = time_bot(moves_bot, moves_player)
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