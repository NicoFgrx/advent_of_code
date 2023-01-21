

class Elf:

    def __init__(self, id, candy):
        self.id = id
        self.candy = candy
        self.nb_candy = len(candy)
        self.max_value = 0
    
    
    def get_id(self):
        return self.id
    def get_nb_candy(self):
        return self.nb_candy
    def get_candy(self):
        return self.candy

    def get_value_candys(self):
        candys_lst = self.candy
        sum = 0
        for candy in candys_lst:
            sum += candy

        return sum
    
    def set_value_candys(self, val):
        self.max_value = val
        return 0
    