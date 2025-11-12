"""
练习 29: 递归
难度: 🟡 进阶
预计时间: 15分钟

递归：函数调用自身
"""


def factorial(n: int) -> int:
    """
    计算阶乘（递归实现）
    
    参数:
        n: 非负整数
    
    返回:
        n的阶乘
    
    示例:
        factorial(5) -> 120 (5*4*3*2*1)
    """
    # TODO: 使用递归实现
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n: int) -> int:
    """
    计算斐波那契数列第n项（递归实现）
    
    参数:
        n: 位置（从0开始）
    
    返回:
        斐波那契数
    
    示例:
        fibonacci(5) -> 5 (0,1,1,2,3,5)
    """
    # TODO: 使用递归实现
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def binary_search(arr: list, target: int, left: int = 0, right: int = None) -> int:
    """
    二分搜索（递归实现）
    
    参数:
        arr: 有序列表
        target: 目标值
        left: 左边界
        right: 右边界
    
    返回:
        目标值的索引，如果不存在返回-1
    """
    # TODO: 使用递归实现二分搜索
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, left, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, right)


def flatten_recursive(nested_list: list) -> list:
    """
    递归展平嵌套列表（任意深度）
    
    参数:
        nested_list: 嵌套列表
    
    返回:
        展平后的列表
    
    示例:
        flatten_recursive([1, [2, [3, 4]], 5]) -> [1, 2, 3, 4, 5]
    """
    # TODO: 使用递归展平任意深度的嵌套列表
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_recursive(item))
        else:
            result.append(item)
    return result


if __name__ == "__main__":
    print(factorial(5))
    print(fibonacci(5))
    print(binary_search([1, 2, 3, 4, 5], 3))
    print(flatten_recursive([1, [2, [3, 4]], 5]))

