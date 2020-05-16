# Initiated: 8/8/19 0858 PST
# Basic Functionality 8/9/19 2343 PST
# Uploaded (after a very, very long gap): 5/16/20 1330 PST

import random

word_bank = ["vacation", "tomato", "airplane", "representative", "education", "competition", "earthquake", "afternoon",
             "pancake", "discussion", "birthday", "development", "punishment", "quicksand", "aftermath", "amusement",
             "expansion", "afterthought", "plastic", "crook", "brook", "frame", "eggnog", "sidewalk", "caption", "van",
             "hose", "recess", "caption", "fireman", "sock", "holiday", "quiver", "scarecrow", "deer", "string",
             "fireman", "powder", "building", "hammer", "existence", "judge", "existence", "rice", "wren", "conviction",
             "wheel", "intelligence", "cactus", "apparel", "jewel", "soap", "business", "force", "kick", "rabbit",
             "whistle", "drain", "bottle", "creature", "bottle", "alarm", "roll", "toothpaste", "salt", "property",
             "minute", "daughter", "sun", "son", "grandfather", "grandmother", "downtown", "iron", "titanium", "rhythm",
             "history", "science", "boot", "popcorn", "stomach", "hydroxyapatite", "suggestion", "car", "hypercar",
             "summer", "winter", "jellyfish", "jam", "texture", "button", "nerve", "blade", "zebra", "stream", "flower",
             "nation", "camera", "arithmetic", "algebra", "airplane", "government", "minister", "basketball", "soccer",
             "football", "sleep", "impulse", "spider", "tiger", "India", "machine", "cricket", "voyage", "toothbrush",
             "knowledge", "wisdom", "earth", "mars", "neptune", "galaxy", "universe", "morning", "evening", "behavior",
             "advertisement", "distribution", "observation", "playground", "motion", "ladybug", "bubble", "instrument",
             "hydrant", "payment", "plantation", "friction", "experience", "apparatus", "vacuum", "weather", "chicken",
             "vacation", "connection", "bluetooth", "copper", "diamond", "chess", "volleyball", "example", "digestion",
             "bucket", "carpenter", "plate", "train", "governor", "animal", "volcano", "butter", "chalk", "lumber", "a",
             "frog", "moon", "exchange", "growth", "xylem", "phloem", "parenchyma", "sclerenchyma", "collenchyma",
             "mitochondria", "oil", "dessert", "desert", "vessel", "invention", "laptop", "furniture", "donkey", "lion",
             "waffle", "biriyani", "squid", "shark", "fire", "snow", "temperature", "constrict", "expedite", "enigma",
             "puzzle", "veneer", "permeate", "vigilance", "labyrinth", "stipulate", "sophomore", "cliff", "fragrant",
             "torque", "supercharger", "python", "fruit"]

guesses_left = [6]


