
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Triad:
    """
    Базовый класс, представляющий тройку чисел.
    """
    def __init__(self, a=0, b=0, c=0):
        self.a = a
        self.b = b
        self.c = c

    def add(self, number):
        self.a += number
        self.b += number
        self.c += number

    def multiply(self, number):
        self.a *= number
        self.b *= number
        self.c *= number

    def equals(self, other):
        return self.a == other.a and self.b == other.b and self.c == other.c

    def display(self):
        print(f"Тройка чисел: {self.a}, {self.b}, {self.c}")

class Vector3D(Triad):
    """
    Производный класс для представления трехмерного вектора.
    """
    def add_vector(self, other):
        self.a += other.a
        self.b += other.b
        self.c += other.c

    def dot_product(self, other):
        return self.a * other.a + self.b * other.b + self.c * other.c

    def display(self):
        print(f"Вектор: ({self.a}, {self.b}, {self.c})")

if __name__ == '__main__':
    triad1 = Triad(1, 2, 3)
    triad2 = Triad(4, 5, 6)

    triad1.display()
    triad1.add(10)
    triad1.display()
    triad1.multiply(2)
    triad1.display()
    print(f"Равенство triad1 и triad2: {triad1.equals(triad2)}")

    vector1 = Vector3D(1, 2, 3)
    vector2 = Vector3D(4, 5, 6)

    vector1.display()
    vector1.add_vector(vector2)
    print("После сложения векторов:")
    vector1.display()

    print(f"Скалярное произведение vector1 и vector2: {vector1.dot_product(vector2)}")