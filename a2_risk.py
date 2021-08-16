"""
CP1401 2020-2 Assignment 2
Run the Risk
Student Name: Gurpreet Singh
Date started: 29/09/2020

Pseudocode: (Only for main, play_turn and determine_results functions)
MENU = "(P)lay \n(I)nstructions \n(D)isplay Report \n(S)how Statistics \n(Q)uit"
STARTING_BALANCE = 1000
CONSERVATIVE_CHANCE = 66
CONSERVATIVE_REWARD = .2
AGGRESSIVE_CHANCE = 45
AGGRESSIVE_REWARD = .6
SILLY_CHANCE = 5
SILLY_REWARD = 1.1
VALID_GAME_CHOICES = ["C", "A", "S"]

function main()
    balance = STARTING_BALANCE
    balance_outcomes = []
    display Welcome message
    display MENU
    get menu_choice
    while menu_choice is not "q"
        if menu_choice is "i"
            display instructions
        else if menu_choice is "p"
            balance_outcome = play_turn(balance)
            balance_outcomes.append(balance_outcome)
            balance += balance_outcome
        else if menu_choice is "d"
            display_results(balance_outcomes, STARTING_BALANCE)
        else if menu_choice is "s"
            display_statistics(balance_outcomes)
        else
            display error message
        display MENU
        get menu_choice
    display farewell message

function play_turn(amount)
    risk_amount = get valid_amount(amount)
    get game_choice
    while game_choice is not in VALID_GAME_CHOICES
        display error message
        get game_choice
    if game_choice is "c":
        game_result = determine_result(CONSERVATIVE_CHANCE, CONSERVATIVE_REWARD, risk_amount)
        return game_result
    else if game_choice is "a"
        game_result = determine_result(AGGRESSIVE_CHANCE, AGGRESSIVE_REWARD, risk_amount)
        return game_result
    else if game_choice is "s"
        game_result = determine_result(SILLY_CHANCE, SILLY_REWARD, risk_amount)
        return game_result

function determine_result(risk_factor, chance_reward, amount)
    draw_result = random.randint(1, 100) <= risk_factor
    if draw_result stands True
        gain = chance_reward * amount
        display win message
        return gain
    else
        display loss message
        return -amount
"""
import random

MENU = "(P)lay \n(I)nstructions \n(D)isplay Report \n(S)how Statistics \n(Q)uit"
STARTING_BALANCE = 1000
CONSERVATIVE_CHANCE = 66
CONSERVATIVE_REWARD = .2
AGGRESSIVE_CHANCE = 45
AGGRESSIVE_REWARD = .6
SILLY_CHANCE = 5
SILLY_REWARD = 1.1
VALID_GAME_CHOICES = ["C", "A", "S"]  # list for all valid game choices


def main():
    """Run the Risk Game program"""
    balance = STARTING_BALANCE
    balance_outcomes = []  # to store all the results after playing one turn
    print("Welcome to Run the Risk")
    print(MENU)
    menu_choice = input("Choose: ").upper()
    while menu_choice != "Q":
        if menu_choice == "I":
            print_instructions()
        elif menu_choice == "P":
            balance_outcome = play_turn(balance)
            balance_outcomes.append(balance_outcome)
            balance += balance_outcome
        elif menu_choice == "D":
            display_results(balance_outcomes, STARTING_BALANCE)
        elif menu_choice == "S":
            display_statistics(balance_outcomes)
        else:
            print("Invalid Selection")
        print(MENU)
        menu_choice = input("Choose: ").upper()
    print("Thank you for playing.")


def play_turn(amount):
    """Gets valid amount to bet and game choice to return the calculated amount from one play/turn

                :parameter amount: The initial balance before playing a turn to bet money on Run the Risk
                :return: calculated amount after determining result of the game choice
    """

    risk_amount = get_valid_amount(amount)
    game_choice = input("C)onservative, A)ggressive, S)illy: ").upper()
    while game_choice not in VALID_GAME_CHOICES:
        print("Please choose from the available options.")
        game_choice = input("C)onservative, A)ggressive, S)illy: ").upper()
    if game_choice == "C":
        game_result = determine_result(CONSERVATIVE_CHANCE, CONSERVATIVE_REWARD, risk_amount)
        return game_result
    elif game_choice == "A":
        game_result = determine_result(AGGRESSIVE_CHANCE, AGGRESSIVE_REWARD, risk_amount)
        return game_result
    elif game_choice == "S":
        game_result = determine_result(SILLY_CHANCE, SILLY_REWARD, risk_amount)
        return game_result


def determine_result(risk_factor, chance_reward, amount):
    """
    Calculates and prints result for the given chance percent, returns the amount won or amount lost

        :parameter risk_factor: Percentage chance of success in one play turn
        :parameter chance_reward: Winning amount increment depending on game_choice
        :parameter amount: amount chosen by user to bet in one play turn

        :return: calculated amount for both cases in draw_result ( win or loss )
    """

    draw_result = random.randint(1, 100) <= risk_factor  # to check if random number is within the winning chance
    if draw_result:
        gain = chance_reward * amount
        print(f"Congratulations! You earned {gain:.2f}")
        return gain
    else:
        print(f"Oh... You lost ${amount:.2f}")
        return -amount


def get_valid_amount(balance):
    """gets valid amount as per game requirements (less than the balance and greater than zero)"""

    risk_money = float(input(f"Amount to risk (up to ${balance:.2f}): $"))
    while balance < risk_money or risk_money < 0:
        print("You can't risk a negative amount or more than you have.")
        risk_money = float(input(f"Amount to risk (up to ${balance:.2f}): $"))
    return risk_money


def print_instructions():
    """displays the Game instructions"""

    print("Run the Risk!")
    print("Each turn, you can risk some of your cash to win rewards. ")
    print("Will you be: ")
    print("- conservative (66% chance for a +20% reward), ")
    print("- aggressive (45% chance for a +60% reward),")
    print("- silly (5% chance for a +110% reward)?")
    print("If your risk-taking doesn't pay off, you lose the amount you choose to risk.")


def display_results(records, balance):
    """displays the Game results"""

    if len(records) == 0:
        print("No risks taken yet. Go on...")
    else:
        print(f"Here is a summary of your {len(records)} turns")
        print("Risk-Reward Record:")
        print(f"Starting balance: ${balance:.2f}")
        for record in records:
            print(f"${record:10.2f}  -> $ {balance + record:8.2f}")
            balance += record
        print(f"Current balance:$ {balance:8.2f}")


def display_statistics(records):
    """displays the statistics of the game as per format requirements"""

    gains = 0
    losses = 0
    if len(records) == 0:
        print("There are no statistics if you don't take any risks.")
    else:
        for amount in records:
            if amount >= 0:
                gains += 1
            else:
                losses += 1
        gain_percent = gains / len(records) * 100
        loss_percent = losses / len(records) * 100
        print(f"Maximum gain: ${max(records):.2f}")
        print(f"Maximum loss: ${min(records):.2f}")
        print(f"{gain_percent:5.1f}% of your turns were gains   ({gains}/{len(records)})")
        print(f"{loss_percent:5.1f}% of your turns were losses  ({losses}/{len(records)})")
        print("Results in sorted order: ")
        for amount in sorted(records):
            print(f"${amount:8.2f}")


main()
