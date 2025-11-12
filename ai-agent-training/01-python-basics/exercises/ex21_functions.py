"""
练习 21: 函数定义
难度: 🟢 基础
预计时间: 5分钟

对比学习：
JS:  function add(a, b) { return a + b; }
Python: def add(a, b): return a + b

关键区别：
1. Python用def定义函数
2. Python用缩进表示代码块（不是{}）
3. Python可以有类型注解（可选）
"""


def simple_function(x: int) -> int:
    """
    简单函数：返回x的平方
    
    参数:
        x: 整数
    
    返回:
        x的平方
    """
    # TODO: 实现函数
    pass


def function_with_default(x: int, multiplier: int = 2) -> int:
    """
    带默认参数的函数
    
    JS: function multiply(x, multiplier = 2) { return x * multiplier; }
    Python: def multiply(x, multiplier=2): return x * multiplier
    
    参数:
        x: 数字
        multiplier: 乘数（默认2）
    
    返回:
        x * multiplier
    """
    # TODO: 实现带默认参数的函数
    pass


def function_docstring() -> str:
    """
    这是一个有文档字符串的函数
    
    Python的文档字符串（docstring）：
    - 用三引号 """...""" 包裹
    - 描述函数的功能、参数、返回值
    - 可以通过 __doc__ 属性访问
    
    返回:
        "This function has a docstring"
    """
    # TODO: 返回字符串
    pass


if __name__ == "__main__":
    print(simple_function(5))
    print(function_with_default(5))
    print(function_with_default(5, 3))
    print(function_docstring())
    print(function_docstring.__doc__)

