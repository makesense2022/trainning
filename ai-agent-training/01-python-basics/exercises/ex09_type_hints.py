"""
练习 09: 类型注解（Type Hints）
难度: 🟡 进阶
预计时间: 15分钟

对比学习：
JS/TS:  function add(a: number, b: number): number { return a + b; }
Python: def add(a: int, b: int) -> int: return a + b

Python的类型注解是可选的，但强烈推荐使用！
"""

from typing import List, Dict, Optional, Union


def add_with_hints(a: int, b: int) -> int:
    """
    带类型注解的加法函数
    
    参数:
        a: 整数
        b: 整数
    
    返回:
        整数
    """
    # TODO: 实现加法
    return a + b


def process_list(items: List[str]) -> List[int]:
    """
    处理字符串列表，返回长度列表
    
    参数:
        items: 字符串列表
    
    返回:
        每个字符串长度的列表
    
    示例:
        process_list(["hello", "world"]) -> [5, 5]
    
    类型注解说明:
        List[str] - 字符串列表
        List[int] - 整数列表
    """
    # 使用列表推导式返回每个字符串的长度
    return [len(item) for item in items]


def get_user_info(user_id: int) -> Optional[Dict[str, Union[str, int]]]:
    """
    获取用户信息（可能不存在）
    
    参数:
        user_id: 用户ID
    
    返回:
        用户信息字典，如果不存在返回None
    
    类型说明:
        Optional[Dict] = Dict | None  (可能返回None)
        Union[str, int] = str | int   (值可能是字符串或整数)
    """
    # 模拟用户数据库
    users = {
        1: {"name": "Alice", "age": 25},
        2: {"name": "Bob", "age": 30}
    }
    
    # 如果用户存在，返回信息；否则返回None
    if user_id in users:
        return users[user_id]
    return None


def process_data(data: Union[str, int, List]) -> str:
    """
    处理不同类型的数据
    
    参数:
        data: 可能是字符串、整数或列表
    
    返回:
        处理后的字符串
    
    类型说明:
        Union[str, int, List] - 可能是字符串、整数或列表中的任意一种
    """
    # 根据不同类型进行不同处理
    if isinstance(data, str):
        return f"字符串: {data.upper()}"
    elif isinstance(data, int):
        return f"整数: {data * 2}"
    elif isinstance(data, list):
        return f"列表: {len(data)} 个元素"
    else:
        return f"未知类型: {type(data)}"


if __name__ == "__main__":
    print(add_with_hints(5, 3))
    print(process_list(["hello", "world"]))
    print(get_user_info(1))
    print(process_data("hello"))
    print(process_data(123))
    print(process_data([1, 2, 3]))

