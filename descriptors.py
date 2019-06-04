
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
