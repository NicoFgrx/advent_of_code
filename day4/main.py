input_file = 'input.txt'



def first_part():
    with open(input_file, 'r') as file:
        data = file.readlines()
        total = 0
        for sections in data:
            elf1_indexes, elf2_indexes = sections.split(',')
            elf1_start, elf1_end = elf1_indexes.split('-')
            elf2_start, elf2_end = elf2_indexes.split('-')

            elf1_start = int(elf1_start)
            elf1_end = int(elf1_end)
            elf2_start = int(elf2_start)
            elf2_end = int(elf2_end)

            if elf1_start >= elf2_start and elf1_end <= elf2_end :
                total +=1
            elif elf2_start >= elf1_start and elf2_end <= elf1_end:
                total +=1

        
 
    return total

def second_part():
    with open(input_file, 'r') as file:

        data = file.readlines()
        total = 0
        for sections in data:
            elf1_indexes, elf2_indexes = sections.split(',')
            elf1_start, elf1_end = elf1_indexes.split('-')
            elf2_start, elf2_end = elf2_indexes.split('-')

            elf1_start = int(elf1_start)
            elf1_end = int(elf1_end)
            elf2_start = int(elf2_start)
            elf2_end = int(elf2_end)

            if elf1_start <= elf2_start and elf2_start <= elf1_end:
                total += 1
            elif elf1_start <= elf2_end and elf2_end <= elf1_end:
                total += 1
            elif elf2_start <= elf1_start and elf1_start <= elf2_end:
                total += 1
            elif elf2_start <= elf1_end and elf1_end <= elf2_end:
                total += 1


    return total

def main():
    first_result = first_part()
    print("The first result is {}".format(first_result))


    second_result = second_part()
    print("The second result is {}".format(second_result))



main()