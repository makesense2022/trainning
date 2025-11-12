"""
练习 12: List切片技巧
难度: 🟡 进阶
预计时间: 15分钟

Python切片语法：list[start:stop:step]
- start: 起始索引（包含）
- stop: 结束索引（不包含）
- step: 步长
"""


def slice_basics(items: list) -> dict:
    """
    基础切片操作
    
    参数:
        items: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    返回:
        {
            "first_three": items[:3],      # [0, 1, 2]
            "last_three": items[-3:],      # [7, 8, 9]
            "middle": items[3:7],           # [3, 4, 5, 6]
            "every_other": items[::2],      # [0, 2, 4, 6, 8]
            "reverse": items[::-1]          # [9, 8, 7, ..., 0]
        }
    """
    # TODO: 实现各种切片
    return {
        "first_three": items[:3],
        "last_three": items[-3:],
        "middle": items[3:7],
        "every_other": items[::2],
        "reverse": items[::-1],
    }


def slice_with_step(items: list, step: int) -> list:
    """
    带步长的切片
    
    参数:
        items: 列表
        step: 步长
    
    返回:
        切片后的列表
    """
    # TODO: 使用步长切片
    return items[::step]


def slice_assignment(items: list, start: int, stop: int, replacement: list) -> list:
    """
    切片赋值（修改原列表的一部分）
    
    参数:
        items: 列表
        start: 起始索引
        stop: 结束索引
        replacement: 替换的列表
    
    返回:
        修改后的列表
    
    示例:
        slice_assignment([1, 2, 3, 4, 5], 1, 3, [10, 20])
        -> [1, 10, 20, 4, 5]
    """
    # TODO: 使用切片赋值
    items[start:stop] = replacement
    return items


if __name__ == "__main__":
    items = list(range(10))
    print(slice_basics(items))
    print(slice_with_step(items, 3))
    print(slice_assignment([1, 2, 3, 4, 5], 1, 3, [10, 20]))

