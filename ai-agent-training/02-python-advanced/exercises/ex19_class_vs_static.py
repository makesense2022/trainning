"""
练习 19: 类方法vs静态方法
难度: 🟡 进阶
预计时间: 15分钟

目标：理解@classmethod和@staticmethod的区别
"""


class Calculator:
    """计算器类"""
    
    @staticmethod
    def add(a: float, b: float) -> float:
        """
        静态方法（不需要访问类或实例）
        
        参数:
            a: 第一个数
            b: 第二个数
        
        返回:
            和
        """
        return a + b
    
    @classmethod
    def create_from_string(cls, expression: str) -> 'Calculator':
        """
        类方法（可以访问类，用于替代构造函数）
        
        参数:
            expression: 表达式字符串（如"5+3"）
        
        返回:
            Calculator实例
        """
        # TODO: 解析表达式并创建实例
        parts = expression.split("+")
        if len(parts) == 2:
            a, b = float(parts[0]), float(parts[1])
            return cls(a, b)
        return cls(0, 0)
    
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b
    
    def calculate(self) -> float:
        """实例方法"""
        return self.a + self.b


if __name__ == "__main__":
    # 使用静态方法
    result = Calculator.add(5, 3)
    print(f"静态方法: {result}")
    
    # 使用类方法
    calc = Calculator.create_from_string("10+20")
    print(f"类方法创建: {calc.calculate()}")

