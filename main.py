import abc
from math import tan, pi, sqrt, sin, cos, radians
import tkinter as tk


colors = [
    "black", "blue", "red", "green", "white"
]


class ConvexPolygon:
    fill_colour = "black"
    outline_colour = "black"
    scale = 1.0

    def __init__(self):
        print("Podaj kolor: ")
        val = input()
        self.fill_colour = val

        print("Kolor obramowania: ")
        val = input()
        self.outline_colour = val

        print("Podaj skale: ")
        val = input()
        self.scale = float(val)

    @abc.abstractmethod
    def area(self):
        pass

    @abc.abstractmethod
    def perimeter(self):
        pass

    @abc.abstractmethod
    def draw(self):
        pass

    def getColors(self):
        return (self.fill_colour, self.outline_colour)

    def shift(self, xy, v1v2):
        [x, y] = xy
        [v1, v2] = v1v2
        return [x + v1, y + v2]


class FloatDescriptor:

    def __init__(self, val=0.0, name='float value'):
        self.val = val
        self.name = name

    def __get__(self, obj, objtype):
        # print(f'Insert {self.name} and hit enter')
        return {"val": self.val, "name": self.name}

    def __set__(self, obj, val):
        print(f'Updated {self.name}')
        v = float(val)
        self.val = v

    def checkValue(self, value):
        if isinstance(val, float):
            self.val = val
        else:
            print("Something went wrong, try again")


class AngleDescriptor:
    val = 0.0

    def __init__(self, angle=0.0, name='angle value'):
        self.val = angle
        self.name = name

    def __get__(self, obj, objtype):
        # print(f'Insert {self.name} and hit enter')
        return {"val": self.val, "name": self.name}

    def __set__(self, obj, val):
        print(f'Updated {self.name}')
        v = float(val)
        self.val = v


class CoordDescriptor:
    x = 0
    y = 0
    name = "coord"

    def __init__(self, x=0, y=0, name='coordinate value'):
        self.x = x
        self.y = y
        self.name = name

    def __get__(self, obj, objtype):
        # print(f'Insert {self.name} and hit enter')
        return {"x": self.x, "y": self.y, "name": self.name}

    def __set__(self, obj, val):
        x = int(val["x"])
        self.x = x
        print(f'Updated {self.name}, x')

        y = int(val["y"])
        self.y = y
        print(f'Updated {self.name}, y')

    def toArray(self):
        return [self.x, self.y]

    def checkValue(self, value):
        if isinstance(val, int):
            self.val = val
        else:
            print("Something went wrong, try again")


class RegularPentagon(ConvexPolygon):
    length = FloatDescriptor(name="length")
    number = 5
    # number = FloatDescriptor(name="number")

    def __init__(self):
        super(RegularPentagon, self).__init__()
        length = input(f'Insert {self.length["name"]}: ')
        self.length = length

    def area(self):
        number = self.number
        return 0.25 * sqrt(number*(number+(2*sqrt(number)))) * (self.length["val"] ** 2)

    def perimeter(self):
        return self.number * self.length["val"]

    def draw(self, can):
        number = self.number
        a = self.length["val"]
        # beacuse we split triangle angle in two
        r = radians(360/(number * 2))
        b = a / (2 * sin(r))
        print(b)
        [centerX, centerY] = [0, 0]

        cords = []
        for i in range(number):
            # we get radian for whole triangle
            r = radians(360/number)
            x = centerX + b * cos(r * i)
            y = centerY + b * sin(r * i)
            [v1, v2] = [400, 400]
            [x, y] = self.shift([x, y], [v1, v2])
            cords.append(x)
            cords.append(y)

        can.create_polygon(cords, fill=self.fill_colour,
                           outline=self.outline_colour)


class RegularHexagon(ConvexPolygon):
    length = FloatDescriptor(name="length")
    number = 6

    def __init__(self):
        super(RegularHexagon, self).__init__()
        length = input(f'Insert {self.length["name"]}: ')
        self.length = length

    def area(self):
        length = self.length
        return ((3 * sqrt(3) * (length['val'] * length['val'])) / 2)

    def perimeter(self):
        return self.length['val'] * self.number

    def draw(self, can):
        number = self.number
        a = self.length["val"]
        # beacuse we split triangle angle in two
        r = radians(360/(number * 2))
        b = a / (2 * sin(r))
        print(b)
        [centerX, centerY] = [0, 0]

        cords = []
        for i in range(number):
            # we get radian for whole triangle
            r = radians(360/number)
            x = centerX + b * cos(r * i)
            y = centerY + b * sin(r * i)
            [v1, v2] = [400, 400]
            [x, y] = self.shift([x, y], [v1, v2])
            cords.append(x)
            cords.append(y)

        can.create_polygon(cords, fill=self.fill_colour,
                           outline=self.outline_colour)


