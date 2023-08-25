from node import Elf

elfs_dict = {}

def get_all_efl():
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


def main():
    get_all_efl()

    id, val = find_max_elf()

    print("Elf n°{} carry {} calories".format(id, val))


main()