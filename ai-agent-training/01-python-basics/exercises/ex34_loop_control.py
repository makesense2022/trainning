"""
练习 34: 循环控制（break/continue）
难度: 🟢 基础
预计时间: 5分钟

对比学习：
JS:  break; continue;
Python: break; continue; (相同)
"""


def find_first_even(numbers: list) -> int:
    """
    找到第一个偶数（使用break）
    
    参数:
        numbers: 数字列表
    
    返回:
        第一个偶数，如果没有返回None
    """
    # TODO: 使用for循环和break
    for num in numbers:
        if num % 2 == 0:
            return num
    return None


def filter_positive(numbers: list) -> list:
    """
    过滤正数（使用continue跳过负数）
    
    参数:
        numbers: 数字列表
    
    返回:
        正数列表
    """
    # TODO: 使用for循环和continue
    result = []
    for num in numbers:
        if num <= 0:
            continue
        result.append(num)
    return result


def process_until_negative(numbers: list) -> list:
    """
    处理数字直到遇到负数（使用break）
    
    参数:
        numbers: 数字列表
    
    返回:
        处理后的列表（遇到负数就停止）
    """
    # TODO: 处理数字，遇到负数就break
    result = []
    for num in numbers:
        if num < 0:
            break
        result.append(num * 2)  # 处理：乘以2
    return result


if __name__ == "__main__":
    print(find_first_even([1, 3, 5, 8, 9]))
    print(filter_positive([-1, 2, -3, 4, 5]))
    print(process_until_negative([1, 2, 3, -1, 4, 5]))

