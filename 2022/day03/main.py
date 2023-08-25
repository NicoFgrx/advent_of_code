input_file = 'input.txt'

def first_part():
    with open(input_file, 'r') as file:
        data = file.readlines()
        
        common = list()
        for backpack in data:
            container1 = backpack[:len(backpack)//2]
            container2 = backpack[len(backpack)//2:]

            for carac in container1:
                if carac in container2:
                    common.append(carac)
                    break
        
            total = 0
            for letter in common:
                if letter.islower():
                    total += ord(letter)-96
                elif letter.isupper():
                    total += ord(letter)-38               


    return total


def second_part():
    with open(input_file, 'r') as file:
        data = file.readlines()
        cpt = 0
        group = list()
        common = list()
        for backpack in data:
            print(backpack)
            if len(group) < 3:
                group.append(backpack)
                
                if len(group) == 3:
                    for carac in group[0]:                    
                        if carac in group[1] and carac in group[2]:
                            print(carac)
                            common.append(carac)
                            group = list()
                            break

        total = 0
        for letter in common:
            if letter.islower():
                total += ord(letter)-96
            elif letter.isupper():
                total += ord(letter)-38    
           
 
    return total


def main():
    first_result = first_part()
    print("The first result is {}".format(first_result))


    second_result = second_part()
    print("The second result is {}".format(second_result))



main()