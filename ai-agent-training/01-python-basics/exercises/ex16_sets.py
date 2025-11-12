"""
练习 16: Set集合操作
难度: 🟢 基础
预计时间: 10分钟

Set特点：
- 无序
- 不重复
- 支持集合运算（交集、并集、差集）
"""


def create_set(items: list) -> set:
    """
    从列表创建集合（自动去重）
    
    参数:
        items: [1, 2, 2, 3, 3, 3]
    
    返回:
        {1, 2, 3}
    """
    return set[int](items)
    pass


def set_operations(set1: set, set2: set) -> dict:
    """
    集合运算
    
    参数:
        set1: {1, 2, 3, 4}
        set2: {3, 4, 5, 6}
    
    返回:
        {
            "union": set1 | set2,        # 并集 {1,2,3,4,5,6}
            "intersection": set1 & set2,  # 交集 {3,4}
            "difference": set1 - set2,    # 差集 {1,2}
            "symmetric_diff": set1 ^ set2  # 对称差集 {1,2,5,6}
        }
    """
    # TODO: 实现集合运算
    pass


def check_subset(set1: set, set2: set) -> bool:
    """
    检查set1是否是set2的子集
    
    参数:
        set1: {1, 2}
        set2: {1, 2, 3, 4}
    
    返回:
        True（如果set1是set2的子集）
    """
    # TODO: 使用 <= 或 issubset()
    pass


if __name__ == "__main__":
    print(create_set([1, 2, 2, 3, 3, 3]))
    print(set_operations({1, 2, 3, 4}, {3, 4, 5, 6}))
    print(check_subset({1, 2}, {1, 2, 3, 4}))

