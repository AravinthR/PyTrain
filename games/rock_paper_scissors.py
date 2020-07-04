# rock beat scissors
# scissors beat paper
# paper beat rock

usr1 = input("Enter user 1 name: ")
usr2 = input("Enter user 2 name: ")

usr1_choice = input("%s, Do you want to choose rock, paper or scissors: " % usr1)
usr2_choice = input("%s, Do you want to choose rock, paper or scissors: " % usr2)


def rps_logic(u1_choice, u2_choice):
    if u1_choice == u2_choice:
        return "It's a tie!"
    elif u1_choice == 'rock':
        if u2_choice == 'scissors':
            return "Rock wins!"
        else:
            return "Paper wins!"
    elif u1_choice == 'scissors':
        if u2_choice == 'paper':
            return "Scissors win!"
        else:
            return "Rock wins!"
    elif u1_choice == 'paper':
        if u2_choice == 'rock':
            return "Paper wins!"
        else:
            return "Scissors win!"
    else:
        return "Invalid input! You have not entered rock, paper or scissors, try again."


print(rps_logic(usr1_choice, usr2_choice))
