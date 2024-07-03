import os
import random as rand
import sys
import time
import json

def input_menu(text, number_of_options):
    while True:
        try:
            choice = int(input(text))
            if choice >= 1 and choice <= number_of_options:
                break
        except ValueError:
            os.system("clear")
    return choice

def useless_loading():
    loading_message = "Loading"
    for _ in range(3):
        print("""
██████╗░██╗░░░██╗░██████╗██╗███╗░░██╗███████╗░██████╗░██████╗
██╔══██╗██║░░░██║██╔════╝██║████╗░██║██╔════╝██╔════╝██╔════╝
██████╦╝██║░░░██║╚█████╗░██║██╔██╗██║█████╗░░╚█████╗░╚█████╗░
██╔══██╗██║░░░██║░╚═══██╗██║██║╚████║██╔══╝░░░╚═══██╗░╚═══██╗
██████╦╝╚██████╔╝██████╔╝██║██║░╚███║███████╗██████╔╝██████╔╝
╚═════╝░░╚═════╝░╚═════╝░╚═╝╚═╝░░╚══╝╚══════╝╚═════╝░╚═════╝░

░██████╗██╗███╗░░░███╗██╗░░░██╗██╗░░░░░░█████╗░████████╗░█████╗░██████╗░
██╔════╝██║████╗░████║██║░░░██║██║░░░░░██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
╚█████╗░██║██╔████╔██║██║░░░██║██║░░░░░███████║░░░██║░░░██║░░██║██████╔╝
░╚═══██╗██║██║╚██╔╝██║██║░░░██║██║░░░░░██╔══██║░░░██║░░░██║░░██║██╔══██╗
██████╔╝██║██║░╚═╝░██║╚██████╔╝███████╗██║░░██║░░░██║░░░╚█████╔╝██║░░██║
╚═════╝░╚═╝╚═╝░░░░░╚═╝░╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝
""")
        loading_message += "."
        print(loading_message)
        time.sleep(1)
        os.system("clear")
    start_menu()

def start_menu():
    choice = input_menu("""
Welcome to the game! What do you want to do?

1. Start
2. Quit

(Please only enter either 1 or 2. Any other input will be ignored.)
""", 2)

    if choice == 1:
        game()
    else:
        exit()

def game():
    player_name = str(input("Enter your name: ")).capitalize()
    company_name = str(input("Enter a name for your company: ")).capitalize()
    os.system("clear")
    print(f"Welcome, {player_name}! You are the CEO of {company_name}. To start your business, you have been able to gather $5000 from friends and family and have hired 5 employees to work with you. Don't go bankrupt!")
    
    day = 0
    balance = 5000
    number_of_employees = 5
    daily_customers = 20
    total_customers = 0
    
    running = True
    while running:
        day += 1
        choice = input_menu(f"""
(Day: {day}, Balance: ${balance}, Number of employees: {number_of_employees}, Total costomers: {total_customers})

What do you want to do, {player_name}?

1. Work
2. Upgrade business/hire workers
3. Invest
4: Advertise {company_name}
5. Loan from the bank
6. Take the day off
7. Quit

(Please only enter either 1, 2, 3, 4, 5, 6 or 7. Any other input will be ingnored)
""", 7)
        if choice == 1:
            total_customers += daily_customers
            revenue = rand.randint(daily_customers * 10, daily_customers * 20)
            losses = number_of_employees * 30 + revenue / 3
            profit = revenue - losses
            print(f"While working, you gained ${revenue} in revenue and lost ${losses} in losses. ${number_of_employees * 30} was spent on employees' paychecks, and ${revenue / 3} was spent on costs of items. Your total profit is ${profit}.")
            os.system("clear")

        elif choice == 2:
            choice = input_menu(f"""
(Day: {day}, Balance: ${balance}, Number of employees: {number_of_employees}, Total customers: {total_customers})

What do you want to do, {player_name}?

1. Upgrade business
2. Hire employees

(Please only enter either 1 or 2. Any other input will be ignored.)
""", 2)
            if choice == 1:
                
                with open("game_data.json", "r") as f:
                    game_data = json.load(f)

                    if len(game_data["other_info"]["upgrade cost list"]) < game_data["other info"]["business level"]:
                        game_data["other info"]["upgrade cost list"].append(game_data["other info"]["upgrade cost list"][-1] + game_data["other info"]["upgrade cost list"][-2])
                    

useless_loading()