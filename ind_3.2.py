#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod


class Number(ABC):
    """
    Абстрактный базовый класс для числа.
    """

    @abstractmethod
    def add(self, other):
        pass

    @abstractmethod
    def subtract(self, other):
        pass

    @abstractmethod
    def multiply(self, other):
        pass

    @abstractmethod
    def divide(self, other):
        pass


class Integer(Number):
    """
    Класс для представления целого числа.
    """

    def __init__(self, value):
        self.value = value

    def add(self, other):
        if isinstance(other, (Integer, Real)):
            return Integer(self.value + other.value)

    def subtract(self, other):
        if isinstance(other, (Integer, Real)):
            return Integer(self.value - other.value)

    def multiply(self, other):
        if isinstance(other, (Integer, Real)):
            return Integer(self.value * other.value)

    def divide(self, other):
        if isinstance(other, (Integer, Real)) and other.value != 0:
            return Real(self.value / other.value)
        else:
            raise ValueError("Division by zero is not allowed.")

    def display(self):
        print(f"Целое число: {self.value}")


class Real(Number):
    """
    Класс для представления действительного числа.
    """

    def __init__(self, value):
        self.value = value

    def add(self, other):
        if isinstance(other, (Integer, Real)):
            return Real(self.value + other.value)

    def subtract(self, other):
        if isinstance(other, (Integer, Real)):
            return Real(self.value - other.value)

    def multiply(self, other):
        if isinstance(other, (Integer, Real)):
            return Real(self.value * other.value)

    def divide(self, other):
        if isinstance(other, (Integer, Real)) and other.value != 0:
            return Real(self.value / other.value)
        else:
            raise ValueError("Division by zero is not allowed.")

    def display(self):
        print(f"Действительное число: {self.value}")


def demonstrate_virtual_call(number):
    """
    Функция для демонстрации работы с числами.
    """
    number.display()


if __name__ == "__main__":
    int_number = Integer(10)
    real_number = Real(5.5)

    result = int_number.add(real_number)
    result.display()

    result = int_number.subtract(real_number)
    result.display()

    result = int_number.multiply(real_number)
    result.display()

    result = int_number.divide(real_number)
    result.display()