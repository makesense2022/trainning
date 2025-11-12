"""
练习 23: *args和**kwargs
难度: 🟡 进阶
预计时间: 15分钟

对比学习：
JS:  function sum(...args) { return args.reduce((a, b) => a + b); }
Python: def sum(*args): return sum(args)

关键概念：
- *args: 接收任意数量的位置参数（打包成元组）
- **kwargs: 接收任意数量的关键字参数（打包成字典）
"""


def sum_args(*args) -> int:
    """
    计算所有位置参数的和
    
    JS: function sum(...args) { return args.reduce((a, b) => a + b, 0); }
    Python: def sum_args(*args): return sum(args)
    
    参数:
        *args: 任意数量的数字
    
    返回:
        所有数字的和
    
    示例:
        sum_args(1, 2, 3) -> 6
        sum_args(1, 2, 3, 4, 5) -> 15
    """
    # TODO: 使用 *args 实现
    pass


def print_kwargs(**kwargs) -> dict:
    """
    接收任意关键字参数并返回字典
    
    JS: function printKwargs(obj) { return obj; }
    Python: def print_kwargs(**kwargs): return kwargs
    
    参数:
        **kwargs: 任意关键字参数
    
    返回:
        包含所有关键字参数的字典
    
    示例:
        print_kwargs(name="Alice", age=25)
        -> {"name": "Alice", "age": 25}
    """
    # TODO: 使用 **kwargs 实现
    pass


def flexible_function(*args, **kwargs) -> dict:
    """
    同时接收位置参数和关键字参数
    
    参数:
        *args: 位置参数
        **kwargs: 关键字参数
    
    返回:
        {
            "args": args的元组,
            "kwargs": kwargs的字典
        }
    
    示例:
        flexible_function(1, 2, 3, name="Alice")
        -> {"args": (1, 2, 3), "kwargs": {"name": "Alice"}}
    """
    # TODO: 同时使用 *args 和 **kwargs
    pass


if __name__ == "__main__":
    print(sum_args(1, 2, 3))
    print(print_kwargs(name="Alice", age=25))
    print(flexible_function(1, 2, 3, name="Alice"))

