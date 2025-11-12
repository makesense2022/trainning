"""
练习 32: for循环
难度: 🟢 基础
预计时间: 10分钟

对比学习：
JS:  for (const item of items) { ... }
Python: for item in items: ...

关键特性：
1. Python的for循环直接遍历可迭代对象
2. 使用range()生成数字序列
3. 支持enumerate()同时获取索引和值
"""


def iterate_list(items: list) -> list:
    """
    遍历列表，将每个元素乘以2
    
    JS: items.map(x => x * 2)
    Python: [x * 2 for x in items] 或 for循环
    
    参数:
        items: 数字列表
    
    返回:
        每个元素乘以2后的新列表
    """
    # TODO: 使用for循环实现
    pass


def iterate_with_range(n: int) -> list:
    """
    使用range生成0到n-1的序列并遍历
    
    参数:
        n: 数字
    
    返回:
        [0, 1, 2, ..., n-1] 的列表
    """
    # TODO: 使用 for i in range(n) 实现
    pass


def iterate_with_enumerate(items: list) -> list:
    """
    使用enumerate同时获取索引和值
    
    JS: items.forEach((item, index) => { ... })
    Python: for index, item in enumerate(items): ...
    
    参数:
        items: 列表
    
    返回:
        [(index, value), ...] 的列表
    
    示例:
        iterate_with_enumerate(["a", "b", "c"])
        -> [(0, "a"), (1, "b"), (2, "c")]
    """
    # TODO: 使用 enumerate() 实现
    pass


if __name__ == "__main__":
    print(iterate_list([1, 2, 3]))
    print(iterate_with_range(5))
    print(iterate_with_enumerate(["a", "b", "c"]))

