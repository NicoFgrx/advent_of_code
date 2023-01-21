input_file = "input.txt"

all_files = dict()

total_space = 70000000

update_size = 30000000

   
def is_int(str):
    try:
        int(str)
        return True
    except:
        return False
    


def build_file_system():

    current_dir_lst = []


    with open(input_file, 'r') as file:
        data = file.readlines()
        
        for line in data:
            print("DEBUG : new line")
            print("DEBUG : "+line, end="")
            instruction = line.split(" ")
            if instruction[0] == '$':
                # is an instruction
                print("DEBUG : is an instruction")
                
                if instruction[1] == 'cd':
                    print("DEBUG : is a cd")
                    if instruction[2].strip() == '..':
                        print("DEBUG : return back parent dir")
                        current_dir_lst.pop()
                    else:
                        current_dir = instruction[2].strip() 
                        print("DEBUG : {}".format(current_dir))
                        current_dir_lst.append(current_dir)
                        
                else:
                    print("DEBUG : is a ls")
                    path = '/'.join(current_dir_lst)
                    if not path in all_files.keys():
                        all_files[path] = 0

            elif instruction[0] == "dir":
                # is a dir
                print("DEBUG : is a dir")
            elif is_int(instruction[0]):
                print("DEBUG : is a file")
                print("DEBUG : path = {}".format(path))

                for idx in range(len(current_dir_lst)):
                    

                    sub_dir_lst = current_dir_lst[:len(current_dir_lst)-idx]
                    print("DEBUG : current_dir_lst = {}".format(current_dir_lst))
                    print("DEBUG : idx = {}".format(idx))
                    print("DEBUG : sub_dir_lst =  {}".format(sub_dir_lst))
                    sub_dir = "/".join(sub_dir_lst)
                    print("DEBUG = " + sub_dir)
                    all_files[sub_dir] = all_files[sub_dir]+int(instruction[0])


    return 0

def first_part():
    # print(all_files)
    result = 0
    for directory in all_files:
        size =  all_files[directory]
        if size < 100000:
            result += size

    return result

def second_part():
    total_space_used = all_files['/']
    total_space_free = total_space - total_space_used

    total_space_need = update_size - total_space_free

    print(total_space_need)

    for value in sorted(all_files.values()):
        if value > total_space_need:
            return value

def main():
    build_file_system()


    first_result = first_part()
    print("The first result is {}".format(first_result))

    second_result = second_part()
    print("The second result is {}".format(second_result))


    
    
    return 0

main()