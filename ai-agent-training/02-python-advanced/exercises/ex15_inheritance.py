"""
练习 15: 继承
难度: 🟡 进阶
预计时间: 15分钟

目标：理解Python的类继承
"""


class Animal:
    """动物基类"""
    
    def __init__(self, name: str):
        self.name = name
    
    def speak(self) -> str:
        """说话（子类应该重写）"""
        return f"{self.name}发出声音"
    
    def move(self) -> str:
        """移动"""
        return f"{self.name}在移动"


class Dog(Animal):
    """狗类（继承Animal）"""
    
    def speak(self) -> str:
        """重写speak方法"""
        # TODO: 返回"汪汪"
        return f"{self.name}说：汪汪"
    
    def fetch(self) -> str:
        """捡球（Dog特有方法）"""
        return f"{self.name}去捡球了"


class Cat(Animal):
    """猫类（继承Animal）"""
    
    def speak(self) -> str:
        """重写speak方法"""
        # TODO: 返回"喵喵"
        return f"{self.name}说：喵喵"
    
    def climb(self) -> str:
        """爬树（Cat特有方法）"""
        return f"{self.name}在爬树"


if __name__ == "__main__":
    dog = Dog("旺财")
    print(dog.speak())
    print(dog.move())
    print(dog.fetch())
    
    cat = Cat("咪咪")
    print(cat.speak())
    print(cat.climb())