def hangman():
    if guesses_left[0] == 6:
        print("                            __________________________\n"
              "                            I                  I\n"
              "                            I                  I\n"
              "                            I                  I\n"
              "                            I\n"
              "                            I\n"
              "                            I\n"
              "                            I\n"
              "                            I\n"
              "                            I\n"
              "                            I"
              "_____________________________________ ")
    elif guesses_left[0] == 5:
        print("\nLooks like the Hangman got a head!\n\n"
              "                            __________________________\n"
              "                            I                  I\n"
              "                            I                  I\n"
              "                            I                  I\n"
              "                            I                  O\n"
              "                            I\n"
              "                            I\n"
              "                            I\n"
              "                            I\n"
              "                            I\n"
              "                            I"
              "_____________________________________ ")
    elif guesses_left[0] == 4:
        print("\nLooks like the Hangman got a body!\n\n"
              "                            __________________________\n"
              "                            I                  I\n"
              "                            I                  I\n"
              "                            I                  I\n"
              "                            I                  O\n"
              "                            I                  | \n"
              "                            I                  |\n"
              "                            I                  |\n"
              "                            I\n"
              "                            I\n"
              "                            I"
              "_____________________________________ ")
    elif guesses_left[0] == 3:
        print("\nLooks like the Hangman got an arm!\n\n"
              "                            __________________________\n"
              "                            I                  I\n"
              "                            I                  I\n"
              "                            I                  I\n"
              "                            I                  O\n"
              "                            I                  | /\n"
              "                            I                  |/\n"
              "                            I                  |\n"
              "                            I\n"
              "                            I\n"
              "                            I"
              "_____________________________________ ")
    elif guesses_left[0] == 2:
        print("\nLooks like the Hangman got both arms!\n\n"
              "                            __________________________\n"
              "                            I                  I\n"
              "                            I                  I\n"
              "                            I                  I\n"
              "                            I                  O\n"
              "                            I                \\ | /\n"
              "                            I                 \\|/\n"
              "                            I                  |\n"
              "                            I\n"
              "                            I\n"
              "                            I"
              "_____________________________________ ")
    elif guesses_left[0] == 1:
        print("\nLooks like the Hangman got a leg!\n\n"
              "                            __________________________\n"
              "                            I                  I\n"
              "                            I                  I\n"
              "                            I                  I\n"
              "                            I                  O\n"
              "                            I                \\ | /\n"
              "                            I                 \\|/\n"
              "                            I                  |\n"
              "                            I                   \\\n"
              "                            I                    \\\n"
              "                            I"
              "_____________________________________ ")
    elif guesses_left[0] == 0:
        print("\nOh no!  Looks like the Hangman got both legs!\nNow, the hangman is completed.  No more guesses!\n"
              "                            __________________________\n"
              "                            I                  I\n"
              "                            I                  I\n"
              "                            I                  I\n"
              "                            I                  0\n"
              "                            I                \\ | /\n"
              "                            I                 \\|/\n"
              "                            I                  |\n"
              "                            I                 / \\\n"
              "                            I                /   \\\n"
              "                            I"
              "_____________________________________ ")


hangman_intro = ("                            __________________________\n"
                 "                            I                  I\n"
                 "                            I                  I\n"
                 "                            I                  I\n"
                 "                            I                  O\n"
                 "                            I                \\ | /\n"
                 "                            I                 \\|/\n"
                 "                            I                  |\n"
                 "                            I                 / \\\n"
                 "                            I                /   \\\n"
                 "                            I"
                 "_____________________________________ ")

guess_arena = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]

open_positions = ["1", "2", "3", "4", "5", "6", "7",
                  "8", "9", "10", "11", "12", "13", "14",
                  "15", "16", "17", "18", "19", "20", "21"]

'''
print("yo")
print(open_positions)

print(len(guess_arena))
'''

winner_sign = ("\n\n\n\ \    / /_ _| \| | \| | __| _ \ |\n"
               " \ \/\/ / | || .` | .` | _||   /_|\n"
               "  \_/\_/ |___|_|\_|_|\_|___|_|_(_)")

win_status = [""]

game_ended_status = {"found": False}

divider = ("___________________________________________________________")

turn_divider = (
    "___________________________________________________________\n___________________________________________________________")

special_characters = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", ",", ".", "?", "/", "<", ">", ";",
                      ":", "'", "\"", "[", "{", "]", "}", "\\", "|", "`", "~"]

chosen_letters = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
                  ""]

correct_chosen_letters = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
                          "", "", ""]

incorrect_chosen_letters = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
                            "", "", ""]

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

number_of_players = {"number": ""}


def find_player_name():
    global player_one_name
    global player_two_name
    if number_of_players[0] == "one":
        player_one_name = input("User, please enter your name:\n")
        if player_one_name == "":
            print("Oops!  Looks like you didn't enter anything!  Please try again!\n")
            find_player_name()
    elif number_of_players[0] == "two":
        player_one_name = input("User, please enter your name:\n")
        player_two_name = input("\nPlease enter the name of the User who will be guessing\n")


