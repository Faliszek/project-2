import abc
import math


colors = [
    "black", "blue", "red", "green", "white"
]


class ConvexPolygon:
    fill_colour = "black"
    outline_colour = "black"

    def __init__(self):
        print("Podaj kolor: ")
        val = input()
        self.fill_colour = val

        print("Kolor obramowania: ")
        val = input()
        self.outline_colour = val

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

    def checkValue(self, value):
        if isinstance(val, int):
            self.val = val
        else:
            print("Something went wrong, try again")


class RegularPentagon(ConvexPolygon):
    length = FloatDescriptor(name="length")
    number = FloatDescriptor(name="number")

    def __init__(self):
        super(RegularPentagon, self).__init__()
        length = input(f'Insert {self.length["name"]}: ')
        self.length = length

        number = input(f'Insert {self.number["name"]}: ')
        self.number = number

    def area(self):
        number = self.number["val"]
        length = self.length["val"]
        return (number * length ** 2)/(4 * math.tan(math.pi/number))

    def perimeter(self):
        return self.length["val"] * self.length["val"]

    def draw(self):
        pass


class RegularHexagon(ConvexPolygon):
    a = FloatDescriptor(name="side a")

    def __init__(self):
        super(RegularHexagon, self).__init__()
        a = input(f'Insert {self.a["name"]}: ')
        self.a = a

    def area(self):
        a = self.a
        return ((3 * math.sqrt(3) * (a['val'] * a['val'])) / 2)

    def perimeter(self):
        return self.a['val'] * 5

    def draw(self):
        pass


class RegularOctagon(ConvexPolygon):
    a = FloatDescriptor(name="side a")

    def __init__(self):
        super(RegularOctagon, self).__init__()
        a = input(f'Insert {self.a["name"]}: ')
        self.a = a

    def area(self):
        a = self.a["val"]
        return (2 * (1 + (math.sqrt(2))) * a * a)

    def perimeter(self):
        return self.a["val"] * 6

    def draw(self):
        pass


class Triangle(ConvexPolygon):
    a = FloatDescriptor(name="side a")
    b = FloatDescriptor(name="side b")
    c = FloatDescriptor(name="side c")

    def __init__(self):
        super(Triangle, self).__init__()

        triangleT = self.__class__.__name__
        print(triangleT)
        a = input(f'Insert {self.a["name"]}: ')
        self.a = a

        if triangleT == "EquilateralTriangle":
            self.b = a
            self.c = a

        elif triangleT == "IsoscelesTriangle":
            self.b = a
            c = input(f'Insert {self.c["name"]}: ')
            self.c = c

        else:
            b = input(f'Insert {self.b["name"]}: ')
            self.b = b
            c = input(f'Insert {self.c["name"]}: ')
            self.c = c

    def area(self):
        a = self.a["val"]
        b = self.b["val"]
        c = self.c["val"]

        s = (a + b + c) / 2

        ar = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        return ar

    def perimeter(self):
        return self.a["val"] + self.b["val"] + self.c["val"]

    def draw(self):
        pass


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
        # b = input(f'Insert {self.b["name"]}: ')
        # self.b = b

        # c = input(f'Insert {self.c["name"]}: ')
        # self.c = c

        # d = input(f'Insert {self.d["name"]}: ')
        # self.d = d

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
            summ += math.sqrt(math.pow(d1, 2) + math.pow(d2, 2))
        return summ

    def draw(self):
        pass


class Kite(ConvexQuadrilateral):
    def __init__(self):
        t = self.__class__.__name__
        if t == 'Kite':
            print("Example values: [3,6], [6,4], [3,0], [0,4]")

        super(Kite, self).__init__()


class Parallelogram(ConvexQuadrilateral):
    def __init__(self):
        t = self.__class__.__name__
        if t == 'Parallelogram':
            print("Example values: [0,0], [2,3], [8,3], [6,0]")

        super(Parallelogram, self).__init__()


class Rhombus(Parallelogram):
    def __init__(self):
        t = self.__class__.__name__
        if t == 'Rhombus':
            print("Example values: [0,3], [2,6], [4,3], [2,0]")

        super(Rhombus, self).__init__()


class Square(Rhombus):

    def __init__(self):
        print("Example values: [0,0], [9,0], [9,9], [0,9]")
        super(Square, self).__init__()


class Main:
    def __init__(self):
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
            unit = "_"
            polygonObject = {
                1: lambda _a: Triangle(),
                2: lambda _a: ConvexQuadrilateral(),
                3: lambda _a: RegularPentagon(),
                4: lambda _a: RegularHexagon(),
                5: lambda _a: RegularOctagon(),
                6: lambda _a: IsoscelesTriangle(),
                7: lambda _a: EquilateralTriangle(),

                8: lambda _a: Parallelogram(),
                9: lambda _a: Kite(),
                10: lambda _a: Rhombus(),
                11: lambda _a: Square(),
            }[value]
            print(polygonObject(unit).perimeter())

        except KeyError:
            print("This thing is not implemented yet, try smt else")
            self.mapNumberToPolygon()


    # def mapPolygonTo
main = Main()


# Uncomment below to take inputs from the user
# a = float(input('Enter first side: '))
# b = float(input('Enter second side: '))
# c = float(input('Enter third side: '))

# calculate the semi-perimeter
