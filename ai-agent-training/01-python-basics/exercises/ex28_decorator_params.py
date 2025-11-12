"""
练习 28: 带参数的装饰器
难度: 🔴 挑战
预计时间: 25分钟

装饰器工厂：返回装饰器的函数
"""

from functools import wraps


def retry(max_attempts: int = 3):
    """
    重试装饰器（带参数）
    
    参数:
        max_attempts: 最大尝试次数
    
    返回:
        装饰器函数
    
    使用:
        @retry(max_attempts=5)
        def flaky_function():
            ...
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # TODO: 实现重试逻辑
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise e
                    print(f"尝试 {attempt + 1} 失败，重试...")
            return None
        return wrapper
    return decorator


def rate_limit(calls_per_second: float = 1.0):
    """
    速率限制装饰器
    
    参数:
        calls_per_second: 每秒允许的调用次数
    
    返回:
        装饰器函数
    """
    import time
    
    def decorator(func):
        last_called = [0.0]
        min_interval = 1.0 / calls_per_second
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            # TODO: 实现速率限制
            elapsed = time.time() - last_called[0]
            if elapsed < min_interval:
                time.sleep(min_interval - elapsed)
            last_called[0] = time.time()
            return func(*args, **kwargs)
        return wrapper
    return decorator


def validate_types(**type_checks):
    """
    类型验证装饰器
    
    参数:
        **type_checks: 参数名和类型的映射
    
    示例:
        @validate_types(a=int, b=str)
        def func(a, b):
            ...
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # TODO: 验证参数类型
            # 获取函数签名
            import inspect
            sig = inspect.signature(func)
            bound = sig.bind(*args, **kwargs)
            bound.apply_defaults()
            
            # 验证类型
            for param_name, expected_type in type_checks.items():
                if param_name in bound.arguments:
                    value = bound.arguments[param_name]
                    if not isinstance(value, expected_type):
                        raise TypeError(f"{param_name}应该是{expected_type}，但得到{type(value)}")
            
            return func(*args, **kwargs)
        return wrapper
    return decorator


if __name__ == "__main__":
    @retry(max_attempts=3)
    def flaky_function():
        import random
        if random.random() < 0.5:
            raise ValueError("随机失败")
        return "成功"
    
    result = flaky_function()
    print(result)

