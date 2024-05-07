#!/usr/bin/python3
""" this is for square class """


class Square():
    """ class:square """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ class init """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ clac the square area() """
        return self.width * self.height

    def permiter_of_my_square(self):
        """ clac the square permiter() """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ print the result """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """ class obj """
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
