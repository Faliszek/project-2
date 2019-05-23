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


class Triangle(ConvexPolygon):
    a = FloatDescriptor(name="side a")
    b = FloatDescriptor(name="side b")
    c = FloatDescriptor(name="side c")

    def __init__(self):
        super(Triangle, self).__init__()
        a = input(f'Insert {self.a["name"]}: ')
        self.a = a
        b = input(f'Insert {self.b["name"]}: ')
        self.b = b

        c = input(f'Insert {self.c["name"]}: ')
        self.c = c

    def area(self):
        a = self.a["val"]
        b = self.b["val"]
        c = self.c["val"]
        s = (a+b+c)/2
        ar = math.sqrt(s*(s-a)*(s-b)*(s-c))
        return ar

    def perimeter(self):
        return self.a["val"] + self.b["val"] + self.c["val"]

    def draw(self):
        pass

        # class ConvexQuadrilateral(ConvexPolygon):

        # class RegularPentagon(ConvexPolygon):

        # class RegularHexagonorazRegularOctagon(ConvexPolygon):

        # class IsoscelesTriangle:

        # class EquilateralTriangle:

        # class Parallelogram:

        # class Kite:

        # class Rhombus:


class Square(ConvexPolygon):
    a = FloatDescriptor(name="side a")

    def __init__(self):
        super(Square, self).__init__()
        a = input(f'Insert {self.a["name"]}: ')
        self.a = a

    def area(self):
        a = self.a["val"]
        return a * a

    def perimeter(self):
        return self.a["val"] * 4

    def draw(self):
        pass


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

class ConvexQuadrilateral(ConvexPolygon):
    length = FloatDescriptor(name="length")
    number = FloatDescriptor(name="number")

    def __init__(self):
        super(ConvexQuadrilateral, self).__init__()
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
                # 4: "RegularHexagon",
                # 5: "RegularOctagon",
                # 6: "IsoscelesTriangle",
                # 7: "EquilateralTriangle",
                # 8: "Parallelogram",
                # 9: "Kite",
                # 10: "Rhombus",
                11: lambda _a: Square(),
            }[value]
            print(polygonObject(unit).area())

        except KeyError:
            print("This thing is not implemented yet, try smt else")
            self.mapNumberToPolygon()

    # def mapPolygonTo
main = Main()
