"""
练习 30: 函数式编程
难度: 🔴 挑战
预计时间: 20分钟

函数式编程：使用map、filter、reduce等函数
"""

from functools import reduce


def map_example(numbers: list) -> list:
    """
    使用map对列表元素平方
    
    JS: numbers.map(x => x * x)
    Python: list(map(lambda x: x * x, numbers))
    
    参数:
        numbers: 数字列表
    
    返回:
        平方后的列表
    """
    # TODO: 使用map实现
    return list(map(lambda x: x * x, numbers))


def filter_example(numbers: list) -> list:
    """
    使用filter过滤偶数
    
    JS: numbers.filter(x => x % 2 === 0)
    Python: list(filter(lambda x: x % 2 == 0, numbers))
    
    参数:
        numbers: 数字列表
    
    返回:
        偶数列表
    """
    # TODO: 使用filter实现
    return list(filter(lambda x: x % 2 == 0, numbers))


def reduce_example(numbers: list) -> int:
    """
    使用reduce计算列表元素的和
    
    JS: numbers.reduce((a, b) => a + b, 0)
    Python: reduce(lambda a, b: a + b, numbers, 0)
    
    参数:
        numbers: 数字列表
    
    返回:
        所有元素的和
    """
    # TODO: 使用reduce实现
    return reduce(lambda a, b: a + b, numbers, 0)


def compose_functions(*funcs):
    """
    组合多个函数
    
    参数:
        *funcs: 多个函数
    
    返回:
        组合后的函数
    
    示例:
        add_one = lambda x: x + 1
        double = lambda x: x * 2
        composed = compose_functions(double, add_one)
        composed(5) -> 12  # double(add_one(5))
    """
    # TODO: 使用reduce组合函数
    def composed(x):
        return reduce(lambda acc, f: f(acc), reversed(funcs), x)
    return composed


def pipeline(data, *funcs):
    """
    数据管道：依次应用多个函数
    
    参数:
        data: 初始数据
        *funcs: 函数列表
    
    返回:
        处理后的数据
    
    示例:
        pipeline([1, 2, 3, 4],
                 lambda x: filter(lambda y: y % 2 == 0, x),
                 lambda x: map(lambda y: y * 2, x),
                 list) -> [4, 8]
    """
    # TODO: 依次应用函数
    result = data
    for func in funcs:
        result = func(result)
    return result


if __name__ == "__main__":
    print(map_example([1, 2, 3, 4]))
    print(filter_example([1, 2, 3, 4, 5, 6]))
    print(reduce_example([1, 2, 3, 4, 5]))
    
    add_one = lambda x: x + 1
    double = lambda x: x * 2
    composed = compose_functions(double, add_one)
    print(composed(5))
    
    result = pipeline([1, 2, 3, 4],
                      lambda x: list(filter(lambda y: y % 2 == 0, x)),
                      lambda x: list(map(lambda y: y * 2, x)))
    print(result)

