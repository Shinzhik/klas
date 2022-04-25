
import random
user_action = input("Сделайте выбор - rock; paper; scissors - ")
possible_actions = ["rock","paper","scissors"]
computer_action = random.choice(possible_actions)
print(f"\nВы выбрали {user_action}, компьютер выбрал {computer_action}.\n")
if user_action == computer_action:
    print('Ничья!')
elif user_action == "rock":
    ('Поздравляем! Вы победили!')
    if computer_action == "scissors":
        print('Поздравляем! Вы победили!')
    else:
        print('Вы проиграли :(')
elif user_action == "paper":
    print('Поздравляем! Вы победили!')
    if computer_action == "rock":
        print('Поздравляем! Вы победили!')
    else:
            print('Вы проиграли :(')
elif user_action == "scissors":
    if computer_action == "paper":
        print('Поздравляем! Вы победили!')
    else:
        print('Вы проиграли :(')
