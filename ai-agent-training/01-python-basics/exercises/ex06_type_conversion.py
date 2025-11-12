"""
练习 06: 类型转换和检查
难度: 🟢 基础
预计时间: 10分钟

对比学习：
JS:  Number("123"), String(123), Boolean(1)
Python: int("123"), str(123), bool(1)

关键函数：
- int(): 转整数
- float(): 转浮点数
- str(): 转字符串
- bool(): 转布尔值
- type(): 检查类型
- isinstance(): 类型检查（推荐）
"""


def convert_to_int(value) -> int:
    """
    将值转换为整数
    
    JS: Number(value) 或 parseInt(value)
    Python: int(value)
    
    参数:
        value: 可转换的值（字符串数字、浮点数等）
    
    返回:
        转换后的整数
    
    示例:
        convert_to_int("123") -> 123
        convert_to_int(3.14) -> 3
    """
    # TODO: 使用 int() 实现
    pass


def convert_to_string(value) -> str:
    """
    将值转换为字符串
    
    JS: String(value) 或 value.toString()
    Python: str(value)
    
    参数:
        value: 任意值
    
    返回:
        字符串表示
    """
    # TODO: 使用 str() 实现
    pass


def check_type(value) -> str:
    """
    检查值的类型
    
    JS: typeof value
    Python: type(value).__name__
    
    参数:
        value: 任意值
    
    返回:
        类型名称字符串（如 "int", "str", "list"）
    """
    # TODO: 使用 type() 实现
    pass


def isinstance_check(value, type_class) -> bool:
    """
    使用isinstance检查类型（推荐方式）
    
    JS: value instanceof Type
    Python: isinstance(value, type_class)
    
    参数:
        value: 要检查的值
        type_class: 类型（如 int, str, list）
    
    返回:
        如果是该类型返回True
    
    示例:
        isinstance_check(123, int) -> True
        isinstance_check("123", int) -> False
    """
    # TODO: 使用 isinstance() 实现
    pass


if __name__ == "__main__":
    print(convert_to_int("123"))
    print(convert_to_string(123))
    print(check_type(123))
    print(isinstance_check(123, int))

