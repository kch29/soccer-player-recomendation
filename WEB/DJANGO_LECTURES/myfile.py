from urllib.parse import uses_params


class agent():
    
    origin = "usa"
    
    def __init__(self,code_name, height, weight):
        self.code_name=code_name
        self.height=height
        self.weight=weight
    
    def call(self):
        return self.code_name
# x=agent("jose", 6.8, 75)
# print(x.height)