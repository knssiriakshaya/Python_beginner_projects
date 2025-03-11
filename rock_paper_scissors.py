import random

your_score = 0
computer_score = 0

def get_user_choice():
    """
    Function to get user's choice (rock, paper, or scissors)
    """
    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ").strip().lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice! Please enter 'rock', 'paper', or 'scissors'.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    global your_score, computer_score;

    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
         
        your_score = your_score + 1
        return "Congratulations! You win this round!"
    else:
        computer_score = computer_score + 1
        return "Computer wins this round!"

def overall_winner(you_score, computer_score):
    if your_score > computer_score:
        return("You won the overall match")
    elif your_score < computer_score:
        return("Computer won the overall match")
    else:
        return("The match is tied")


if __name__ == '__main__':
    print("Let's play Rock, Paper, Scissors!")
    n = int(input("How many rounds do you want to play? "))
    print("This game is the best of ",n,"!")
    print("\n")

    while n > 0:
        print(f"Round: {n}")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        print(determine_winner(user_choice, computer_choice))

        n = n - 1
        
    print("\n")
    print(overall_winner(your_score, computer_score))

    
