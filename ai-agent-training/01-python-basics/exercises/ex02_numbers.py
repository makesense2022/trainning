"""
练习 02: 数字类型和运算
难度: 🟢 基础
预计时间: 5分钟

对比学习：
JS:  let x = 10; let y = 3.14; let z = x + y;
Python: x = 10; y = 3.14; z = x + y

关键区别：
1. Python有int（任意精度）和float（双精度）
2. Python的整数除法用 //，普通除法 / 总是返回float
3. Python支持 ** 幂运算（JS用Math.pow）
"""


def add_numbers(a: int, b: int) -> int:
    """
    两数相加
    
    参数:
        a: 第一个整数
        b: 第二个整数
    
    返回:
        两数之和
    
    示例:
        add_numbers(5, 3) -> 8
    """
    return a + b


def divide_numbers(a: float, b: float) -> float:
    """
    两数相除（普通除法，返回float）
    
    JS: a / b
    Python: a / b (总是返回float，即使能整除)
    
    参数:
        a: 被除数
        b: 除数
    
    返回:
        除法结果（float类型）
    
    示例:
        divide_numbers(10, 3) -> 3.333...
        divide_numbers(10, 2) -> 5.0 (注意是float!)
    """
    return a / b


def integer_divide(a: int, b: int) -> int:
    """
    整数除法（向下取整）
    
    JS: Math.floor(a / b)
    Python: a // b
    
    参数:
        a: 被除数
        b: 除数
    
    返回:
        整数除法结果
    
    示例:
        integer_divide(10, 3) -> 3
        integer_divide(10, 2) -> 5
    """
    return a // b


def power(base: int, exponent: int) -> int:
    """
    幂运算
    
    JS: Math.pow(base, exponent)
    Python: base ** exponent
    
    参数:
        base: 底数
        exponent: 指数
    
    返回:
        base的exponent次方
    
    示例:
        power(2, 3) -> 8
        power(5, 2) -> 25
    """
    return base ** exponent


def modulo(a: int, b: int) -> int:
    """
    取模运算（求余数）
    
    JS: a % b
    Python: a % b (相同)
    
    参数:
        a: 被除数
        b: 除数
    
    返回:
        余数
    
    示例:
        modulo(10, 3) -> 1
        modulo(10, 2) -> 0
    """
    return a % b


def round_number(num: float, decimals: int = 0) -> float:
    """
    四舍五入
    
    JS: Math.round(num)
    Python: round(num, decimals)
    
    参数:
        num: 要四舍五入的数字
        decimals: 保留小数位数（默认0）
    
    返回:
        四舍五入后的数字
    
    示例:
        round_number(3.14159) -> 3.0
        round_number(3.14159, 2) -> 3.14
    """
    return round(num, decimals)


if __name__ == "__main__":
    print("测试 add_numbers:", add_numbers(5, 3))
    print("测试 divide_numbers:", divide_numbers(10, 3))
    print("测试 integer_divide:", integer_divide(10, 3))
    print("测试 power:", power(2, 3))
    print("测试 modulo:", modulo(10, 3))
    print("测试 round_number:", round_number(3.14159, 2))

