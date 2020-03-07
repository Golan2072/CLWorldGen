# stellagama.py
# A module with various useful functions by Omer Golan-Joel
# v3.2 - March 7th, 2020
# This is open source code, feel free to use it for any purpose
# contact me at golan2072@gmail.com

# import modules
import random
import os
import platform


# functions
def yn():
    query = True
    while query:
        answer = input("Y/N: ")
        if answer.lower() == "y":
            return True
            break
        if answer.lower() == "n":
            return False
            break
        else:
            print("Invalid Answer")


def dice(n, sides):
    die = 0
    roll = 0
    while die < n:
        roll = roll + random.randint(1, sides)
        die += 1
    return roll


def pseudo_hex(num):
    num = int(num)
    code = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q",
            "E", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    num = code[num]
    return num


def current_dir():
    if platform.system() == "Windows":
        directory = os.listdir(".\\")
    else:
        directory = os.getcwd()
    return directory


def check_file_exists(check_file):
    if check_file in os.listdir():
        file_exists = True
    else:
        file_exists = False
    return file_exists


def savefile(extension):
    filename = str(input("Please enter file name to save: "))
    filecheck = filename + "." + extension
    if check_file_exists(filecheck):
        print(" ")
        print("File already exists. Overwrite?")
        overwrite = yn()
        if overwrite:
            pass
        if not overwrite:
            filename = input("Please enter new file name to generate: ")
    filename = filename + "." + extension
    return filename


def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')


def random_line(filename):
    with open(filename, "r") as line_list:
        line = random.choice(line_list.readlines())
        line = line.strip()
    return line


def list_stringer(input_list):
    output_list = []
    for item in input_list:
        output_list.append(str(item))
    return ' '.join(output_list)