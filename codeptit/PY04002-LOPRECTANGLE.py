class Rectangle:
    def __init__(self, width, height, _color):
        self.width = width
        self.height = height
        self._color = _color
    def perimeter(self):
        return (self.width + self.height) * 2
    def area(self):
        return self.width * self.height
    def color(self):
        return self._color.capitalize()
    
arr = input().split()
if int(arr[0]) > 0 and int(arr[1]) > 0:
    r = Rectangle(int(arr[0]), int(arr[1]), str(arr[2]))
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
else:
    print("INVALID")