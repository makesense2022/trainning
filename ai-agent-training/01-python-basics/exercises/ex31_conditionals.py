"""
练习 31: if/elif/else
难度: 🟢 基础
预计时间: 5分钟

对比学习：
JS:  if (x > 0) { ... } else if (x < 0) { ... } else { ... }
Python: if x > 0: ... elif x < 0: ... else: ...

关键区别：
1. Python用elif（不是else if）
2. Python用冒号:和缩进（不是{}）
"""


def check_number(num: int) -> str:
    """
    检查数字的正负性
    
    参数:
        num: 整数
    
    返回:
        "positive" 如果 > 0
        "negative" 如果 < 0
        "zero" 如果 == 0
    """
    # TODO: 使用 if/elif/else 实现
    pass


def grade_score(score: int) -> str:
    """
    根据分数返回等级
    
    90-100: "A"
    80-89: "B"
    70-79: "C"
    60-69: "D"
    <60: "F"
    """
    # TODO: 实现等级判断
    pass


if __name__ == "__main__":
    print(check_number(5))
    print(check_number(-3))
    print(check_number(0))
    print(grade_score(95))

