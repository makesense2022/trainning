"""
练习 36: itertools技巧
难度: 🔴 挑战
预计时间: 25分钟

目标：使用itertools进行高效迭代
"""

from itertools import chain, combinations, permutations, cycle, islice


def chain_iterables(*iterables):
    """
    链式迭代多个可迭代对象
    
    参数:
        *iterables: 多个可迭代对象
    
    返回:
        链式迭代结果列表
    """
    # TODO: 使用itertools.chain
    return list(chain(*iterables))


def get_combinations(items: list, r: int) -> list:
    """
    获取组合
    
    参数:
        items: 列表
        r: 组合长度
    
    返回:
        组合列表
    """
    # TODO: 使用itertools.combinations
    return list(combinations(items, r))


def get_permutations(items: list, r: int = None) -> list:
    """
    获取排列
    
    参数:
        items: 列表
        r: 排列长度（None表示全排列）
    
    返回:
        排列列表
    """
    # TODO: 使用itertools.permutations
    return list(permutations(items, r))


def cycle_demo(items: list, n: int = 10) -> list:
    """
    循环迭代演示
    
    参数:
        items: 列表
        n: 迭代次数
    
    返回:
        前n个元素
    """
    # TODO: 使用itertools.cycle和islice
    return list(islice(cycle(items), n))


if __name__ == "__main__":
    print(chain_iterables([1, 2], [3, 4], [5]))
    print(get_combinations([1, 2, 3], 2))
    print(get_permutations([1, 2, 3], 2))
    print(cycle_demo([1, 2, 3], 7))

