"""
练习 07: 多重赋值和解包
难度: 🟡 进阶
预计时间: 10分钟

对比学习：
JS:  const [a, b] = [1, 2]; const {x, y} = {x: 1, y: 2};
Python: a, b = [1, 2]; x, y = {"x": 1, "y": 2}.values()

Python的解包更强大：
- 可以解包任意可迭代对象
- 支持*args和**kwargs
- 支持嵌套解包
"""


def unpack_list(items: list) -> tuple:
    """
    解包列表
    
    JS: const [first, second, third] = items;
    Python: first, second, third = items
    
    参数:
        items: 包含3个元素的列表
    
    返回:
        (first, second, third) 元组
    
    示例:
        unpack_list([1, 2, 3]) -> (1, 2, 3)
    """
    # TODO: 解包列表
    pass


def unpack_with_rest(items: list) -> tuple:
    """
    解包列表，第一个元素单独，其余打包
    
    JS: const [first, ...rest] = items;
    Python: first, *rest = items
    
    参数:
        items: 列表
    
    返回:
        (first, rest) 元组，rest是列表
    
    示例:
        unpack_with_rest([1, 2, 3, 4]) -> (1, [2, 3, 4])
    """
    # TODO: 使用 *rest 解包
    pass


def swap_variables(a, b) -> tuple:
    """
    交换两个变量（使用解包）
    
    JS: [a, b] = [b, a];
    Python: a, b = b, a
    
    参数:
        a: 第一个值
        b: 第二个值
    
    返回:
        (b, a) 元组
    """
    # TODO: 使用解包交换
    pass


def unpack_dict(data: dict) -> tuple:
    """
    解包字典的值
    
    JS: const {name, age} = data;
    Python: name, age = data.values() 或 name, age = data["name"], data["age"]
    
    参数:
        data: {"name": "Alice", "age": 25}
    
    返回:
        ("Alice", 25) 元组
    """
    # TODO: 解包字典值
    pass


if __name__ == "__main__":
    print(unpack_list([1, 2, 3]))
    print(unpack_with_rest([1, 2, 3, 4]))
    print(swap_variables(5, 10))
    print(unpack_dict({"name": "Alice", "age": 25}))

