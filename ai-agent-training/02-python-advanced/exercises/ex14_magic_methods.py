"""
练习 14: 魔术方法
难度: 🟡 进阶
预计时间: 20分钟

目标：理解和使用Python的魔术方法
"""


class Vector:
    """向量类（演示魔术方法）"""
    
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
    def __str__(self) -> str:
        """字符串表示（用户友好）"""
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self) -> str:
        """对象表示（开发者友好）"""
        return f"Vector({self.x}, {self.y})"
    
    def __add__(self, other: 'Vector') -> 'Vector':
        """向量加法"""
        # TODO: 实现向量加法
        return Vector(self.x + other.x, self.y + other.y)
    
    def __mul__(self, scalar: float) -> 'Vector':
        """向量数乘"""
        # TODO: 实现数乘
        return Vector(self.x * scalar, self.y * scalar)
    
    def __eq__(self, other: 'Vector') -> bool:
        """相等比较"""
        # TODO: 实现相等比较
        return self.x == other.x and self.y == other.y
    
    def __len__(self) -> int:
        """长度（向量模）"""
        import math
        return int(math.sqrt(self.x**2 + self.y**2))


if __name__ == "__main__":
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    print(v1 + v2)  # Vector(4, 6)
    print(v1 * 2)   # Vector(2, 4)
    print(v1 == v2)  # False

