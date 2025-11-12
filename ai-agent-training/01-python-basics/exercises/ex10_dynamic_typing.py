"""
练习 10: 动态类型陷阱
难度: 🟡 进阶
预计时间: 10分钟

Python是动态类型语言，这带来灵活性，但也可能隐藏bug
"""


def add_numbers(a, b):
    """
    动态类型函数（没有类型注解）
    
    问题：如果传入字符串会怎样？
    
    参数:
        a: 任意类型
        b: 任意类型
    
    返回:
        相加结果
    """
    # TODO: 实现加法，但考虑类型检查
    return a + b


def safe_add(a, b):
    """
    安全的加法（带类型检查）
    
    参数:
        a: 数字
        b: 数字
    
    返回:
        相加结果，如果类型错误返回None
    """
    # TODO: 检查类型，只允许数字相加
    pass


def type_coercion_demo():
    """
    演示类型强制转换的陷阱
    
    返回:
        演示结果的字典
    """
    # TODO: 演示以下情况
    # 1. "5" + 3 会怎样？
    # 2. "5" * 3 会怎样？
    # 3. True + 1 会怎样？
    pass


if __name__ == "__main__":
    print(add_numbers(5, 3))  # 8
    print(add_numbers("5", "3"))  # "53" (字符串拼接)
    # print(add_numbers("5", 3))  # 会报错！
    
    print(safe_add(5, 3))
    print(safe_add("5", 3))  # 应该返回None

