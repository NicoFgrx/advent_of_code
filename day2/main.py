input_file = 'input.txt'

your_play_dct = {
    'X' : 0,
    'Y' : 1,
    'Z' : 2,
}

your_method_dct = {
    'X' : 'loose',
    'Y' : 'draw',
    'Z' : 'win',
}

other_play_dct = {
    'A' : 0,
    'B' : 1,
    'C' : 2,
}

true_lst = [ 
    [4, 1, 7],
    [8, 5, 2],
    [3, 9, 6]
]


def first_part():
    with open(input_file, 'r') as file:
        data = file.readlines()
        total = 0
        for round in data:
            other_play, your_play = round.split()
            id_other = other_play_dct[other_play]
            id_your = your_play_dct[your_play]
            curr_score = true_lst[id_your][id_other]
            total += curr_score

    return total


def second_part():
    with open(input_file, 'r') as file:
        data = file.readlines()
        total = 0
        for round in data:
            other_play, your_method = round.split()


            id_other = other_play_dct[other_play]
            your_human_method = your_method_dct[your_method]

            if your_human_method == 'win':
                if id_other == 0: id_your = 1
                elif id_other == 1: id_your = 2
                elif id_other == 2: id_your = 0
            elif your_human_method == 'draw':
                id_your = id_other
            elif your_human_method == 'loose':
                if id_other == 0: id_your = 2
                elif id_other == 1: id_your = 0
                elif id_other == 2: id_your = 1


            curr_score = true_lst[id_your][id_other]
            total += curr_score

    return total


def main():
    first_result = first_part()
    print("The first result is {}".format(first_result))


    second_result = second_part()
    print("The second result is {}".format(second_result))



main()