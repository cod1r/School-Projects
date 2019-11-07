import random


def numberToName(number):
    # Implement Function
    # Sees what number the parameter taken is equal to and returns the string value associated with that number
    if number == 1:
        return "rock"
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'scissors'


def rockPaperScissors(userchoice):
    # Implement Function
    cchoose = numberToName(random.randint(1, 3))
    # checks to see if what the computer chooses and what the player chooses will allow the computer to win and prints
    # out the necessary information to the console
    if (cchoose == 'rock' and userchoice == 'scissors') or cchoose == 'scissors' and userchoice == 'paper' \
            or cchoose == 'paper' and userchoice == 'rock':
        print('Player 1 chooses ' + userchoice)
        print('Player 2 chooses ' + cchoose)
        print('Player 2 Wins')
        return 'L'
    # checks to see if what the computer chooses and what the player chooses will allow the player to win and prints
    # out the necessary information to the console
    elif (cchoose == 'rock' and userchoice == 'paper') or cchoose == 'paper' and userchoice == 'scissors' \
            or cchoose == 'scissors' and userchoice == 'rock':
        print('Player 1 chooses ' + userchoice)
        print('Player 2 chooses ' + cchoose)
        print('Player 1 Wins')
        return 'W'
    # if the computer and the player both choose the same choice then it prints out tie and what they chose
    elif cchoose == userchoice:
        print('Player 1 chooses ' + userchoice)
        print('Player 2 chooses ' + cchoose)
        print('Player 1 and Player 2 tie')
        return 'T'


def countLetters(word, char):
    # Implement Function
    # checks to see if the current match is tied and if it is then a zero is returned
    # indicating that nothing valuable happened
    if char == 'T':
        return 0
    # if somebody wins return how many wins they have
    elif char == 'W':
        times = 0
        for x in word:
            if x == char:
                times += 1
        return times
    # if somebody loses return how many losses they have
    elif char == 'L':
        times = 0
        for x in word:
            if x == char:
                times += 1
        return times


if __name__ == '__main__':
    userInput = 0
    # starts the loop once the program is run
    while userInput != -1:
        print("\nPlease select one of the menu options")
        print(" 1. Start game of rock, paper, scissors")
        print("-1. to exit the program.")
        userInput = input()
        # if player enters anything but a 1 or a -1 it will catch the error and print that msg
        if userInput.strip() != '1' and userInput.strip() != '-1':
            print('Please choose only those values')
        # if player enters in a 1 to start the game then it will start a loop that takes in the game options they have
        if userInput == "1":
            print('\nStarting Game... Input 1 for rock, 2 for paper or 3 for scissor.\n')
            # the string that will represent the match history for both players
            matchHistory = ""
            # runs a loop
            while True:
                # Implement Code
                # tries to take in a number input and if the player doesn't enter in a number an error is catched
                # and a custom msg is printed
                try:
                    userInput = int(input())
                except ValueError:
                    print('Not a number, please try again')
                    break
                # puts a method return in a variable
                c = rockPaperScissors(numberToName(userInput))
                # tries to add a character to a string and if it tries to add a non-string, a custom msg is printed
                try:
                    matchHistory += c
                except TypeError:
                    print('Not an acceptable answer')
                # checks to see if there are 2 wins/losses for any player and will print who has won
                # and then breaking the loop
                if countLetters(matchHistory, c) == 2:
                    if c == 'L':
                        print("Player 2 has won " + str(countLetters(matchHistory, c)) + " games out of 3")
                    elif c == 'W':
                        print("Player 1 has won " + str(countLetters(matchHistory, c)) + " games out of 3")
                    break
        # if the player doesn't want to play the program will end
        elif userInput == '-1':
            break
