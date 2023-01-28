input_file = "input.txt"

directions_lst = ['L', 'R', 'U', 'D'] # left, right, up, down
opposite_directions_dct = {'L':'R', 'R':'L', 'U':'D', 'D':'U'}
points_dct = {'head': None, 'tail': None}
points_tail_lst = []

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def go_left(self):
        self.x = self.x - 1

    def go_right(self):
        self.x = self.x + 1
    
    def go_up(self):
        self.y = self.y + 1

    def go_down(self):
        self.y = self.y - 1

    def go_diag_ul(self):
        self.go_up()
        self.go_left()
        
    def go_diag_ur(self):
        self.go_up()
        self.go_right()
        
    def go_diag_dl(self):
        self.go_down()
        self.go_left()

    def go_diag_dr(self):
        self.go_down()
        self.go_right()

    def move(self, direction, metric):
        if direction not in directions_lst:
            return "Error : direction misspelling", self.x, self.y

        tail = points_dct['tail']
       
        for step in range(metric):  
            if direction == 'L':
                self.go_left()
            elif direction == 'R':
                self.go_right()
            elif direction == 'U':
                self.go_up()
            elif direction == 'D':
                self.go_down()     

            # tail in touch ?            
            if self == tail:
                # print("Object moving is the tail")
                return 0
                     
            if not tail.is_contact(self.x, self.y):      
                if [tail.x, tail.y] not in points_tail_lst:                    
                    points_tail_lst.append([tail.x, tail.y]) # save last position    
                    # print(points_tail_lst)

                # else:
                #     print("DEBUG : Tail has already passed this way ")    
                
                tail.move(direction, 1)  
                
                # # disgusting move, but works
                tail.x = self.x
                tail.y = self.y 
                tail.move(opposite_directions_dct[direction], 1)
            # else:
            #     print("DEBUG : tail can touch the head ")

            print("DEBUG : head ({},{}), tail ({},{})".format(self.x, self.y, tail.x, tail.y))
            
        return "Moving...", self.x, self.y


    def is_contact(self, other_x, other_y):
        delta_x = abs(self.x - other_x)   
        delta_y = abs(self.y - other_y) 
        if delta_x == 0 and delta_y == 0: # covered
            return True
        elif delta_x == 1 and delta_y == 0: # upper or down
            return True
        elif delta_x == 0 and delta_y == 1: # left or right
            return True
        elif delta_x == 1 and delta_y == 1: # diag 
            return True
        else:
            return False

def first_part():
    
    with open(input_file, 'r') as file:

        head = points_dct['head']
        
        for line in file:
            direction , metric = line.split(' ')
            metric = int(metric)
            action, head_pos_x, head_pos_y = head.move(direction, metric)
            print(action)

        return len(points_tail_lst)

def second_part():
    with open(input_file, 'r') as file:
        pass

def display_map():
    max_x = 0
    max_y = 0

    min_x = 0
    min_y = 0
    for points in points_tail_lst:
        x, y = points           
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
        if x < min_x:
            min_x = x
        if y < min_y:
            min_y = y

    print("="*50)
    for y in range(max_y,min_y,-1):
        for x in range(min_x, max_x+1,1):
            if [x,y] == [0, 0]:
                print("s", end='')
                continue
            if [x, y] in points_tail_lst:
                print("x", end='')
                continue
            print(".", end='')
        print()
    
    print("="*50)




def main():

    head = Point(0, 0)
    tail = Point(0, 0)

    points_tail_lst.append([0,0])

    points_dct['head'] = head
    points_dct['tail'] = tail


    
    # Wrong guess : 6557 (to high)
    # New guess : 

    first_result = first_part()
    print("The first result is {}".format(first_result))

    display_map()

    second_result = second_part()
    print("The second result is {}".format(second_result))

main()