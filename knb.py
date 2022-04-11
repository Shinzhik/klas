if user_action == computer_action:
    print('Ничья!')
elif user_action == "rock":
    if computer_action == "scissors":
        print('Поздравляем! Вы победили!')
    else:
        print('Вы проиграли :(')
elif user_action == "paper":
    if computer_action == "rock":
        print('Поздравляем! Вы победили!')