"""
练习 25: 高阶函数
难度: 🟡 进阶
预计时间: 15分钟

高阶函数：接受函数作为参数或返回函数的函数
"""


def apply_function(func, value):
    """
    应用函数到值
    
    参数:
        func: 函数
        value: 值
    
    返回:
        函数应用结果
    
    示例:
        apply_function(lambda x: x * 2, 5) -> 10
    """
    return func(value)


def create_multiplier(factor: int):
    """
    创建乘法器函数（返回函数）
    
    参数:
        factor: 乘数
    
    返回:
        一个函数，该函数将输入乘以factor
    
    示例:
        double = create_multiplier(2)
        double(5) -> 10
    """
    return lambda x: x * factor


def compose(f, g):
    """
    函数组合：f(g(x))
    
    参数:
        f: 外层函数
        g: 内层函数
    
    返回:
        组合后的函数
    
    示例:
        add_one = lambda x: x + 1
        double = lambda x: x * 2
        composed = compose(double, add_one)
        composed(5) -> 12  # double(add_one(5)) = double(6) = 12
    """
    return lambda x: f(g(x))


def filter_with_predicate(items: list, predicate):
    """
    使用谓词函数过滤列表
    
    参数:
        items: 列表
        predicate: 谓词函数（返回True/False）
    
    返回:
        过滤后的列表
    
    示例:
        filter_with_predicate([1, 2, 3, 4], lambda x: x % 2 == 0) -> [2, 4]
    """
    # TODO: 使用列表推导式或filter函数
    return list(filter(predicate, items))


if __name__ == "__main__":
    print(apply_function(lambda x: x * 2, 5))
    double = create_multiplier(2)
    print(double(5))
    
    add_one = lambda x: x + 1
    double = lambda x: x * 2
    composed = compose(double, add_one)
    print(composed(5))
    
    print(filter_with_predicate([1, 2, 3, 4], lambda x: x % 2 == 0))

