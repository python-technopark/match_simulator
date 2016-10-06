import random

NUM_OF_TEAMS = 0
input_tuple = ("Краснодар\n", "ЦСКА\n", "Динамо\n", "Спартак\n", "Зенит\n") 
games = [] # changes to tuple after filling

teams = {}
table = {}

# team's names list creating
def read():
    global NUM_OF_TEAMS
    team_id = 0
    NUM_OF_TEAMS = len(input_tuple)
    for team in input_tuple:
        teams[team_id] = [team[:-1], 0, 0, 0, 0, 0, 0]  # name win lose draw score miss points
        table[team[:-1]] = team_id
        team_id += 1


def generate():
    global games
    # create temp matrix from lists
    games = [0] * NUM_OF_TEAMS
    for i in range(NUM_OF_TEAMS):
        games[i] = [0] * NUM_OF_TEAMS
    for i in range(NUM_OF_TEAMS):
        for j in range(i):
            # filling games table
            a = random.randint(0, 5)
            b = random.randint(0, 5)
            score = str(a) + ":" + str(b)
            games[i][j] = score
            games[j][i] = score[::-1]
            # filling game's list
            if a > b:
                teams[i][1] += 1
                teams[i][6] += 3
                teams[j][2] += 1
            elif a < b:
                teams[j][1] += 1
                teams[j][6] += 3
                teams[i][2] += 1
            else:
                teams[i][3] += 1
                teams[i][6] += 1
                teams[j][3] += 1
                teams[j][6] += 1
            teams[i][4] += a
            teams[i][5] += b
            teams[j][4] += b
            teams[j][5] += a
    # create constant games matrix from tuples
    for i in range(NUM_OF_TEAMS):
        games[i] = tuple(games[i])
    games = tuple(games)

# debug
'''
def print_games():
    for i in range(NUM_OF_TEAMS):
        print(games[i])
    print("\n")
'''

def print_table():
    i = 0
    while teams:
        max_id = -1
        index = 0
        for key, value in teams.items():
            if value[6] > max_id:
                max_id = value[6]
                index = key
        item = teams.pop(index)
        i += 1
        print(i, " {:<10}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}".format(*item))


def print_result():
    while True:
        print("Введите поочередно названия команд или end для выхода:\n")
        str1 = input('Введите первую команду\n')
        if str1 != "exit":
            str2 = input('Введите вторую команду\n')
            i, j = -1, -1
            for key, val in table.items():
                if key == str1:
                    i = val
                elif key == str2:
                    j = val
            if i == -1 or j == -1:
                print("Вы ошиблись в написании команды\n")
            else:
                print(games[i][j])
        else:
            print("Спасибо за использование нашей программы\n")
            break


read()
generate()
print_table()
print("\n")
print_result()
