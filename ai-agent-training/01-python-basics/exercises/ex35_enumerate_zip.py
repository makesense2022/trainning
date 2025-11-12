"""
练习 35: enumerate和zip
难度: 🟡 进阶
预计时间: 10分钟

enumerate: 同时获取索引和值
zip: 并行迭代多个序列
"""


def use_enumerate(items: list) -> list:
    """
    使用enumerate获取索引和值
    
    JS: items.forEach((item, index) => { ... })
    Python: for index, item in enumerate(items): ...
    
    参数:
        items: ["a", "b", "c"]
    
    返回:
        [(0, "a"), (1, "b"), (2, "c")]
    """
    # TODO: 使用enumerate
    pass


def use_zip(list1: list, list2: list) -> list:
    """
    使用zip并行迭代
    
    参数:
        list1: [1, 2, 3]
        list2: ["a", "b", "c"]
    
    返回:
        [(1, "a"), (2, "b"), (3, "c")]
    """
    # TODO: 使用zip
    pass


def create_dict_from_lists(keys: list, values: list) -> dict:
    """
    使用zip从两个列表创建字典
    
    参数:
        keys: ["name", "age"]
        values: ["Alice", 25]
    
    返回:
        {"name": "Alice", "age": 25}
    """
    # TODO: 使用zip和dict()
    pass


if __name__ == "__main__":
    print(use_enumerate(["a", "b", "c"]))
    print(use_zip([1, 2, 3], ["a", "b", "c"]))
    print(create_dict_from_lists(["name", "age"], ["Alice", 25]))

