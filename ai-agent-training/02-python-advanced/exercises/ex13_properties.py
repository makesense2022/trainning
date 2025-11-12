"""
练习 13: @property装饰器
难度: 🟡 进阶
预计时间: 15分钟

目标：使用@property创建属性访问器
"""


class Temperature:
    """温度类（演示@property）"""
    
    def __init__(self, celsius: float):
        self._celsius = celsius
    
    @property
    def celsius(self) -> float:
        """获取摄氏度"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value: float):
        """设置摄氏度"""
        if value < -273.15:
            raise ValueError("温度不能低于绝对零度")
        self._celsius = value
    
    @property
    def fahrenheit(self) -> float:
        """获取华氏度（只读属性）"""
        return self._celsius * 9/5 + 32


class Circle:
    """圆类"""
    
    def __init__(self, radius: float):
        self._radius = radius
    
    @property
    def radius(self) -> float:
        """半径"""
        return self._radius
    
    @radius.setter
    def radius(self, value: float):
        """设置半径"""
        if value < 0:
            raise ValueError("半径不能为负")
        self._radius = value
    
    @property
    def area(self) -> float:
        """面积（只读，自动计算）"""
        import math
        return math.pi * self._radius ** 2
    
    @property
    def circumference(self) -> float:
        """周长（只读，自动计算）"""
        import math
        return 2 * math.pi * self._radius


if __name__ == "__main__":
    temp = Temperature(25)
    print(f"摄氏度: {temp.celsius}, 华氏度: {temp.fahrenheit}")
    
    circle = Circle(5)
    print(f"半径: {circle.radius}, 面积: {circle.area:.2f}")

