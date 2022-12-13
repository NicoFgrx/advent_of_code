import re

input_file = 'input.txt'

def create_list():

    with open(input_file, 'r') as file:

        line = file.readline()

        array_dct = {}

        while line != "\n":
            cpt = 0
            for carac in range(0, len(line), 4):
                cpt += 1
                # print("DEBUG " + str(cpt) + " : " + line[carac:carac+3])
                if re.match("\[\w\]", line[carac:carac+3]):
                    letter = line[carac:carac+3][1]
                    # print("DEBUG letter : "+letter)
                    if cpt in array_dct.keys():
                        array = list(array_dct[cpt])
                        array.insert(0,letter)
                        array_dct[cpt] = array
                    else:
                        array = []
                        array.append(letter)
                        array_dct[cpt] = array


                           
            # print("DEBUG line = " + line)
            # print("DEBUG dict "+ str(array_dct))
            line = file.readline()

    return array_dct

def display(array_dct):
    print("--"*10)
    for i in sorted(array_dct.keys()):
        print(i, end=' : ')
        print(array_dct[i])
    print('--'*10)


def first_part():
    array_dct = create_list()

    print("Avant")
    display(array_dct)

    with open(input_file, 'r') as file:
        data = file.readlines()
        pattern = "move\s(\d{1,})\sfrom\s(\d)\sto\s(\d)"
        cpt = 0
        for instruction in data:
            if re.search(pattern, instruction):


                
                m = re.match(pattern, instruction)
                nb, begin, end = m.group(1,2,3)

                # pts = instruction.split(" ")
                # nb = pts[1]
                # begin = pts[3]
                # end = pts[5]


                nb = int(nb)
                begin = int(begin)
                end = int(end)
                


                array = list(array_dct[begin])
                sub_lst_inf = array[:len(array)-nb]
                sub_lst_sup = array[len(array)-nb:]

                sub_lst_sup.reverse() # enlever le reverse pour part2
                
                array_dct[begin] = sub_lst_inf
                array = list(array_dct[end])
                array += sub_lst_sup
                array_dct[end] = array

                print("DEBUG")
                print(instruction)
                print('moving {} from {} to {}...'.format(nb, begin, end))
                display(array_dct)


        result = []

        for id in sorted(array_dct.keys()):
            array = list(array_dct[id])

            if len(array) > 0:
                result.append(array[-1])

        print(result)

    print("Après")
    display(array_dct)
 
    return result

def second_part():
    with open(input_file, 'r') as file:

        data = file.readlines()
        total = 0
        for sections in data:
            pass

    return total

def main():

    create_list()

    result = first_part()
    first_result = "".join(result)
    print("The first result is {}".format(first_result))


    second_result = second_part()
    print("The second result is {}".format(second_result))



main()