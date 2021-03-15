class Rectangle:
    width = 0
    height = 0
    
    def __init__(self, w, h):
        self.width = w
        self.height = h
    
    def __str__(self):
        return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) +")"

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
            i = (("*"*(self.width)+'\n')*self.height)
            return (i)
    
    def get_amount_inside (self, shape):
        Shape_Area = shape.get_area()
        Fitting_Area = self.get_area()
        i = 0
        while Fitting_Area>=Shape_Area:
            Fitting_Area = Fitting_Area-Shape_Area
            i=i+1
        return i 



class Square(Rectangle):

    def __init__(self, l):
        super(Rectangle, self).__init__()
        self.width = l
        self.height = l

    def __str__(self):
        return "Square(side=" + str(self.width) + ")"

    def set_side(self, l):
        self.set_width(l)
        self.set_height(l)

    def set_width(self, l):
        self.width = l

    def set_height(self, l):
        self.height = l
