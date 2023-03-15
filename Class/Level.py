class Level:

    def __init__(self, field: list):
        self.field = field
        self.field_dictionary = self.create_dic()

    def create_dic(self):
        dic = {}
        for layer in range(len(self.field)):
            for tile in range(len(self.field[layer])):
                if self.field[layer][tile] != ' ':
                    pos = (tile * 16, layer * 16)
                    dic[pos] = self.field[layer][tile]
        return dic
