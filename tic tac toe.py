import random
occupied = []
positions=[i for i in range(1,10)]
combinations=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
def gameBoard():
    print(f"""
 {positions[0]} | {positions[1]} | {positions[2]}
-----------
 {positions[3]} | {positions[4]} | {positions[5]}
-----------
 {positions[6]} | {positions[7]} | {positions[8]}
""")

def user_mov(choice):
    user_pos = int(input("Enter Position:"))
    positions[user_pos-1]=choice
    occupied.append(user_pos)
    gameBoard()
    return checkWinner(user_pos,choice)

def cpu_move(choice):
    while True:
        cpu_pos = random.randint(1,9)
        if cpu_pos in occupied:
            continue
        else:
            break
    positions[cpu_pos-1]=choice
    occupied.append(cpu_pos)
    gameBoard()
    return checkWinner(cpu_pos,choice)
    
        
          

def checkWinner(pos,choice):
    for i in range(0,len(combinations)):
        if pos in combinations[i]:
            index=combinations[i].index(pos)
            combinations[i][index]=choice
            
            
    for i in range(0,len(combinations)):
        if combinations[i][0]==choice and combinations[i][1]==choice and combinations[i][2]==choice:
            return "win"


choice = input("Enter Choice : X|0 =>")
if choice == 'X':
    cpu_choice ='0'
else:
    cpu_choice = 'X'
while True:
    msg=user_mov(choice)
    if msg=="win":
        print("user wins")
        break

    msg=cpu_move(cpu_choice)
    if msg=="win":
        print("cpu wins")
        break
