"""
练习 35: collections模块
难度: 🟡 进阶
预计时间: 20分钟

目标：使用collections模块的高级数据结构
"""

from collections import defaultdict, Counter, deque, namedtuple


def use_defaultdict():
    """
    使用defaultdict（自动创建默认值）
    
    返回:
        示例字典
    """
    # TODO: 创建defaultdict
    dd = defaultdict(list)
    dd["a"].append(1)
    dd["a"].append(2)
    return dict(dd)


def use_counter(items: list) -> dict:
    """
    使用Counter统计元素出现次数
    
    参数:
        items: 列表
    
    返回:
        统计结果字典
    """
    # TODO: 使用Counter
    counter = Counter(items)
    return dict(counter)


def use_deque():
    """
    使用deque（双端队列）
    
    返回:
        操作结果
    """
    # TODO: 使用deque实现队列操作
    dq = deque([1, 2, 3])
    dq.appendleft(0)  # 左侧添加
    dq.append(4)      # 右侧添加
    return list(dq)


def use_namedtuple():
    """
    使用namedtuple（命名元组）
    
    返回:
        Point实例
    """
    # TODO: 创建namedtuple
    Point = namedtuple("Point", ["x", "y"])
    p = Point(1, 2)
    return p


if __name__ == "__main__":
    print(use_defaultdict())
    print(use_counter(["a", "b", "a", "c", "b", "a"]))
    print(use_deque())
    print(use_namedtuple())

