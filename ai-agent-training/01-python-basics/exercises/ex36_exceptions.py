"""
练习 36: 异常处理
难度: 🟡 进阶
预计时间: 15分钟

对比学习：
JS:  try { ... } catch (e) { ... } finally { ... }
Python: try: ... except Exception as e: ... finally: ...

关键区别：
1. Python用except（不是catch）
2. Python可以捕获特定异常类型
3. Python有else子句（没有异常时执行）
"""


def safe_divide(a: float, b: float) -> float:
    """
    安全除法，处理除零错误
    
    参数:
        a: 被除数
        b: 除数
    
    返回:
        除法结果，如果除零返回0.0
    """
    # TODO: 使用 try/except 处理 ZeroDivisionError
    pass


def safe_get_value(data: dict, key: str, default=None):
    """
    安全获取字典值，处理KeyError
    
    参数:
        data: 字典
        key: 键
        default: 默认值
    
    返回:
        值或默认值
    """
    # TODO: 使用 try/except 或 .get() 方法
    pass


def exception_types() -> dict:
    """
    演示不同异常类型
    
    返回:
        {
            "value_error": 捕获ValueError的示例,
            "type_error": 捕获TypeError的示例,
            "key_error": 捕获KeyError的示例
        }
    """
    # TODO: 实现不同异常类型的捕获
    pass


if __name__ == "__main__":
    print(safe_divide(10, 2))
    print(safe_divide(10, 0))
    print(safe_get_value({"a": 1}, "a"))
    print(safe_get_value({"a": 1}, "b", "default"))

