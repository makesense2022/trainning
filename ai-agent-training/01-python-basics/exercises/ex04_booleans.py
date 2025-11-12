"""
练习 04: 布尔值和逻辑运算
难度: 🟢 基础
预计时间: 5分钟

对比学习：
JS:  true, false, &&, ||, !
Python: True, False, and, or, not

关键区别：
1. Python用True/False（首字母大写）
2. Python用and/or/not（不是&&/||/!）
3. Python的and/or返回实际值，不是布尔值
"""


def boolean_basics() -> dict:
    """
    返回布尔值基础信息
    
    返回:
        {
            "true_value": True,
            "false_value": False,
            "true_type": type(True),
            "false_type": type(False)
        }
    """
    # TODO: 实现
    pass


def logical_and(a: bool, b: bool) -> bool:
    """
    逻辑与运算
    
    JS: a && b
    Python: a and b
    
    参数:
        a: 第一个布尔值
        b: 第二个布尔值
    
    返回:
        a and b的结果
    """
    # TODO: 使用 and 实现
    pass


def logical_or(a: bool, b: bool) -> bool:
    """
    逻辑或运算
    
    JS: a || b
    Python: a or b
    
    参数:
        a: 第一个布尔值
        b: 第二个布尔值
    
    返回:
        a or b的结果
    """
    # TODO: 使用 or 实现
    pass


def logical_not(a: bool) -> bool:
    """
    逻辑非运算
    
    JS: !a
    Python: not a
    
    参数:
        a: 布尔值
    
    返回:
        not a的结果
    """
    # TODO: 使用 not 实现
    pass


def truthy_falsy(value) -> bool:
    """
    判断值是否为真值（truthy）
    
    Python的假值（falsy）：
    - False
    - None
    - 0 (数字零)
    - "" (空字符串)
    - [] (空列表)
    - {} (空字典)
    - set() (空集合)
    
    其他都是真值（truthy）
    
    参数:
        value: 任意值
    
    返回:
        如果是真值返回True，否则返回False
    """
    # TODO: 使用 bool() 转换
    pass


if __name__ == "__main__":
    print(boolean_basics())
    print(logical_and(True, False))
    print(logical_or(True, False))
    print(logical_not(True))
    print(truthy_falsy(""))
    print(truthy_falsy("hello"))

