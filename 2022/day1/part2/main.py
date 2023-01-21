from node import Elf

elfs_dict = {}
elfs_by_values = {}

def get_all_elf():
    with open("input.txt", "r") as file:
        data = file.readlines()
        buffer = []
        for line in data :
            if line != '\n':
                buffer.append(int(line))
            else:
                elf = Elf(len(elfs_dict), buffer)
                elfs_dict[len(elfs_dict)] = elf
                buffer = []
        
    return 0


def find_max_elf():
    buffer_max_value = 0
    buffer_id = 0
    for id_elf in elfs_dict.keys():
        curr_elf = elfs_dict[id_elf]
        val = curr_elf.get_value_candys()
        if val > buffer_max_value:
            buffer_max_value = val
            buffer_id = id_elf

    return buffer_id, buffer_max_value


def create_sort_dict():
    for id_elf in elfs_dict.keys():
        curr_elf = elfs_dict[id_elf]
        elfs_by_values[id_elf] = curr_elf.get_value_candys()

    return 0

def get_top_three():
    curr_lst = list(elfs_by_values.values())
    curr_lst.sort()
    sub_lst = curr_lst[-3:]

    sum = 0
    for item in sub_lst:
        sum += item
    return sum




def main():
    get_all_elf()
    create_sort_dict()

    id, val = find_max_elf()

    top_three = get_top_three()
   

    print("Day 1 : Elf n°{} carry {} calories".format(id, val))
    print("Day 2 : The top three carry {} calories".format(top_three))


main()