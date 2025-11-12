"""
练习 20: 集合操作
难度: 🟢 基础
预计时间: 15分钟

目标：掌握集合的常用操作
"""


def set_union(set1: set, set2: set) -> set:
    """
    集合并集
    
    参数:
        set1: 集合1
        set2: 集合2
    
    返回:
        并集
    
    示例:
        set_union({1, 2, 3}, {3, 4, 5}) -> {1, 2, 3, 4, 5}
    """
    # TODO: 使用|操作符或union()方法
    return set1 | set2


def set_intersection(set1: set, set2: set) -> set:
    """
    集合交集
    
    参数:
        set1: 集合1
        set2: 集合2
    
    返回:
        交集
    
    示例:
        set_intersection({1, 2, 3}, {3, 4, 5}) -> {3}
    """
    # TODO: 使用&操作符或intersection()方法
    return set1 & set2


def set_difference(set1: set, set2: set) -> set:
    """
    集合差集（在set1中但不在set2中）
    
    参数:
        set1: 集合1
        set2: 集合2
    
    返回:
        差集
    
    示例:
        set_difference({1, 2, 3}, {3, 4, 5}) -> {1, 2}
    """
    # TODO: 使用-操作符或difference()方法
    return set1 - set2


def set_symmetric_difference(set1: set, set2: set) -> set:
    """
    集合对称差集（在set1或set2中，但不同时在两者中）
    
    参数:
        set1: 集合1
        set2: 集合2
    
    返回:
        对称差集
    
    示例:
        set_symmetric_difference({1, 2, 3}, {3, 4, 5}) -> {1, 2, 4, 5}
    """
    # TODO: 使用^操作符或symmetric_difference()方法
    return set1 ^ set2


def remove_duplicates_with_set(items: list) -> list:
    """
    使用集合去重（保持顺序）
    
    参数:
        items: 列表
    
    返回:
        去重后的列表（保持原有顺序）
    
    注意：set()会丢失顺序，需要使用其他方法
    """
    # TODO: 使用dict.fromkeys()或列表推导式保持顺序
    
    return list(dict.fromkeys(items))


if __name__ == "__main__":
    print(set_union({1, 2, 3}, {3, 4, 5}))
    print(set_intersection({1, 2, 3}, {3, 4, 5}))
    print(set_difference({1, 2, 3}, {3, 4, 5}))
    print(set_symmetric_difference({1, 2, 3}, {3, 4, 5}))
    print(remove_duplicates_with_set([1, 2, 2, 3, 1, 4]))

