"""
练习 15: 字典推导式
难度: 🟡 进阶
预计时间: 10分钟

类似列表推导式，但生成字典
语法: {key: value for item in iterable}
"""


def dict_from_list(items: list) -> dict:
    """
    从列表创建字典（索引作为key）
    
    参数:
        items: ["a", "b", "c"]
    
    返回:
        {0: "a", 1: "b", 2: "c"}
    """
    # TODO: 使用字典推导式
    return {i: item for i, item in enumerate(items)}
    pass


def dict_from_two_lists(keys: list, values: list) -> dict:
    """
    从两个列表创建字典
    
    参数:
        keys: ["name", "age"]
        values: ["Alice", 25]
    
    返回:
        {"name": "Alice", "age": 25}
    """
    # TODO: 使用zip和字典推导式
    pass


def dict_with_condition(items: list) -> dict:
    """
    带条件的字典推导式
    
    只包含偶数索引的元素
    
    参数:
        items: ["a", "b", "c", "d", "e"]
    
    返回:
        {0: "a", 2: "c", 4: "e"}
    """
    # TODO: 使用条件过滤
    pass


if __name__ == "__main__":
    print(dict_from_list(["a", "b", "c"]))
    print(dict_from_two_lists(["name", "age"], ["Alice", 25]))
    print(dict_with_condition(["a", "b", "c", "d", "e"]))

