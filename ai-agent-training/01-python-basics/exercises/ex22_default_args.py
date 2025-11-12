"""
练习 22: 默认参数
难度: 🟢 基础
预计时间: 5分钟

对比学习：
JS:  function greet(name = "Guest") { ... }
Python: def greet(name="Guest"): ...

注意：默认参数只计算一次，不要用可变对象作为默认值！
"""


def greet(name: str = "Guest") -> str:
    """
    带默认参数的问候函数
    
    参数:
        name: 姓名（默认"Guest"）
    
    返回:
        问候语
    """
    # TODO: 实现
    pass


def add_numbers(a: int, b: int = 0, c: int = 0) -> int:
    """
    多个默认参数
    
    参数:
        a: 第一个数（必需）
        b: 第二个数（默认0）
        c: 第三个数（默认0）
    
    返回:
        三个数的和
    """
    # TODO: 实现
    pass


def mutable_default_trap():
    """
    演示可变默认参数的陷阱
    
    ❌ 错误示例：
    def append_to_list(item, my_list=[]):
        my_list.append(item)
        return my_list
    
    ✅ 正确方式：
    def append_to_list(item, my_list=None):
        if my_list is None:
            my_list = []
        my_list.append(item)
        return my_list
    
    返回:
        正确实现的函数
    """
    # TODO: 实现正确的版本
    def append_to_list(item, my_list=None):
        if my_list is None:
            my_list = []
        my_list.append(item)
        return my_list
    
    return append_to_list


if __name__ == "__main__":
    print(greet())
    print(greet("Alice"))
    print(add_numbers(1))
    print(add_numbers(1, 2))
    print(add_numbers(1, 2, 3))