def game_type():
    try:
        print("\n\nWelcome to Hangman!\n")
        game_type_response = int(input(
            "\nWhat type of game do you want to play?\n(1) One Player Game\n(2) Setting up a game for another person\n"))
        if game_type_response == 1:
            print("\nGreat!  Let's play a One Player Game\n")
            number_of_players[0] = "one"
            find_player_name()
            one_player()
        elif game_type_response == 2:
            print("\nGreat!  Let's get the game set up!\n")
            number_of_players[0] = "two"
            find_player_name()
            two_player()
        elif game_type_response != 1 or 2:
            print("\nOops!  Looks like that was not a valid choice.  Please please enter '1' or '2'.\n")
            game_type()
    except ValueError:
        print("\nOh no!  Looks like that is not a valid input.  Please please enter '1' or '2'.\n")
        game_type()


def end_game():
    global player_one_name
    global player_two_name
    if number_of_players[0] == "one":
        if win_status[0] == "won":
            print("\n\nGreat job, " + player_one_name + "!  You won!  Thank you for playing!")
        elif win_status[0] == "lost":
            print("\nThe word was:\n" + word + "\n\n")
            print("\n\nGreat job, " + player_one_name + "!  You did a great job!  Thank you for playing!")
    elif number_of_players[0] == "two":
        if win_status[0] == "won":
            print("\n\nGreat job, " + player_two_name + "!  You won!  Thank you for playing!")
        elif win_status[0] == "lost":
            print("\nThe word was:\n" + word + "\n\n")
            print("\n\nGreat job, " + player_two_name + "!  You did a great job!  Thank you for playing!")


def display_guess_arena():
    spaces_left = len(word)
    subtract_number = len(word)
    while spaces_left != 0:
        print(guess_arena[len(word) - subtract_number] + " ", end="")
        subtract_number -= 1
        spaces_left -= 1


def one_player():
    try:
        choose_or_random = int(input("\nDo you want to choose a random word or do you want the computer to choose?"
                                     "\nThese are your options:\n(1) Choose a random word\n"
                                     "(2) Let the computer choose one for you\n"))
        if choose_or_random == 1:
            one_player_choose_word()
            word_length = len(word)
            del guess_arena[len(word):]
            del open_positions[len(word):]
            guess_loop()
        elif choose_or_random == 2:
            one_player_computer_choose_word()
            word_length = len(word)
            del guess_arena[len(word):]
            del open_positions[len(word):]
            guess_loop()
        elif choose_or_random != 1 or 2:
            print("\nOops!  Looks like that was not a valid choice.  Please please enter '1' or '2'.\n")
            one_player()
    except ValueError:
        print("\nOh no!  Looks like that is not a valid input.  Please please enter '1' or '2'.\n")
        one_player()


def one_player_choose_word():
    global word
    global word_length
    player_word_choice = int(input("\nChoose a number between 1 and " + str(len(word_bank)) + ":\n"))
    if player_word_choice > len(word_bank):
        print("\n\nOops!  Looks like that number is out of range!  Please try again!\n")
        one_player_choose_word()
    player_word_choice -= 1
    word = word_bank[player_word_choice]
    word_length = len(word)


def one_player_computer_choose_word():
    global word
    global word_length
    word = random.choice(word_bank)
    word_length = len(word)


