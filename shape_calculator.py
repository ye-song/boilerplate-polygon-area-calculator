class Rectangle:
    width = 0
    height = 0

    def __init__(self, w, h):
        self.width = w
        self.height = h

    def set_width(self, w):
        self.width = w
    
    def set_height(self, h):
        self.height = h

    def get_area (self):
        self.area = self.width * self.height
        return self.area
    
    def get_perimeter (self):
        self.perimeter = 2 * (self.width + self.height)
        return self.perimeter

    def get_diagonal (self):
        self.diagonal = ((self.width**2 + self.height**2)**0.5)
        return self.diagonal

    def get_picture (self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            for i in range (self.height + 1):
                return ("*" * (self.width + 1))
    
    #def get_amount_inside (self):


class Square(Rectangle):

    def __init__(self, l):
        super().__init__(l, l)

    def set_side(self, l):
        self.set_width(l)
        self.set_height(l)

    def set_width(self, l):
        self.width = l

    def set_height(self, l):
        self.height = l
