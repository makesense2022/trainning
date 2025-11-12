"""
练习 14: Dict基础操作
难度: 🟢 基础
预计时间: 10分钟

对比学习：
JS:  const obj = {name: "Alice"}; obj.age = 25; obj["city"] = "Beijing";
Python: obj = {"name": "Alice"}; obj["age"] = 25; obj.get("city", "Unknown")

关键区别：
1. Python的key必须是不可变类型（字符串、数字、元组）
2. Python用{}创建，但key必须是字符串时用引号
3. Python有.get()方法（安全访问）
"""


def create_dict() -> dict:
    """
    创建字典
    
    JS: {name: "Alice", age: 25}
    Python: {"name": "Alice", "age": 25}
    
    返回:
        {"name": "Alice", "age": 25}
    """
    # TODO: 创建字典
    pass


def access_dict(data: dict, key: str):
    """
    访问字典值
    
    JS: data[key] 或 data.key
    Python: data[key] 或 data.get(key)
    
    参数:
        data: 字典
        key: 键
    
    返回:
        对应的值，如果不存在返回None
    """
    # TODO: 使用 .get() 安全访问
    pass


def update_dict(data: dict, key: str, value) -> dict:
    """
    更新字典
    
    JS: data[key] = value
    Python: data[key] = value (相同)
    
    参数:
        data: 字典
        key: 键
        value: 值
    
    返回:
        更新后的字典
    """
    # TODO: 更新字典
    pass


def dict_methods(data: dict) -> dict:
    """
    演示字典常用方法
    
    返回:
        {
            "keys": 所有键的列表,
            "values": 所有值的列表,
            "items": 所有键值对的列表,
            "get": 使用get获取值（不存在返回"default"）
        }
    
    示例:
        dict_methods({"a": 1, "b": 2})
        -> {
            "keys": ["a", "b"],
            "values": [1, 2],
            "items": [("a", 1), ("b", 2)],
            "get": 1
        }
    """
    # TODO: 实现各种字典方法
    pass


if __name__ == "__main__":
    print(create_dict())
    data = {"name": "Alice"}
    print(access_dict(data, "name"))
    print(update_dict(data, "age", 25))
    print(dict_methods({"a": 1, "b": 2}))

