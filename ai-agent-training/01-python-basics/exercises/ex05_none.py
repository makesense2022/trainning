"""
练习 05: None vs undefined/null
难度: 🟢 基础
预计时间: 5分钟

对比学习：
JS:  null, undefined
Python: None (只有一个"空值")

关键区别：
1. Python只有None（没有null和undefined）
2. None是单例对象（只有一个None实例）
3. 检查None用 is None（不是 == None）
"""


def return_none() -> None:
    """
    返回None
    
    JS: return null; 或 return undefined;
    Python: return None
    
    返回:
        None
    """
    # TODO: 返回None
    pass


def check_none(value) -> bool:
    """
    检查值是否为None
    
    重要：使用 is None（不是 == None）
    
    JS: value === null || value === undefined
    Python: value is None
    
    参数:
        value: 任意值
    
    返回:
        如果是None返回True，否则返回False
    """
    # TODO: 使用 is None 检查
    pass


def none_vs_false() -> dict:
    """
    演示None和False的区别
    
    返回:
        {
            "none_is_false": bool(None),  # None是falsy
            "none_equals_false": None == False,  # 但None != False
            "none_is_none": None is None,  # True
            "type_of_none": type(None).__name__  # NoneType
        }
    """
    # TODO: 实现
    pass


def default_value(value):
    """
    如果value是None，返回默认值"default"
    
    JS: value ?? "default"
    Python: value or "default" (如果value是None)
    
    参数:
        value: 可能为None的值
    
    返回:
        value（如果不是None）或"default"
    """
    # TODO: 实现默认值逻辑
    pass


if __name__ == "__main__":
    print(return_none())
    print(check_none(None))
    print(check_none("hello"))
    print(none_vs_false())
    print(default_value(None))
    print(default_value("hello"))

