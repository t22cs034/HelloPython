import random

def rps():
    choices = [0, 1, 2]
    cpu_choice = random.choice(choices)
    
    user_choice = int(input("じゃんけん[0:グー 1:チョキ 2:パー]:"))
    
    if user_choice not in choices:
        print("無効な選択です.")
        return
    
    if user_choice == 0:
        user_hand = "グー"
    elif user_choice == 1:
        user_hand = "チョキ"
    elif user_choice == 2:
        user_hand = "パー"
        
    if cpu_choice == 0:
        cpu_hand = "グー"
    elif cpu_choice == 1:
        cpu_hand = "チョキ"
    elif cpu_choice == 2:
        cpu_hand = "パー"
    
    print("あなたの選択:", user_hand)
    print("CPUの選択:", cpu_hand)
    
    if user_choice == cpu_choice:
        print("引き分けです！")
    elif (user_choice == 0 and cpu_choice == 1) or \
         (user_choice == 1 and cpu_choice == 2) or \
         (user_choice == 2 and cpu_choice == 0):
        print("あなたの勝ちです！")
    else:
        print("CPUの勝ちです！")
        
rps()