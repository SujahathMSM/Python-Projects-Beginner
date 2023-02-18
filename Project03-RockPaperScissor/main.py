import random


def play():
    user = input(" 'r' for rock, 'p' for paper and 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])
    if user == computer:
        return 'it\'s a tie'
    # to win the game
    # r>s, s>p, p > r
    if is_win(user, computer):
        return "You Won"
    return "You Lost"


def is_win(player, opponent):
    if (player == 'r' and opponent == "s") or (player == 's' and opponent == "p") or (
            player == 'p' and opponent == "r"):
        return True


print(play())
