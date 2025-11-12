"""
练习 17: Tuple元组
难度: 🟢 基础
预计时间: 10分钟

Tuple特点：
- 不可变（immutable）
- 有序
- 可以包含不同类型
- 用()创建，但逗号才是关键
"""


def create_tuple() -> tuple:
    """
    创建元组
    
    返回:
        (1, 2, 3) 元组
    """
    # TODO: 创建元组
    pass


def tuple_unpacking(data: tuple) -> dict:
    """
    元组解包
    
    参数:
        data: ("Alice", 25, "Beijing")
    
    返回:
        {"name": "Alice", "age": 25, "city": "Beijing"}
    """
    # TODO: 解包元组
    pass


def tuple_vs_list() -> dict:
    """
    演示元组和列表的区别
    
    返回:
        {
            "tuple_immutable": 尝试修改元组会怎样,
            "list_mutable": 列表可以修改,
            "tuple_use_case": "元组适合用作字典key或函数返回值"
        }
    """
    # TODO: 演示区别
    pass


if __name__ == "__main__":
    print(create_tuple())
    print(tuple_unpacking(("Alice", 25, "Beijing")))

