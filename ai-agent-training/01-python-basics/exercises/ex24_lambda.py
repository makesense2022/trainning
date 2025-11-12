"""
练习 24: Lambda表达式
难度: 🟢 基础
预计时间: 10分钟

对比学习：
JS:  const add = (a, b) => a + b;
Python: add = lambda a, b: a + b

Lambda是匿名函数，适合简单的一行函数
"""


def create_lambda_add() -> callable:
    """
    创建lambda函数实现加法
    
    返回:
        lambda函数: (a, b) -> a + b
    """
    return lambda a, b: a + b


def use_lambda_with_map(numbers: list) -> list:
    """
    使用lambda和map对列表元素平方
    
    JS: numbers.map(x => x * x)
    Python: list(map(lambda x: x * x, numbers))
    
    参数:
        numbers: [1, 2, 3, 4]
    
    返回:
        [1, 4, 9, 16]
    """
    # TODO: 使用lambda和map
    pass


def use_lambda_with_filter(numbers: list) -> list:
    """
    使用lambda和filter过滤偶数
    
    JS: numbers.filter(x => x % 2 === 0)
    Python: list(filter(lambda x: x % 2 == 0, numbers))
    
    参数:
        numbers: [1, 2, 3, 4, 5, 6]
    
    返回:
        [2, 4, 6]
    """
    # TODO: 使用lambda和filter
    pass


def use_lambda_with_sorted(items: list) -> list:
    """
    使用lambda和sorted按长度排序
    
    参数:
        items: ["apple", "pie", "banana"]
    
    返回:
        ["pie", "apple", "banana"] (按长度排序)
    """
    return sorted(items, key=lambda x: len(x))


if __name__ == "__main__":
    add = create_lambda_add()
    print(add(5, 3))
    print(use_lambda_with_map([1, 2, 3, 4]))
    print(use_lambda_with_filter([1, 2, 3, 4, 5, 6]))
    print(use_lambda_with_sorted(["apple", "pie", "banana"]))

