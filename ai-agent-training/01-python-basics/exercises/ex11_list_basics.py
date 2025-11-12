"""
练习 11: List基础操作
难度: 🟢 基础
预计时间: 10分钟

对比学习：
JS:  const arr = [1, 2, 3]; arr.push(4); arr.length;
Python: arr = [1, 2, 3]; arr.append(4); len(arr)

关键区别：
1. Python用append()而不是push()
2. Python用len()而不是.length属性
3. Python支持负数索引（arr[-1]是最后一个）
"""


def create_list() -> list:
    """
    创建一个包含1, 2, 3的列表
    
    JS: [1, 2, 3]
    Python: [1, 2, 3]
    
    返回:
        [1, 2, 3]
    """
    # TODO: 创建列表
    pass


def append_item(items: list, item) -> list:
    """
    向列表末尾添加元素
    
    JS: items.push(item)
    Python: items.append(item)
    
    参数:
        items: 列表
        item: 要添加的元素
    
    返回:
        修改后的列表（原地修改，但返回它以便测试）
    """
    # TODO: 使用 append() 实现
    pass


def get_length(items: list) -> int:
    """
    获取列表长度
    
    JS: items.length
    Python: len(items)
    
    参数:
        items: 列表
    
    返回:
        列表长度
    """
    # TODO: 使用 len() 实现
    pass


def access_by_index(items: list, index: int):
    """
    通过索引访问元素
    
    Python支持负数索引：
    - items[0] 第一个
    - items[-1] 最后一个
    - items[-2] 倒数第二个
    
    参数:
        items: 列表
        index: 索引（可以是负数）
    
    返回:
        对应索引的元素
    """
    # TODO: 使用索引访问
    pass


def list_slicing(items: list) -> dict:
    """
    列表切片操作
    
    JS: items.slice(start, end)
    Python: items[start:end:step]
    
    参数:
        items: [0, 1, 2, 3, 4, 5]
    
    返回:
        {
            "first_three": items[:3],  # [0, 1, 2]
            "last_two": items[-2:],     # [4, 5]
            "middle": items[2:4],       # [2, 3]
            "reverse": items[::-1]      # [5, 4, 3, 2, 1, 0]
        }
    """
    # TODO: 实现各种切片
    pass


if __name__ == "__main__":
    print(create_list())
    items = [1, 2, 3]
    print(append_item(items, 4))
    print(get_length([1, 2, 3]))
    print(access_by_index([1, 2, 3], -1))
    print(list_slicing([0, 1, 2, 3, 4, 5]))

