"""
练习 17: 抽象类
难度: 🟡 进阶
预计时间: 20分钟

目标：使用抽象基类定义接口
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """动物抽象基类"""
    
    def __init__(self, name: str):
        self.name = name
    
    @abstractmethod
    def speak(self) -> str:
        """说话（子类必须实现）"""
        pass
    
    def move(self) -> str:
        """移动（有默认实现）"""
        return f"{self.name}在移动"


class Dog(Animal):
    """狗类（实现抽象方法）"""
    
    def speak(self) -> str:
        """实现speak方法"""
        return f"{self.name}说：汪汪"


class Cat(Animal):
    """猫类（实现抽象方法）"""
    
    def speak(self) -> str:
        """实现speak方法"""
        return f"{self.name}说：喵喵"


if __name__ == "__main__":
    dog = Dog("旺财")
    print(dog.speak())
    print(dog.move())
    
    cat = Cat("咪咪")
    print(cat.speak())

