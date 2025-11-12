"""
练习 11: 类定义
难度: 🟢 基础
预计时间: 10分钟

对比学习：
JS:  class User { constructor(name) { this.name = name; } }
Python: class User: def __init__(self, name): self.name = name
"""


class User:
    """
    用户类
    
    属性:
        name: 姓名
        age: 年龄
    """
    
    def __init__(self, name: str, age: int = 0):
        """
        初始化用户
        
        参数:
            name: 姓名
            age: 年龄（默认0）
        """
        # TODO: 初始化属性
        pass
    
    def greet(self) -> str:
        """
        问候方法
        
        返回:
            问候语
        """
        # TODO: 返回问候语，如 "Hello, I'm {name}, {age} years old"
        pass
    
    def have_birthday(self):
        """
        过生日，年龄+1
        """
        # TODO: 年龄加1
        pass


class Calculator:
    """
    计算器类
    """
    
    def __init__(self):
        """初始化计算器"""
        self.history = []  # 计算历史
    
    def add(self, a: float, b: float) -> float:
        """
        加法
        
        参数:
            a: 第一个数
            b: 第二个数
        
        返回:
            结果
        """
        # TODO: 实现加法，并记录到history
        pass
    
    def get_history(self) -> list:
        """
        获取计算历史
        
        返回:
            历史记录列表
        """
        # TODO: 返回历史
        pass


if __name__ == "__main__":
    # 测试User类
    user = User("Alice", 25)
    print(user.greet())
    user.have_birthday()
    print(f"After birthday: {user.age}")
    
    # 测试Calculator类
    calc = Calculator()
    print(calc.add(5, 3))
    print(calc.get_history())

