import random

hand = ['グー','チョキ','パー']
result = ['あいこです','Computerの勝ちです','Playerの勝ちです']

print("入力は　1:グー, 2:チョキ, 3:パー　です\n")


# 1~3の値が入力されるまで無限ループ
while(1):
    print("じゃんけん ...")
    player = input('>')
    
    if player=='1' or player=='2' or player=='3':
        break
    else:
        print("入力は　1:グー, 2:チョキ, 3:パー　です\n")

        
# 入力された値を0~2に修正する
player = int(player)-1
print('Player   :'+hand[player])

# コンピュータの手はランダムに選ぶ
computer = random.randint(0,2)
print('Computer :'+hand[computer])


# 勝敗を決定する
judge = (player - computer + 3) % 3


print('\n'+result[judge])