def guess_loop():
    global player_letter_choice
    global guesses_left
    turns_left = 6
    correct_guess_letter_position = 0
    incorrect_guess_letter_position = 0
    move_number = 0
    while turns_left != 0 and game_ended_status["found"] == False:
        if '_' not in guess_arena and turns_left != 0:
            game_ended_status["found"] = True
            win_status[0] = "won"
            print("\n\nGreat job, " + player_one_name + "!  You got all the letters!  The word was:")
        print("\n")
        if move_number != 0 and game_ended_status["found"] == False:
            print(turn_divider + "\n\n")
            print("\nThese are the letters you have already chosen:\n")
            print("Correct Letters: ")
            print(correct_chosen_letters[0:correct_guess_letter_position])
            print("\nIncorrect Letters: ")
            print(incorrect_chosen_letters[0:incorrect_guess_letter_position])
            print("\n")
        display_guess_arena()
        if move_number == 0:
            player_letter_choice = input("\n\n" + player_one_name + ", choose a letter.\n").lower()
        elif move_number > 0 and game_ended_status["found"] == False:
            player_letter_choice = input(
                "\n\n" + player_one_name + ", choose a letter.  Or enter a guess for the word\n").lower()
        if player_letter_choice in word:
            if player_letter_choice == "" and game_ended_status["found"] == False:
                print("Oops!  Looks like you didn't enter a guess.  Please try again!")
                continue
            elif player_letter_choice in chosen_letters and game_ended_status["found"] == False:
                print("\nOops!  Looks like you already chose that letter.  Please try again")
                continue
            elif len(player_letter_choice) > 1:
                if player_letter_choice == word:
                    game_ended_status["found"] = True
                    win_status[0] = "won"
                    end_game()
                elif len(player_letter_choice) >= 2:
                    print("Oops!  Looks like that is not the word!  Try again!")
                    continue
            chosen_letters[correct_guess_letter_position] = player_letter_choice
            correct_chosen_letters[correct_guess_letter_position] = player_letter_choice
            correct_guess_letter_position += 1
            print("\n")
            print(divider)
            if turns_left != 0 and game_ended_status["found"] == False:
                print("\nYou got a letter!")
            print(divider)
            check_input_in_word(player_letter_choice)
            player_letter_choice = chosen_letters[move_number]
            move_number += 1
            if win_status[0] == "won":
                print(winner_sign)
            print("\n")
            print(turn_divider + "\n\n")
            if turns_left == 0:
                end_game()
        elif player_letter_choice not in word:
            if player_letter_choice == "" and game_ended_status["found"] == False:
                print("Oops!  Looks like you didn't enter a guess.  Please try again!")
                continue
            elif len(player_letter_choice) > 1 and game_ended_status["found"] == False:
                print("That was a nice guess!  But, it wasn't quite there.  Please guess again!")
            elif player_letter_choice.isnumeric() and game_ended_status["found"] == False:
                print("Sorry!  Looks like you entered a number!  Keep going!")
                continue
            elif not player_letter_choice.isnumeric():
                if player_letter_choice in incorrect_chosen_letters:
                    print("Oops!  You chose that letter already.  It is still an incorrect guess.  Try again!")
                elif player_letter_choice not in incorrect_chosen_letters:
                    chosen_letters[incorrect_guess_letter_position] = player_letter_choice
                    incorrect_chosen_letters[incorrect_guess_letter_position] = player_letter_choice
                    move_number += 1
                    turns_left -= 1
                    incorrect_guess_letter_position += 1
                    print("Sorry!  Looks like that letter is not in the word.")
                    guesses_left[0] -= 1
                    print(turn_divider + "\n\n")
                    hangman()
                    if turns_left == 0:
                        win_status[0] = "lost"
                        end_game()


