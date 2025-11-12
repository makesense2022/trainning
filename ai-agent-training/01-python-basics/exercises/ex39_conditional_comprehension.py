"""
练习 39: 列表推导式中的条件
难度: 🟡 进阶
预计时间: 10分钟

在列表推导式中使用条件过滤和条件表达式
"""


def filter_even(numbers: list) -> list:
    """
    过滤偶数（使用列表推导式）
    
    参数:
        numbers: 数字列表
    
    返回:
        偶数列表
    
    示例:
        filter_even([1, 2, 3, 4, 5]) -> [2, 4]
    """
    # TODO: 使用列表推导式过滤
    return [x for x in numbers if x % 2 == 0]


def map_with_condition(numbers: list) -> list:
    """
    条件映射：正数变平方，负数变0
    
    参数:
        numbers: 数字列表
    
    返回:
        处理后的列表
    
    示例:
        map_with_condition([1, -2, 3, -4]) -> [1, 0, 9, 0]
    """
    # TODO: 使用条件表达式
    return [x * x if x > 0 else 0 for x in numbers]


def complex_comprehension(data: list) -> list:
    """
    复杂列表推导式：过滤+映射+条件
    
    参数:
        data: 数字列表
    
    返回:
        大于5的偶数，每个乘以2
    
    示例:
        complex_comprehension([1, 2, 3, 4, 5, 6, 7, 8]) -> [12, 16]
    """
    # TODO: 组合多个条件
    return [x * 2 for x in data if x > 5 and x % 2 == 0]


def nested_comprehension_with_condition(matrix: list) -> list:
    """
    嵌套列表推导式+条件
    
    参数:
        matrix: 二维列表
    
    返回:
        展平后的大于5的元素
    
    示例:
        nested_comprehension_with_condition([[1, 6], [3, 8], [2, 9]])
        -> [6, 8, 9]
    """
    # TODO: 嵌套推导式+条件
    return [item for row in matrix for item in row if item > 5]


if __name__ == "__main__":
    print(filter_even([1, 2, 3, 4, 5]))
    print(map_with_condition([1, -2, 3, -4]))
    print(complex_comprehension([1, 2, 3, 4, 5, 6, 7, 8]))
    print(nested_comprehension_with_condition([[1, 6], [3, 8], [2, 9]]))