class RegularOctagon(ConvexPolygon):
    length = FloatDescriptor(name="side a")
    number = 8

    def __init__(self):
        super(RegularOctagon, self).__init__()
        length = input(f'Insert {self.length["name"]}: ')
        self.length = length

    def area(self):
        length = self.length
        return ((3 * sqrt(3) * (length['val'] * length['val'])) / 2)

    def perimeter(self):
        return self.length['val'] * self.number

    def draw(self, can):
        number = self.number
        a = self.length["val"]
        # beacuse we split triangle angle in two
        r = radians(360/(number * 2))
        b = a / (2 * sin(r))
        print(b)
        [centerX, centerY] = [0, 0]

        cords = []
        for i in range(number):
            # we get radian for whole triangle
            r = radians(360/number)
            x = centerX + b * cos(r * i)
            y = centerY + b * sin(r * i)
            [v1, v2] = [400, 400]
            [x, y] = self.shift([x, y], [v1, v2])
            cords.append(x)
            cords.append(y)

        can.create_polygon(cords, fill=self.fill_colour,
                           outline=self.outline_colour)


class Triangle(ConvexPolygon):
    a = FloatDescriptor(name="side a")
    b = FloatDescriptor(name="side b")
    c = FloatDescriptor(name="side c")

    def __init__(self):
        super(Triangle, self).__init__()

        triangleT = self.__class__.__name__
        print("Just remember! Length of a and b, must be higher than c!!")
        a = input(f'Insert {self.a["name"]}: ')
        self.a = a

        if triangleT == "EquilateralTriangle":
            self.b = a
            self.c = a

        elif triangleT == "IsoscelesTriangle":
            b = input(f'Insert {self.b["name"]}: ')
            self.b = b
            self.c = b

        else:
            b = input(f'Insert {self.b["name"]}: ')
            self.b = b
            c = input(f'Insert {self.c["name"]}: ')
            self.c = c

    def area(self):
        a = self.a["val"]
        b = self.b["val"]
        c = self.c["val"]

        print("a: ", a, "b: ", b, "c: ", c)

        s = (a + b + c) / 2

        ar = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        return ar

    def perimeter(self):
        return self.a["val"] + self.b["val"] + self.c["val"]

    def draw(self, can):
        # from formula for path between two points, and having length,
        # we calculate y of second point in triangle
        # calculated value is 3 object in Quadratic_equation
        # and we go with delta and stuff

        # caclucate c
        # y2 = (self.area() * 2) / self.a["val"]
        # h = y2
        # [x1, y1] = [0, h]
        # [x2, y2] = [0, 0]
        # [x3, y3] = [self.c["val"], h]
        # wordC = (pow(self.a["val"], 2) - pow(x1, 2) -
        #          pow(y2, 2) + (2 * y2 * y1) - pow(y1, 2))

        # # calculate b
        # wordB = 2 * x1
        # wordA = 1

        # d = (wordB**2) - (4*wordA*wordC)
        # sol1 = (-wordB-sqrt(d))/(2*wordA)
        # sol2 = (-wordB+sqrt(d))/(2*wordA)

        # x2 = max([sol1, sol2])
        h = (self.area() * 2) / self.a["val"]

        v1 = (400 / self.scale) - (self.a['val'] / 2)
        v2 = (400 / self.scale) - (h / 2)

        [x1, y1] = self.shift([0, 0], [v1, v2])
        [x2, y2] = self.shift([self.a['val'], 0], [v1, v2])

        [x3, y3] = self.shift(
            [sqrt(self.b['val']**2 - h**2), h], [v1, v2])

        arr = [x1, y1, x2, y2, x3, y3]

        arr = list(map(lambda a: a * self.scale, arr))

        can.create_polygon(arr, fill=self.fill_colour,
                           outline=self.outline_colour)


class IsoscelesTriangle(Triangle):
    arm = FloatDescriptor(name="=arm")
    bottom = FloatDescriptor(name="bottom")

    def __init__(self):
        super(IsoscelesTriangle, self).__init__()


class EquilateralTriangle(Triangle):
    side = FloatDescriptor(name="side")

    def __init__(self):
        super(EquilateralTriangle, self).__init__()


