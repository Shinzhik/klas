import random
user_action = input("Сделайте выбор - rock; paper; scissors - ")
possible_actions = ["rock","paper","scissors"]
computer_action = random.choice(possible_actions)
print(f"\nВы выбрали {user_action}, компьютер выбрал {computer_action}.\n")
