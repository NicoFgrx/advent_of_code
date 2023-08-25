input_file = "input.txt"

wood = []

def build_wood():

    with open(input_file, 'r') as file:
        for line in file:
            line = line.strip()
            list_lst = list()
            for id in line:
                list_lst.append(id)

            wood.append(list_lst)

    return 0

def first_part():

    result = {False: 0, True:0}

    border_x_min = 0
    border_x_max = len(wood[0])

    border_y_min = 0
    border_y_max = len(wood)

    # outside
    perimeter = 2*border_y_max + 2*border_x_max - 4
    result[True] = perimeter

    scenic_score_buff = 0

    # inside
    for y in range(border_y_min+1, border_y_max-1, 1):
        for x in range(border_x_min+1, border_x_max-1, 1):


            current_tree = wood[y][x]

            down = False
            upper = False
            left = False
            right = False
            visible = True


            cpt = 0
            for i in range(y+1, border_y_max,1):
                cpt += 1
                down = False
                if current_tree <= wood[i][x]:
                    down = True
                    break

            scenic_score = cpt

            cpt = 0
            for i in range(y-1, -1, -1):
                cpt += 1
                upper = False
                if current_tree <= wood[i][x]:
                    upper = True
                    break

            scenic_score = scenic_score*cpt

            cpt = 0
            for i in range(x+1, border_x_max,1):
                cpt += 1
                left = False
                if current_tree <= wood[y][i]:
                    left = True
                    break

            scenic_score = scenic_score*cpt

            cpt = 0
            for i in range(x-1, -1, -1):
                cpt += 1
                right = False
                if current_tree <= wood[y][i]:
                    right = True
                    break

            scenic_score = scenic_score*cpt

            if down and upper and right and left:
                visible = False

            print("DEBUG for x: {} y: {}, scenic:{}".format(x, y, scenic_score))

            if scenic_score > scenic_score_buff:
                scenic_score_buff = scenic_score

            result[visible] += 1
            print(result)


    return result[True], scenic_score_buff

def second_part():
    pass

def main():
    build_wood()


    first_result, second_result = first_part()
    print("The first result is {}".format(first_result))


    print("The second result is {}".format(second_result))




    return 0

main()
