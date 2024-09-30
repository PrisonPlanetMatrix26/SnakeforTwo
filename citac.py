'''
Lesson 20 - Snake
'''
import os
import time
import random
import msvcrt

BOARD_WIDTH = 40
BOARD_HEIGHT = 20
DIFFICULTY = 8

def create_fruit(tail_positions, tail_positions2):
    fruit_position = [random.randint(1, BOARD_WIDTH), random.randint(1, BOARD_HEIGHT)]
    while fruit_position in tail_positions or fruit_position in tail_positions2:
        fruit_position = [random.randint(1, BOARD_WIDTH), random.randint(1, BOARD_HEIGHT)]
    return fruit_position

def create_board(fruit_position, head_position, tail_positions, head_position2, tail_positions2):
    board = ''
    for i in range(BOARD_HEIGHT + 2):
        for j in range(BOARD_WIDTH + 2):
            if i == 0 or j == 0 or i == BOARD_HEIGHT + 1 or j == BOARD_WIDTH + 1:
                board += '#'
            elif fruit_position == [j, i]:
                board += 'F'
            elif head_position == [j, i]:
                board += 'O'
            elif head_position2 == [j, i]:
                board += 'X'
            elif [j, i] in tail_positions2:
                board += 'o'
            elif [j, i] in tail_positions:
                board += 'o'
            else:
                board += ' '
        board += '\n'
    return board

def draw(fruit_position, head_position,head_position2 ,tail_positions,tail_positions2, score1, score2,igrac1,igrac2):
    tail_positions.pop(0)
    tail_positions.append(head_position.copy())
    tail_positions2.pop(0)
    tail_positions2.append(head_position2.copy())
    board = create_board(fruit_position, head_position, tail_positions,head_position2, tail_positions2)
    os.system('cls')
    print(board)
    print(f'{igrac1}:  {score1}')
    print(f"{igrac2}:  {score2}")

current_key1 = ''
current_key2 = ''
def get_pressed_key():
    global current_key1,current_key2
    if msvcrt.kbhit():
        key =  msvcrt.getch().decode()
        if key in ['w','a','s','d']:
            current_key1 = key
        elif key in ['i','j','k','l']:
            current_key2 = key
    return current_key1,current_key2
    

def change_side(head_position):
    if head_position[0] == 0:
        head_position[0] = BOARD_WIDTH
    elif head_position[0] == BOARD_WIDTH + 1:
        head_position[0] = 1
    if head_position[1] == 0:
        head_position[1] = BOARD_HEIGHT
    elif head_position[1] == BOARD_HEIGHT + 1:
        head_position[1] = 1
    return head_position

def move1(head_position, directions):
    key1,key2 = get_pressed_key()
   
    if key1 == 'd' and directions['LEFT'] == False:
        head_position[0] += 1
        directions['UP'] = False
        directions['DOWN'] = False
        directions['RIGHT'] = True
    elif key1 == 'a' and directions['RIGHT'] == False:
        head_position[0] -= 1
        directions['UP'] = False
        directions['DOWN'] = False
        directions['LEFT'] = True
    elif key1 == 's' and directions['UP'] == False:
        head_position[1] += 1
        directions['RIGHT'] = False
        directions['LEFT'] = False
        directions['DOWN'] = True
    elif key1 == 'w' and directions['DOWN'] == False:
        head_position[1] -= 1
        directions['RIGHT'] = False
        directions['LEFT'] = False
        directions['UP'] = True
    else:
        if directions['RIGHT'] == True:
            head_position[0] += 1
        elif directions['LEFT'] == True:
            head_position[0] -= 1
        elif directions['DOWN'] == True:
            head_position[1] += 1
        elif directions['UP'] == True:
            head_position[1] -= 1
    
    head_position = change_side(head_position)
    
     
    return head_position 

def move2(head_position2,directions2):
    key1,key2 = get_pressed_key()
    if key2 == 'l' and directions2['LEFT'] == False:
        head_position2[0] += 1
        directions2['UP'] = False
        directions2['DOWN'] = False
        directions2['RIGHT'] = True
    elif key2 == 'j' and directions2['RIGHT'] == False:
        head_position2[0] -= 1
        directions2['UP'] = False
        directions2['DOWN'] = False
        directions2['LEFT'] = True
    elif key2 == 'k' and directions2['UP'] == False:
        head_position2[1] += 1
        directions2['RIGHT'] = False
        directions2['LEFT'] = False
        directions2['DOWN'] = True
    elif key2 == 'i' and directions2['DOWN'] == False:
        head_position2[1] -= 1
        directions2['RIGHT'] = False
        directions2['LEFT'] = False
        directions2['UP'] = True
    else:
        if directions2['RIGHT']:
            head_position2[0] += 1
        elif directions2['LEFT']:
            head_position2[0] -= 1
        elif directions2['DOWN']:
            head_position2[1] += 1
        elif directions2['UP']:
            head_position2[1] -= 1
        
    head_position2 = change_side(head_position2)


    return head_position2

def main():
    
    DIFFICULTY = int(input("Koju TEezinu zelite 1-10?"))
    head_position = [ BOARD_WIDTH // 4, BOARD_HEIGHT // 4]
    tail_positions = [head_position.copy()]
    head_position2 = [ (BOARD_WIDTH // 4)*2,(BOARD_HEIGHT // 4)*2]
    tail_positions2 = [head_position2.copy()]
    fruit_position = create_fruit(tail_positions,tail_positions2)
    directions = {'RIGHT': True, 'LEFT': False, 'UP': False, 'DOWN': False}
    directions2 = {'RIGHT':False,'LEFT':True,'UP':False,'DOWN':False}
    score1 = 0
    score2 = 0 
    igrac1 = input("1 igrac,unesi ime:")
    igrac2 = input("2 igrac,unesite ime:")
    while True:
        draw(fruit_position, head_position,head_position2, tail_positions,tail_positions2, score1,score2,igrac1,igrac2)
        head_position = move1(head_position, directions)
        head_position2 = move2(head_position2,directions2)         
        
        
        if head_position in tail_positions:
            print(f'Pobednik je {igrac2}')
            time.sleep(5)
            break

        if head_position2 in tail_positions2:
            print(f"Pobednik je {igrac1}")
            time.sleep(5)
            break
        
        if head_position == fruit_position:
                tail_positions.append(head_position.copy())
                score1 += 10
                fruit_position = create_fruit(tail_positions,tail_positions2)
                
        if head_position2 == fruit_position:
                tail_positions2.append(head_position2.copy())
                score2 += 10
                fruit_position = create_fruit(tail_positions,tail_positions2)
                
         

 
        if score1 == 100:
            print(f"Pobednik je {igrac1}")
            time.sleep(5)
            break
        if score2 == 100:
            print(f"Pobednik je {igrac2}")
            time.sleep(5)
            break       
            
             
        time.sleep(1 / DIFFICULTY)

main()
