"""
randomly select an entry from a list of encounters
"""

import csv
import random
import textwrap

"""
All lists need to be declared as global variables and added to encounter options
"""
COMMON_HEARTH = "hearth_encounters.csv"
WILDERNESS_ENCOUNTERS = "wilderness_encounters.csv"
CITY_ENCOUNTERS = "city_encounters.csv"
ENCOUNTER_OPTIONS = [COMMON_HEARTH, WILDERNESS_ENCOUNTERS, CITY_ENCOUNTERS]


def main():
    run = True
    while run:
        # request file to open
        user_selection = main_menu()
        # open the csv
        current_list = open_csv(user_selection)
        # select a random option (*to do for later unless already used)
        current_encounter = randomise_option(current_list)
        # TODO: add the option to an exceptions list
        # print the random option
        display_result(current_encounter)
        quit = (input("Would you like to quit? Y/N").upper())
        if quit == "Y":
            run = False


def main_menu():
    print("Welcome to the encounter generator. Please enter the number of the encounter list would you like to use:")
    for i in ENCOUNTER_OPTIONS:
        print("{} for {}".format(ENCOUNTER_OPTIONS.index(i),i))
    user_choice = int(input(">>>"))
    selection = ENCOUNTER_OPTIONS[user_choice]
    return selection


def open_csv(selection):
    file = open(selection, 'r')
    read_file = csv.reader(file, delimiter=',')
    return read_file


def randomise_option(enc_list):
    dice_roll = random.randint(1,100)
    for i in enc_list:
        if int(i[0]) == dice_roll:
            generated_encounter = i[1]
            return generated_encounter
    enc_list.close()


def display_result(encounter):
    wrapped_text = textwrap.TextWrapper(width=80,
                                        initial_indent=" " * 4,
                                        subsequent_indent=" " * 4,
                                        break_long_words=False,
                                        break_on_hyphens=False)
    print(wrapped_text.fill(encounter))


main()
