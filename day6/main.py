input_file='input.txt'

def first_part():
    result = list()

    with open(input_file, 'r') as file:
        data = file.readlines()
        result = list()
        for line in data:
            result.append(find_first_substring(line, 4))

        return result           
        

def find_first_substring(line,pas):
    print("DEBUG : line = {}".format(line))
    for i in range(len(line)-pas):
        idx = i+pas
        buffer = line[i:idx]

        print('DEBUG : buffer = {}'.format(buffer))

        letter_lst = list()
        for letter in buffer:

            if letter not in letter_lst:
                letter_lst.append(letter)

            if len(letter_lst) == pas:
                print('DEBUG : letter_lst = {}'.format(letter_lst))
                return idx

    return -1

def second_part():
    result = list()

    with open(input_file, 'r') as file:
        data = file.readlines()
        result = list()
        for line in data:
            result.append(find_first_substring(line, 14))

        return result   

def main():

    first_result = first_part()
    print("The first result is {}".format(first_result))


    second_result = second_part()
    print("The second result is {}".format(second_result))



main()