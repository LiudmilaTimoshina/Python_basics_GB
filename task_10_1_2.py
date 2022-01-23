l1 = [[1,2,3],[4,5,6],[7,8,9]]
l2 = [[10,11,12],[13,14,15],[16,17,18]]



class Matrix:
    def __init__(self,args):
        self.args = args

    def __str__(self):
        return '\n'.join(str(i) for i in self.args)

    def __add__(self, other):
        return Matrix([[a + b for a, b in zip(my_row, other_row)]
                       for my_row, other_row in zip(self.args, other.args)])

obj1 = Matrix(l1)
print(obj1, '\n')

obj2 = Matrix(l2)
print(obj2, '\n')

obj3 = obj1 + obj2
print(obj3)