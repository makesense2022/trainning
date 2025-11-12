"""
练习 18: @dataclass
难度: 🟡 进阶
预计时间: 15分钟

目标：使用@dataclass简化类定义
"""

from dataclasses import dataclass, field
from typing import List


@dataclass
class Point:
    """点类（使用@dataclass）"""
    x: float
    y: float
    
    def distance_from_origin(self) -> float:
        """到原点的距离"""
        import math
        return math.sqrt(self.x**2 + self.y**2)


@dataclass
class User:
    """用户类"""
    name: str
    age: int
    email: str = ""  # 默认值
    tags: List[str] = field(default_factory=list)  # 可变默认值


@dataclass(frozen=True)
class ImmutablePoint:
    """不可变点类"""
    x: float
    y: float


if __name__ == "__main__":
    point = Point(3, 4)
    print(f"点: {point}, 距离: {point.distance_from_origin()}")
    
    user = User("Alice", 25, "alice@example.com")
    print(user)