def two_player_guess_loop():
    del guess_arena[len(word):]
    del open_positions[len(word):]
    if game_ended_status["found"] == False:
        print("\nNow, it is time for " + player_two_name + " to play.")
    global player_letter_choice
    move_number = 0
    turns_left = 6
    correct_guess_letter_position = 0
    incorrect_guess_letter_position = 0
    while turns_left != 0 and game_ended_status["found"] == False:
        if '_' not in guess_arena and turns_left != 0:
            game_ended_status["found"] = True
            win_status[0] = "won"
            print("\n\nGreat job, " + player_two_name + "!  You got all the letters!  The word was:")
        print("\n")
        if move_number != 0 and game_ended_status["found"] == False:
            print(turn_divider + "\n\n")
            print("\nThese are the letters you have already chosen:\n")
            print("Correct Letters: ")
            print(correct_chosen_letters[0:correct_guess_letter_position])
            print("\nIncorrect Letters: ")
            print(incorrect_chosen_letters[0:incorrect_guess_letter_position])
            print("\n")
        display_guess_arena()
        if move_number == 0:
            player_letter_choice = input("\n\n" + player_two_name + ", choose a letter.\n").lower()
        elif move_number > 0 and game_ended_status["found"] == False:
            player_letter_choice = input(
                "\n\n" + player_two_name + ", choose a letter.  Or enter a guess for the word\n").lower()
        if player_letter_choice in word:
            if player_letter_choice == "" and game_ended_status["found"] == False:
                print("Oops!  Looks like you didn't enter a guess.  Please try again!")
                continue
            elif player_letter_choice in chosen_letters and game_ended_status["found"] == False:
                print("\nOops!  Looks like you already chose that letter.  Please try again")
                continue
            elif len(player_letter_choice) > 1:
                if player_letter_choice == word:
                    game_ended_status["found"] = True
                    win_status[0] = "won"
                    end_game()
                elif len(player_letter_choice) >= 2:
                    print("Oops!  Looks like that is not the word!  Try again!")
                    continue
            chosen_letters[correct_guess_letter_position] = player_letter_choice
            correct_chosen_letters[correct_guess_letter_position] = player_letter_choice
            correct_guess_letter_position += 1
            print("\n")
            print(divider)
            if turns_left != 0 and game_ended_status["found"] == False:
                print("\nYou got a letter!")
            print(divider)
            check_input_in_word(player_letter_choice)
            player_letter_choice = chosen_letters[move_number]
            move_number += 1
            if win_status[0] == "won":
                print(winner_sign)
            print("\n")
            print(turn_divider + "\n\n")
            if turns_left == 0:
                end_game()
        elif player_letter_choice not in word:
            if player_letter_choice == "" and game_ended_status["found"] == False:
                print("Oops!  Looks like you didn't enter a guess.  Please try again!")
                continue
            elif len(player_letter_choice) > 1 and game_ended_status["found"] == False:
                print("That was a nice guess!  But, it wasn't quite there.  Please guess again!")
            elif player_letter_choice.isnumeric() and game_ended_status["found"] == False:
                print("Sorry!  Looks like you entered a number!  Keep going!")
                continue
            elif not player_letter_choice.isnumeric():
                if player_letter_choice in incorrect_chosen_letters:
                    print("Oops!  You chose that letter already.  It is still an incorrect guess.  Try again!")
                elif player_letter_choice not in incorrect_chosen_letters:
                    chosen_letters[incorrect_guess_letter_position] = player_letter_choice
                    incorrect_chosen_letters[incorrect_guess_letter_position] = player_letter_choice
                    move_number += 1
                    turns_left -= 1
                    incorrect_guess_letter_position += 1
                    print("Sorry!  Looks like that letter is not in the word.")
                    guesses_left[0] -= 1
                    print(turn_divider + "\n\n")
                    hangman()
                    if turns_left == 0:
                        win_status[0] = "lost"
                        end_game()


def check_input_in_word(player_letter_choice):
    position_checked = 0
    while position_checked != word_length:
        if word[position_checked] == player_letter_choice:
            guess_arena[position_checked] = player_letter_choice
        position_checked += 1


def two_player():
    global word
    global word_length
    word = input("\n" + player_one_name + ", enter a single word for " + player_two_name + " to guess.\n")
    if " " in word:
        print("\nOops!  Looks like you entered multiple words!  Please Try Again with a single word.")
        two_player()
    word_length = len(word)
    word_check_length = word_length - 1
    word_checked = word_check_length
    word_check_loop_number = 0
    if word.isnumeric():
        print("\nOops!  Looks like you entered a number.  Try again.  Use only letters.\n")
        two_player()
    while word_checked != 0:
        try:
            if word[word_check_length - word_check_loop_number] in numbers:
                word_checked -= 1
                word_check_loop_number += 1
                print(
                    "\nOops!  Looks like you included a number or numbers in the word.  Try again.  Use only letters.\n")
                two_player()
            elif word[0] in numbers:
                print(
                    "\nOops!  Looks like you included a number or numbers in the word.  Try again.  Use only letters.\n")
                two_player()
            elif word[word_check_length - word_check_loop_number] in special_characters:
                print(
                    "\nOops!  Looks like you included special characters in the word.  Try again.  Use only letters.\n")
                two_player()
            else:
                two_player_guess_loop()
        except IndexError:
            print("\nOops!  You didn't enter anything.  Try Again.")
            two_player()


print(hangman_intro)
game_type()