class ConvexQuadrilateral(ConvexPolygon):
    a = CoordDescriptor(name="side a", x=0, y=0)
    b = CoordDescriptor(name="side b", x=0, y=0)
    c = CoordDescriptor(name="side c", x=0, y=0)
    d = CoordDescriptor(name="side d", x=0, y=0)
    xs = []
    xy = []

    def __init__(self):
        super(ConvexQuadrilateral, self).__init__()

        t = self.__class__.__name__
        if t == 'ConvexQuadrilateral':
            print("Okay it will be a hell of input, we need, 4 tuples, with x, and y")
            print("Remeber to provide x,y in clock wise way")
            x = input("x: ")
            y = input("y: ")
            self.a = {"x": x, "y": y}

            x = input("x: ")
            y = input("y: ")
            self.b = {"x": x, "y": y}

            x = input("x: ")
            y = input("y: ")
            self.c = {"x": x, "y": y}

            x = input("x: ")
            y = input("y: ")
            self.d = {"x": x, "y": y}

            self.xs = [self.a["x"], self.b["x"], self.c["x"], self.d["x"]]
            self.ys = [self.a["y"], self.b["y"], self.c["y"], self.d["y"]]

    def area(self):
     # Initialze area
        area = 0.0

        # Calculate value of shoelace formula
        xs = self.xs
        ys = self.ys
        n = 4
        j = n - 1
        print(xs, ys)
        for i in range(0, n):
            area += (xs[j] + xs[i]) * (ys[j] - ys[i])
            j = i   # j is previous vertex to i

        return abs(area / 2.0)

    def perimeter(self):

        summ = 0
        for i in range(4):
            _next = 0 if i == 3 else i + 1

            x1 = self.xs[i]
            x2 = self.xs[_next]

            y1 = self.ys[i]
            y2 = self.ys[_next]
            d1 = x2-x1
            d2 = y2-y1
            summ += sqrt(pow(d1, 2) + pow(d2, 2))
        return summ

    def findVector(self):
        # |AB|2|AB||AB|=|AC|2+|BC|2=|AC|2+|BC
        [x1, y1] = [self.a["x"] * self.scale, self.a["y"] * self.scale]
        [x2, y2] = [self.b["x"] * self.scale, self.b["y"] * self.scale]
        [x3, y3] = [self.c["x"] * self.scale, self.c["y"] * self.scale]
        [x4, y4] = [self.d["x"] * self.scale, self.d["y"] * self.scale]
        d1 = sqrt((x1-x3)**2 + (y1-y3)**2)
        d2 = sqrt((x2-x4)**2 + (y2-y4)**2)
        return [400 - (d1 / 2), 400 - (d2 / 2)]

    def draw(self, can):
        v = self.findVector()
        [x1, y1] = self.shift(
            [self.a["x"] * self.scale, self.a["y"] * self.scale], v)
        [x2, y2] = self.shift(
            [self.b["x"] * self.scale, self.b["y"] * self.scale], v)
        [x3, y3] = self.shift(
            [self.c["x"] * self.scale, self.c["y"] * self.scale], v)
        [x4, y4] = self.shift(
            [self.d["x"] * self.scale, self.d["y"] * self.scale], v)
        can.create_polygon([x1, y1, x2, y2, x3, y3, x4, y4], fill=self.fill_colour,
                           outline=self.outline_colour)


class Kite(ConvexQuadrilateral):
    a = FloatDescriptor(name="shorter side")
    b = FloatDescriptor(name="longest side")
    angle = AngleDescriptor(name="angle between two sides")

    def __init__(self):

        super(Kite, self).__init__()

        a = input(f'Insert {self.a["name"]}: ')
        self.a = a

        t = self.__class__.__name__
        if t == 'Rhombus' or t == 'Square':
            self.b = self.a['val']
        else:
            b = input(f'Insert {self.b["name"]}: ')
            self.b = b

        if t == 'Square':
            self.angle = 90.0
        else:
            angle = input(f'Insert {self.angle["name"]}: ')
            self.angle = angle

        print(self.a['val'], self.b['val'], self.angle['val'])

    def calcD1(self):
        # longest
        angle = self.angle['val']
        a = self.a['val']
        b = self.b['val']

        # law of cosinus
        # c2=a2+b2−2abcosγ
        # in kite diagonals cut angles in half so 2 of them - 180 is up angle

        r = radians(angle)
        return sqrt(pow(a, 2) + pow(b, 2) - 2 * a * b * cos(r))

    def calcD2(self):
        # shorter
        angle = self.angle['val']
        a = self.a['val']

        upAngle = 180 - angle
        r2 = radians(upAngle)
        return sqrt(pow(a, 2) + pow(a, 2) - 2 * a * a * cos(r2))

    def area(self):
        d1 = self.calcD1()
        d2 = self.calcD2()

        return (d1 * d2) / 2

    def perimeter(self):
        a = self.a['val']
        b = self.b['val']
        return a+a + b + b

    def findCenter(self):
        d1 = self.calcD1()
        d2 = self.calcD2()
        print("d1: ", d1, "d2: ", d2)
        return [(d2 / 2) * self.scale, (d1 / 2) * self.scale]

    def draw(self, can):
        shorterD = self.calcD2() * self.scale
        longerD = self.calcD1() * self.scale
        angle = self.angle['val']
        a = self.a['val'] * self.scale
        b = self.b['val'] * self.scale

        [s1, s2] = self.findCenter()
        v = [400 - s1,  400 - s2]
        alpha = (180 - angle) / 2

        r = radians(alpha)

        smallerPartOfLongestD = (shorterD / 2) / tan(r)

        [x1, y1] = self.shift([shorterD / 2, 0], v)
        [x2, y2] = self.shift([0, smallerPartOfLongestD], v)
        [x3, y3] = self.shift([shorterD / 2, longerD], v)

        [x4, y4] = self.shift([shorterD, smallerPartOfLongestD], v)

        arr = [x1, y1, x2, y2, x3, y3, x4, y4]

        can.create_polygon(arr, fill=self.fill_colour,
                           outline=self.outline_colour)


