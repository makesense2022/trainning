"""
练习 18: 嵌套数据结构
难度: 🟡 进阶
预计时间: 15分钟

处理嵌套的列表、字典等复杂数据结构
"""


def access_nested_dict(data: dict, keys: list):
    """
    访问嵌套字典的值
    
    参数:
        data: {"user": {"name": "Alice", "age": 25}}
        keys: ["user", "name"]
    
    返回:
        对应的值（"Alice"）
    """
    # TODO: 根据keys路径访问嵌套值
    pass


def flatten_nested_dict(data: dict, parent_key: str = "", sep: str = ".") -> dict:
    """
    展平嵌套字典
    
    参数:
        data: {"user": {"name": "Alice", "age": 25}}
        parent_key: 父键前缀
        sep: 分隔符
    
    返回:
        {"user.name": "Alice", "user.age": 25}
    """
    # TODO: 递归展平字典
    pass


def deep_copy_nested(data):
    """
    深拷贝嵌套结构
    
    参数:
        data: 嵌套的列表或字典
    
    返回:
        深拷贝的结果
    """
    # TODO: 使用copy.deepcopy或手动实现
    import copy
    return copy.deepcopy(data)


def merge_nested_dicts(dict1: dict, dict2: dict) -> dict:
    """
    合并嵌套字典
    
    参数:
        dict1: {"a": 1, "b": {"c": 2}}
        dict2: {"b": {"d": 3}, "e": 4}
    
    返回:
        合并后的字典 {"a": 1, "b": {"c": 2, "d": 3}, "e": 4}
    """
    # TODO: 递归合并字典
    pass


if __name__ == "__main__":
    data = {"user": {"name": "Alice", "age": 25}}
    print(access_nested_dict(data, ["user", "name"]))
    print(flatten_nested_dict(data))
    print(merge_nested_dicts({"a": 1}, {"b": 2}))

