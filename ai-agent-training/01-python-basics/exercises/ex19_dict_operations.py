"""
练习 19: 字典操作
难度: 🟢 基础
预计时间: 15分钟

目标：掌握字典的常用操作
"""


def merge_dicts(dict1: dict, dict2: dict) -> dict:
    """
    合并两个字典
    
    参数:
        dict1: 字典1
        dict2: 字典2
    
    返回:
        合并后的字典（dict2的值会覆盖dict1）
    
    示例:
        merge_dicts({"a": 1, "b": 2}, {"b": 3, "c": 4})
        -> {"a": 1, "b": 3, "c": 4}
    """
    # TODO: 使用**解包或update()方法
    result = dict1.copy()
    result.update(dict2)
    return result


def get_nested_value(data: dict, keys: list):
    """
    获取嵌套字典的值
    
    参数:
        data: 字典 {"user": {"name": "Alice", "age": 25}}
        keys: 键路径 ["user", "name"]
    
    返回:
        对应的值（"Alice"）
    """
    # TODO: 根据keys路径访问嵌套值
    result = data
    for key in keys:
        if isinstance(result, dict) and key in result:
            result = result[key]
        else:
            return None
    return result


def filter_dict_by_value(data: dict, condition) -> dict:
    """
    根据值过滤字典
    
    参数:
        data: 字典
        condition: 条件函数（如 lambda x: x > 10）
    
    返回:
        过滤后的字典
    
    示例:
        filter_dict_by_value({"a": 5, "b": 15, "c": 20}, lambda x: x > 10)
        -> {"b": 15, "c": 20}
    """
    # TODO: 使用字典推导式过滤
    return {k: v for k, v in data.items() if condition(v)}


def invert_dict(data: dict) -> dict:
    """
    反转字典（键值互换）
    
    参数:
        data: 字典 {"a": 1, "b": 2}
    
    返回:
        反转后的字典 {1: "a", 2: "b"}
    
    注意：如果值有重复，后面的会覆盖前面的
    """
    # TODO: 使用字典推导式反转
    return {v: k for k, v in data.items()}


if __name__ == "__main__":
    print(merge_dicts({"a": 1, "b": 2}, {"b": 3, "c": 4}))
    print(get_nested_value({"user": {"name": "Alice"}}, ["user", "name"]))
    print(filter_dict_by_value({"a": 5, "b": 15, "c": 20}, lambda x: x > 10))
    print(invert_dict({"a": 1, "b": 2}))