class Rhombus(Kite):
    def __init__(self):
        super(Rhombus, self).__init__()

    def draw(self, can):
        return super(Rhombus, self).draw(can)


class Square(Rhombus):

    def __init__(self):
        super(Square, self).__init__()


class Parallelogram(ConvexQuadrilateral):
    a = FloatDescriptor(name="basis")
    h = FloatDescriptor(name="height")
    angle = AngleDescriptor(name="angle between basis and left segment")

    def __init__(self):

        super(Parallelogram, self).__init__()

        a = input(f'Insert {self.a["name"]}: ')
        self.a = a

        h = input(f'Insert {self.h["name"]}: ')
        self.h = h

        angle = input(f'Insert {self.angle["name"]}: ')
        self.angle = angle

        print(self.a['val'], self.h['val'], self.angle['val'])

    def area(self):
        return self.a["val"] * self.h["val"]

    def calculateLeftSide(self):
        angle = self.angle['val']
        r = radians(angle)
        return self.h['val'] / sin(r)

    def perimeter(self):
        a = self.a['val']
        b = self.calculateLeftSide()
        return a + a + b + b        # basis of triangle

    def draw(self, can):
        a = self.a['val'] * self.scale
        b = self.calculateLeftSide() * self.scale

        h = self.h['val'] * self.scale
        c = sqrt(pow(b, 2) - pow(h, 2))
        v = [400 - (a / 2), 400 - (h / 2)]

        [x1, y1] = self.shift([0, h], v)
        [x2, y2] = self.shift([c, 0], v)
        [x3, y3] = self.shift([c + a, 0], v)
        [x4, y4] = self.shift([a, h], v)
        arr = [x1, y1, x2, y2, x3, y3, x4, y4]

        can.create_polygon(arr, fill=self.fill_colour,
                           outline=self.outline_colour)


class Main(tk.Frame):
    polygon = None

    def __init__(self,  master=None):
        print("Hi there! Pick number, and hit enter")
        print("This program will calculate area of this shape")
        print("and draw it! Take your time, enjoy!")

        print("1. Triangle")
        print("2. ConvexQuadrilateral")
        print("3. Pentagon")
        print("4. RegularHexagon")
        print("5. RegularOctagon")
        print("6. IsoscelesTriangle")
        print("7. EquilateralTriangle")
        print("8. Parallelogram")
        print("9. Kite")
        print("10.Rhombus")
        print("11.Square")

        self.mapNumberToPolygon()

        root = tk.Tk()
        c = tk.Canvas(root, width=800, height=800, bg="white")
        self.polygon.draw(c)
        c.pack()
        root.mainloop()

    def mapNumberToPolygon(self):

        try:
            self.value = input()
            value = int(self.value)
            polygon = {
                1: "Triangle",
                2: "ConvexQuadrilateral",
                3: "Pentagon",
                4: "RegularHexagon",
                5: "RegularOctagon",
                6: "IsoscelesTriangle",
                7: "EquilateralTriangle",
                8: "Parallelogram",
                9: "Kite",
                10: "Rhombus",
                11: "Square",
            }[value]
            print(f'Nice choice! You pick {polygon}')

        except KeyError:
            print("Ups, something went wrong, try again")
            self.mapNumberToPolygon()

        try:
            polygonObject = {
                1: lambda: Triangle(),
                2: lambda: ConvexQuadrilateral(),
                3: lambda: RegularPentagon(),
                4: lambda: RegularHexagon(),
                5: lambda: RegularOctagon(),
                6: lambda: IsoscelesTriangle(),
                7: lambda: EquilateralTriangle(),
                8: lambda: Parallelogram(),
                9: lambda: Kite(),
                10: lambda: Rhombus(),
                11: lambda: Square(),
            }[value]
            self.polygon = polygonObject()
            print("Area: ", self.polygon.area())
            print("Perimeter: ", self.polygon.perimeter())
        except KeyError:
            print("This thing is not implemented yet, try smt else")
            self.mapNumberToPolygon()


    # def mapPolygonTo
main = Main()
